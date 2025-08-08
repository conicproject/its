from api.models.user import UserModel
from api.connections.oracle import OracleConnection
from rest_framework.exceptions import NotFound
from argon2 import PasswordHasher

import cx_Oracle
import pandas as pd

class UserRepository:

    def __init__(self):
        self.oracle_connection = OracleConnection().get_connection()

        self.not_found_msg = 'user not found'

    def validate_session(self, id, msg):
        sql_command = """
            SELECT * FROM BMA_PHASE_II.USERS
            WHERE id = {}
        """.format(id)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        try:
            columes = [row[0] for row in cursor.description]
            df = pd.DataFrame(data=data, columns=columes)
            df = df.rename(columns={
                'ID': 'id',
                'GROUP_ID': 'group_id',
                'NAME': 'name',
                'PASSWORD': 'password',
                'IS_SUPER_USER': 'is_super_user'
            })

            result = df.to_dict('records')
            data = result[0]

        except:
            response = {
                'status_code': 404,
                'message': msg
            }

            raise NotFound(response)
    

    def get_by_id(self, id):
        sql_command = """
            SELECT * FROM BMA_PHASE_II.USERS
            WHERE id = {}
        """.format(id)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        try:
            columes = [row[0] for row in cursor.description]
            df = pd.DataFrame(data=data, columns=columes)
            df = df.rename(columns={
                'ID': 'id',
                'GROUP_ID': 'group_id',
                'NAME': 'name',
                'PASSWORD': 'password',
                'IS_SUPER_USER': 'is_super_user'
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


    def get_by_name(self, name):
        sql_command = """
            SELECT * FROM BMA_PHASE_II.USERS u 
            WHERE name = '{}'
        """.format(name)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        try:
            columes = [row[0] for row in cursor.description]
            df = pd.DataFrame(data=data, columns=columes)
            df = df.rename(columns={
                'ID': 'id',
                'GROUP_ID': 'group_id',
                'NAME': 'name',
                'PASSWORD': 'password',
                'IS_SUPER_USER': 'is_super_user'
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

    def get_all(self):
        sql_command = """
            SELECT u.*,d.NAME AS DEPARTMENT_NAME  FROM BMA_PHASE_II.USERS u 
                JOIN BMA_PHASE_II.GROUPS g ON u.GROUP_ID = g.ID
                JOIN BMA_PHASE_II.DEPARTMENTS d ON g.DEPARTMENT_ID =d.ID 
        """

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        try:
            columes = [row[0] for row in cursor.description]
            df = pd.DataFrame(data=data, columns=columes)
            df = df.drop(['PASSWORD'], axis=1)
            df = df.rename(columns={
                'ID': 'id',
                'GROUP_ID': 'group_id',
                'NAME': 'name',
                'IS_SUPER_USER': 'is_super_user'
            })

            result = df.to_dict('records')
            data = result

        except:
            response = {
                'status_code': 404,
                'message': self.not_found_msg
            }

            raise NotFound(response)
        
        return data

    def get_group_user(self):
        sql_command = """
            SELECT g.*,ul.NAME AS USER_LEVEL_NAME FROM BMA_PHASE_II.GROUPS g
	            JOIN BMA_PHASE_II.USER_LEVELS ul  ON g.USER_LEVEL_ID  = ul.ID   
        """

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        try:
            columes = [row[0] for row in cursor.description]
            df = pd.DataFrame(data=data, columns=columes)
            df = df.rename(columns={
                'ID': 'id',
                'DEPARTMENT_ID': 'department_id',
                'USER_LEVEL_NAME': 'user_level_name',
                'USER_LEVEL_ID': 'user_level_id',
                'NAME': 'name',
                'DESCRIPTION':'description'
            })

            result = df.to_dict('records')
            data = result

        except:
            response = {
                'status_code': 404,
                'message': self.not_found_msg
            }

            raise NotFound(response)
        
        return data

    def get_all_group_department(self):
        sql_command = """
            SELECT g.*,d.NAME AS DEPARTMENT_NAME FROM BMA_PHASE_II.GROUPS g
	            JOIN BMA_PHASE_II.DEPARTMENTS d ON g.DEPARTMENT_ID = d.ID  
        """

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        try:
            columes = [row[0] for row in cursor.description]
            df = pd.DataFrame(data=data, columns=columes)
            df = df.rename(columns={
                'ID': 'group_id',
                'DEPARTMENT_ID': 'department_id',
                'DEPARTMENT_NAME': 'department_name',
                'USER_LEVEL_ID': 'user_level_id',
                'NAME': 'group_name',
                'DESCRIPTION':'description'
            })

            result = df.to_dict('records')
            data = result

        except:
            response = {
                'status_code': 404,
                'message': self.not_found_msg
            }

            raise NotFound(response)
        
        return data


    def insert(self,payloads):
        cursor = self.oracle_connection.cursor()
        new_id = cursor.var(cx_Oracle.NUMBER)
        ph = PasswordHasher()
        hash = ph.hash(payloads['password'])

        sql_command = """
            INSERT INTO BMA_PHASE_II.USERS (NAME, PASSWORD, EMAIL, PHONE, HOME_ADDRESS,GROUP_ID,IS_SUPER_USER)
            VALUES ('{}', '{}', '{}', '{}', '{}', '{}', {})
        """.format(payloads['name'], hash,
            payloads['email'], payloads['phone'], payloads['address'],payloads['group'],payloads['is_super_user']
        )

        cursor.execute(sql_command)
        self.oracle_connection.commit()

        print('====test====')

        return "success"
    
    def edit(self,payloads,query):

        sql_command = """
            UPDATE BMA_PHASE_II.USERS SET {}
            WHERE ID = {}
        """.format(query,payloads['id']
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        self.oracle_connection.commit()
        return "success"

    def delete(self,payloads):

        sql_command = """
            DELETE FROM BMA_PHASE_II.USERS
            WHERE ID = {}
        """.format(payloads['id']
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        self.oracle_connection.commit()
        return "delete success"

    def get_department(self):
        sql_command = """
            SELECT ID,NAME FROM BMA_PHASE_II.DEPARTMENTS d ORDER BY ID
        """
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)        
        data = cursor.fetchall()

        try:
            columes = [row[0] for row in cursor.description]
            df = pd.DataFrame(data=data, columns=columes)
            df = df.rename(columns={
                'ID': 'id',
                'NAME': 'department_name',
            })

            result = df.to_dict('records')
            data = result

        except:
            response = {
                'status_code': 404,
                'message': self.not_found_msg
            }

            raise NotFound(response)
        
        return data

    def get_user_level(self):
        sql_command = """
            SELECT ID,NAME FROM BMA_PHASE_II.USER_LEVELS ul ORDER BY ID
        """
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)        
        data = cursor.fetchall()

        try:
            columes = [row[0] for row in cursor.description]
            df = pd.DataFrame(data=data, columns=columes)
            df = df.rename(columns={
                'ID': 'id',
                'NAME': 'level_name',
            })

            result = df.to_dict('records')
            data = result

        except:
            response = {
                'status_code': 404,
                'message': self.not_found_msg
            }

            raise NotFound(response)
        
        return data

    def insert_group(self,payloads):
        
        sql_command = """
            INSERT INTO BMA_PHASE_II.GROUPS (NAME, DEPARTMENT_ID, USER_LEVEL_ID)
            VALUES ('{}', {}, {})
        """.format(payloads['name'],payloads['department_id'],payloads['user_level_id']
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        self.oracle_connection.commit()

        return "success"

    def edit_group(self,payloads,query):

        sql_command = """
            UPDATE BMA_PHASE_II.GROUPS SET {}
            WHERE ID = {}
        """.format(query,payloads['id']
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        self.oracle_connection.commit()
        return "success"

    def delete_group(self,id):

        sql_command = """
            DELETE FROM BMA_PHASE_II.GROUPS
            WHERE ID = {}
        """.format(id
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        self.oracle_connection.commit()
        return "delete success"

    def check_exist_group(self,payloads):

        sql_command = """
            SELECT COUNT(*) FROM (SELECT * FROM BMA_PHASE_II.USERS
                WHERE GROUP_ID = {})
        """.format(payloads['id']
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        return data[0][0]

    def insert_user_level(self,payloads):
        
        sql_command = """
            INSERT INTO BMA_PHASE_II.USER_LEVELS (NAME)
            VALUES ('{}')
        """.format(payloads['name']
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        self.oracle_connection.commit()

        return "success"
    
    def get_user_level_id_by_name(self,payloads):

        sql_command = """
            SELECT ID FROM BMA_PHASE_II.USER_LEVELS
                WHERE NAME = '{}'
        """.format(payloads['name']
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        
        return data[0][0]