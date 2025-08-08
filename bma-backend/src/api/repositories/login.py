from api.repositories.user import UserRepository
from api.models.login import LoginModel
from api.logics.session import SessionLogic

from api.connections.oracle import OracleConnection
import cx_Oracle
import pandas as pd

from rest_framework.exceptions import NotFound

class LoginRepository:

    def __init__(self):
        self.user_repo = UserRepository()
        self.session_logic = SessionLogic()
        self.oracle_connection = OracleConnection().get_connection()

        self.password_fail_msg = 'incorrected password'


    def validate_session(self, id, msg):
        sql_command = '''
            SELECT ID, USER_ID, TO_CHAR(CREATED_AT, 'YYYY-MM-DD HH24:MI:SS') AS CREATED_AT, TO_CHAR(EXPIRED_AT , 'YYYY-MM-DD HH24:MI:SS') AS EXPIRED_AT
            FROM BMA_PHASE_II.LOGINS
            WHERE ID = {}
        '''.format(id)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        try:
            columes = [row[0] for row in cursor.description]
            df = pd.DataFrame(data=data, columns=columes)
            df = df.rename(columns={
                'ID': 'id',
                'USER_ID': 'user_id',
                'CREATED_AT': 'created_at',
                'EXPIRED_AT': 'expired_at'
            })
            df['created_at'] = pd.to_datetime(df['created_at'])
            df['expired_at'] = pd.to_datetime(df['expired_at'])

            result = df.to_dict('records')
            data = result[0]

        except:
            response = {
                'status_code': 404,
                'message': msg
            }

            raise NotFound(response)
        
        return data
    

    def stamp_login(self, user_id):
        created_at, expired_at = self.session_logic.session_timestamp()

        cursor = self.oracle_connection.cursor()
        new_id = cursor.var(cx_Oracle.NUMBER)

        sql_command = """
            INSERT INTO BMA_PHASE_II.LOGINS (USER_ID, CREATED_AT, EXPIRED_AT)
            VALUES ({}, TO_TIMESTAMP('{}', 'YYYY-MM-DD HH24:MI:SS'), TO_TIMESTAMP('{}', 'YYYY-MM-DD HH24:MI:SS'))
            returning ID into :python_var
        """.format(user_id, created_at, expired_at)

        cursor.execute(sql_command, [new_id])

        login_id = new_id.getvalue()
        login_id = int(login_id[0])
        self.oracle_connection.commit()

        get_sql_command = '''
            SELECT ID, USER_ID, TO_CHAR(CREATED_AT, 'YYYY-MM-DD HH24:MI:SS') AS CREATED_AT FROM BMA_PHASE_II.LOGINS
            WHERE ID = {}
        '''.format(login_id)

        cursor.execute(get_sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'ID': 'id',
            'USER_ID': 'user_id',
            'CREATED_AT': 'created_at'
        })

        result = df.to_dict('records')
        login = result[0]

        return login
