from api.connections.oracle import OracleConnection

import pandas as pd

class OracleVehicleColorRepository:

    def __init__(self):
        self.oracle_connection = OracleConnection().get_connection()


    def get_list_name(self):
        sql_command = """
            SELECT COLOR_NAMETH FROM VEHICLE_COLOR
        """

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'COLOR_NAMETH': 'name'
        })

        result = df['name'].to_list()

        return result

    def list(self):
        sql_command = """
            SELECT COLOR_NAME, COLOR_NAMETH FROM VEHICLE_COLOR
        """

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'COLOR_NAME': 'value',
            'COLOR_NAMETH': 'name'
        })

        result = df.to_dict('record')

        return result

    def get_by_name(self, name):
        sql_command = """
            SELECT COLOR_ID, COLOR_NAMETH FROM VEHICLE_COLOR
            WHERE COLOR_NAME = '{}' 
        """.format(name)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        try:
            columes = [row[0] for row in cursor.description]
            df = pd.DataFrame(data=data, columns=columes)
            df = df.rename(columns={
                'COLOR_ID': 'id',
                'COLOR_NAMETH': 'name'
            })

            result = df.to_dict('records')
            result = result[0]

        except:
            result = {
                'id': "0",
                'name': "-",
            }

        return result