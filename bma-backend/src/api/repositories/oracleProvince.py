from api.connections.oracle import OracleConnection

import pandas as pd

class OracleProvinceRepository:

    def __init__(self):
        self.oracle_connection = OracleConnection().get_connection()


    def get_list_name(self):
        sql_command = """
            SELECT PROVINCE_NAMETH FROM PROVINCE
        """

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'PROVINCE_NAMETH': 'name'
        })

        result = df['name'].to_list()

        return result

    def list(self):
        sql_command = """
            SELECT PROVINCE_ID, PROVINCE_NAMETH FROM PROVINCE
        """

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'PROVINCE_ID': 'value',
            'PROVINCE_NAMETH': 'name'
        })

        result = df.to_dict('record')

        return result

    def get_by_id(self, id):
        sql_command = """
            SELECT PROVINCE_ID, PROVINCE_NAMETH FROM PROVINCE
            WHERE PROVINCE_ID = '{}' 
        """.format(id)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        try:
            columes = [row[0] for row in cursor.description]
            df = pd.DataFrame(data=data, columns=columes)
            df = df.rename(columns={
                'PROVINCE_ID': 'id',
                'PROVINCE_NAMETH': 'name'
            })

            result = df.to_dict('records')
            result = result[0]

        except:
            result = {
                'id': "0",
                'name': "-",
            }

        return result