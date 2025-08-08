from api.connections.oracle import OracleConnection

import pandas as pd

class userLevel:
    
    def __init__(self):
        
        self.oracle_connection = OracleConnection().get_connection()
        
    def get_list_user_level(self):
        
        sql_command = """
            SELECT * FROM BMA_PHASE_II.USER_LEVELS
        """
        
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        
        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'ID': 'id',
            'NAME': 'name'
        })

        result = df.to_dict('records')

        return result

    def get_user_level_permission(self):
        
        sql_command = """
            SELECT ul.*,p.MENU_ID  FROM BMA_PHASE_II.USER_LEVELS ul 
            JOIN BMA_PHASE_II.PERMISSIONS p
                ON ul.ID = p.USER_LEVEL_ID 
        """
        
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        
        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'ID': 'id',
            'NAME': 'name',
            'DETAIL':'detail',
            'MENU_ID':'menu_id'
        })

        result = df.to_dict('records')

        return result
    
    def insert_user_level_permission(self,query):
        sql_command = query
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        self.oracle_connection.commit()
        return 'success'
    
    def query_string_user_level_permission(self,id,payloads):
        if payloads['menu'] != '':
            insert_sql_command = "INSERT INTO BMA_PHASE_II.PERMISSIONS (user_level_id, menu_id) SELECT * FROM ( "
            for i in payloads['menu']:
                insert_data = """SELECT {} as user_level_id, {} as menu_id FROM DUAL UNION ALL """.format(
                            id, i
                        )
                insert_sql_command += insert_data
            
            
            insert_sql_command = insert_sql_command[:-11]
            insert_endline_command = ')'
            insert_sql_command += insert_endline_command
            return insert_sql_command
        else:
            insert_sql_command = ''
            return insert_sql_command

    def update_user_level_permission(self,payloads):
        sql_command = """
                DELETE FROM BMA_PHASE_II.PERMISSIONS
                WHERE USER_LEVEL_ID = {}
            """.format(payloads['id']
            )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        self.oracle_connection.commit()
        
        if payloads['menu'] != []:
            for i in payloads['menu']:
                sql_command = """INSERT INTO BMA_PHASE_II.PERMISSIONS (USER_LEVEL_ID, MENU_ID)
                    VALUES ({},{})
                """.format(payloads['id'],i
                )
                cursor = self.oracle_connection.cursor()
                cursor.execute(sql_command)
                self.oracle_connection.commit()
              
        return 'success'

    def exist_user_level_permission(self,payloads):

        sql_command = """
            SELECT COUNT(*) FROM (SELECT * FROM BMA_PHASE_II.PERMISSIONS
                WHERE USER_LEVEL_ID = {})
        """.format(payloads['id']
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        return data[0][0]

    def exist_user_level_group(self,payloads):

        sql_command = """
            SELECT COUNT(*) FROM (SELECT * FROM BMA_PHASE_II.GROUPS
                WHERE USER_LEVEL_ID = {})
        """.format(payloads['id']
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        return data[0][0]

    def delete_user_level(self,id):

        sql_command = """
            DELETE FROM BMA_PHASE_II.USER_LEVELS
            WHERE ID = {}
        """.format(id
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        self.oracle_connection.commit()
        return "delete success"
    
    def edit_user_level_name(self,payloads):
        sql_command = """
            UPDATE BMA_PHASE_II.USER_LEVELS SET NAME = '{}'
            WHERE ID = {}
        """.format(payloads['name'],payloads['id']
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        self.oracle_connection.commit()
        return "success"
