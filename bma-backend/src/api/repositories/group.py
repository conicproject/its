from api.connections.oracle import OracleConnection
from rest_framework.exceptions import NotFound

import pandas as pd

class GroupRepository:

    def __init__(self):
        self.oracle_connection = OracleConnection().get_connection()

        self.not_found_msg = 'group not found'

    def get_by_id(self, id):
        sql_command = """
            SELECT g.*,d.NAME as DEPARTMENT_NAME FROM BMA_PHASE_II.GROUPS g JOIN BMA_PHASE_II.DEPARTMENTS d ON g.DEPARTMENT_ID = d.ID
            WHERE g.id = {}
        """.format(id)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        try:
            columes = [row[0] for row in cursor.description]
            df = pd.DataFrame(data=data, columns=columes)
            df = df.rename(columns={
                'ID': 'id',
                'DEPARTMENT_ID': 'department_id',
                'DEPARTMENT_NAME' : 'department_name',
                'USER_LEVEL_ID': 'user_level_id'
            })

            result = df.to_dict('records')
            data = result[0]

        except:
            response = {
                'status_code': 404,
                'message': self.not_found_msg
            }

            raise NotFound(response)

        return data