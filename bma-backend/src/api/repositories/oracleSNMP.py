from api.connections.oracle import OracleConnection

import pandas as pd


class OracleSNMPRepository:

    def __init__(self):
        self.oracle_connection = OracleConnection().get_connection()

    def get_dataframe_all_config(self):
        sql_command = """
            SELECT s.PRTG_ID, s."TYPE" FROM snmp s WHERE s.PROJECT_ID = 2
        """

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'PRTG_ID': 'id',
            'TYPE': 'type'
        })

        result = df

        return result


    def get_dataframe_by_checkpoint(self, checkpoint_id):
        sql_command = """
            SELECT s.PRTG_ID, s."TYPE"  FROM snmp s
            WHERE s.CHECKPOINT_ID = '{}' AND s.PROJECT_ID = 2
        """.format(checkpoint_id)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'PRTG_ID': 'id',
            'TYPE': 'type'
        })

        result = df

        return result


    def get_dataframe_server(self):
        sql_command = """
            SELECT PRTG_ID, "TYPE" FROM snmp
            WHERE "TYPE" = 'server' AND PROJECT_ID = 2
        """

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'PRTG_ID': 'id',
            'TYPE': 'type'
        })

        result = df

        return result


    def get_dataframe_all_sensor_report(self):
        sql_command = """
            SELECT s.PRTG_ID, s.CHECKPOINT_ID  FROM snmp s WHERE s.PROJECT_ID = 2
        """

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'PRTG_ID': 'id',
            'CHECKPOINT_ID': 'checkpoint'
        })

        result = df

        return result


    def get_dataframe_all_sensor_report_by_checkpoint(self, checkpoint_id):
        sql_command = """
            SELECT s.PRTG_ID, s.CHECKPOINT_ID  FROM snmp s 
            WHERE s.CHECKPOINT_ID = '{}' AND s.PROJECT_ID = 2
        """.format(checkpoint_id)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'PRTG_ID': 'id',
            'CHECKPOINT_ID': 'checkpoint'
        })

        result = df

        return result

    def get_all(self):
        sql_command = """
            SELECT PRTG_ID, TYPE, CHECKPOINT_NICKNAME, 'Device' AS TEXT, 'storage' AS ICON, IP FROM snmp s
            LEFT JOIN (SELECT CHECKPOINT_ID, CHECKPOINT_NICKNAME FROM CHECKPOINT WHERE CHECKPOINT_ID >= 28) ch 
                ON ch.CHECKPOINT_ID=s.CHECKPOINT_ID 
            WHERE PROJECT_ID = 2
        """

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'PRTG_ID': 'id',
            'TYPE': 'type',
            'CHECKPOINT_NICKNAME': 'checkpoint',
            'TEXT':'text',
            'ICON':'icon',
            'IP':'ip',
        })

        result = df.to_dict('records')

        return result

