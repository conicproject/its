from api.connections.oracle import OracleConnection
from rest_framework.exceptions import NotFound

import pandas as pd

class OracleCameraRepository:
    
    def __init__(self):
        self.oracle_connection = OracleConnection().get_connection()

        self.not_found_msg = 'checkpoint not available'
        self.not_found_checkpoint_camera_msg = 'camera not available'


    def get_by_id(self, id):
        sql_command = """
            SELECT c.CAMERA_ID, c.BMA_CODE,c.TYPE,c.CAMERA_CODE,c.HLS FROM CAMERA c JOIN CHECKPOINT c2 ON c.CHECKPOINT_ID = c2.CHECKPOINT_ID 
            WHERE c.CHECKPOINT_ID = '{}' AND c2.PROJECT_ID = 2
                AND c.CAMERA_CODE IS NOT NULL 
        """.format(id)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        try:
            columes = [row[0] for row in cursor.description]
            df = pd.DataFrame(data=data, columns=columes)
            df = df.rename(columns={
                'CAMERA_ID': 'id',
                'BMA_CODE': 'code',
                'TYPE':'type',
                'HLS' : 'url'
            })

            result = df.to_dict('records')

        except:
            response = {
                'status_code': 400,
                'message':  self.not_found_msg
            }

            raise NotFound(response)

        return result


    def get_sample_camera(self, id):
        sql_command = """
            SELECT c.CAMERA_CODE FROM CAMERA c JOIN CHECKPOINT c2 ON c.CHECKPOINT_ID = c2.CHECKPOINT_ID 
            WHERE c.CHECKPOINT_ID = '{}'
                 AND c2.PROJECT_ID = 2
        """.format(id)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        try:
            columes = [row[0] for row in cursor.description]
            df = pd.DataFrame(data=data, columns=columes)
            df = df.rename(columns={
                'CAMERA_CODE': 'code'
            })

            result = df.to_dict('records')

        except:
            response = {
                'status_code': 400,
                'message':  self.not_found_msg
            }

            raise NotFound(response)

        return result


    def get_checkpoint_camera(self, id, camera_code):
        sql_command = """
            SELECT c.CAMERA_ID, c.CAMERA_CODE FROM CAMERA c JOIN CHECKPOINT c2 ON c.CHECKPOINT_ID = c2.CHECKPOINT_ID 
            WHERE c.CHECKPOINT_ID = '{}'
                AND c.BMA_CODE = '{}' AND c2.PROJECT_ID = 2
        """.format(id, camera_code)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        try:
            columes = [row[0] for row in cursor.description]
            df = pd.DataFrame(data=data, columns=columes)
            df = df.rename(columns={
                'CAMERA_ID': 'id',
                'CAMERA_CODE': 'code'
            })

            result = df.to_dict('records')
            result = result[0]

        except:
            response = {
                'status_code': 400,
                'message':  self.not_found_checkpoint_camera_msg
            }

            raise NotFound(response)

        return result

    def get_count_2_phase_all(self):
        sql_command = """
            SELECT count(*) AS total FROM CAMERA c WHERE CAMERA_CODE IS NOT NULL 
        """
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        total = data[0][0]

        return total
    
    def get_all_camera_code_phase_2(self):
        sql_command = """
            SELECT c.CAMERA_CODE,c.TYPE  FROM CAMERA c JOIN CHECKPOINT c2 ON c.CHECKPOINT_ID = c2.CHECKPOINT_ID 
            WHERE c2.PROJECT_ID = 2 AND c.CAMERA_CODE IS NOT NULL 
        """
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'CAMERA_CODE': 'code',
            'TYPE':'type'
        })
        result = df.to_dict('records')
        

        return result

    def get_count_all(self):
        sql_command = """
            SELECT count(*) AS total FROM CAMERA c JOIN CHECKPOINT c2 ON c.CHECKPOINT_ID = c2.CHECKPOINT_ID 
            WHERE c2.PROJECT_ID = 2
        """
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        total = data[0][0]

        return total


    def get_count_by_checkpoint(self, checkpoint_id):
        sql_command = """
            SELECT count(*) AS total FROM CAMERA c JOIN CHECKPOINT c2 ON c.CHECKPOINT_ID = c2.CHECKPOINT_ID
            where c.CHECKPOINT_ID = '{}' AND c2.PROJECT_ID = 2
        """.format(checkpoint_id)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        total = data[0][0]

        return total


    def get_all_sensor_report(self):
        sql_command = """
            SELECT c.CAMERA_CODE , c.IP, c.BMA_CODE, ch.CHECKPOINT_NICKNAME FROM CAMERA c
            JOIN CHECKPOINT ch ON ch.CHECKPOINT_ID=c.CHECKPOINT_ID AND ch.PROJECT_ID = 2
        """
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'IP': 'ip',
            'CAMERA_CODE': 'code',
            'BMA_CODE': 'name',
            'CHECKPOINT_NICKNAME': 'checkpoint'
        })

        return df


    def get_all_sensor_report_by_checkpoint(self, checkpoint_id):
        sql_command = """
            SELECT c.CAMERA_CODE , c.IP, c.BMA_CODE, ch.CHECKPOINT_NICKNAME FROM CAMERA c
            JOIN CHECKPOINT ch ON ch.CHECKPOINT_ID=c.CHECKPOINT_ID AND ch.PROJECT_ID = 2 
            WHERE ch.CHECKPOINT_ID = '{}'
        """.format(checkpoint_id)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'IP': 'ip',
            'CAMERA_CODE': 'code',
            'BMA_CODE': 'name',
            'CHECKPOINT_NICKNAME': 'checkpoint'
        })

        return df

    def get_by_checkpoint(self, checkpoint_id):
        sql_command = """
            SELECT c.CAMERA_ID, c.CAMERA_CODE, c.BMA_CODE, ch.CHECKPOINT_ID, c.HLS FROM CAMERA c
            JOIN CHECKPOINT ch 
            ON ch.CHECKPOINT_ID=c.CHECKPOINT_ID AND ch.PROJECT_ID = 2 AND ch.CHECKPOINT_ID >= 28
            WHERE ch.CHECKPOINT_ID = '{}'
        """.format(checkpoint_id)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        result = pd.DataFrame(data=data, columns=columes)

        # return result
        df = df.rename(columns={
            'CAMERA_ID': 'camera_id',
            'CHECKPOINT_ID': 'checkpoint_id',
            'CAMERA_CODE': 'code',
            'BMA_CODE': 'name',
            'HLS': 'url'
        })

        result = df.to_dict('records')

        return result

    def get_sample_camera_id(self, id):
        sql_command = """
            SELECT CAMERA_CODE FROM CAMERA
            WHERE CAMERA_ID = {}
        """.format(id)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        try:
            columes = [row[0] for row in cursor.description]
            df = pd.DataFrame(data=data, columns=columes)
            df = df.rename(columns={
                'CAMERA_CODE': 'code'
            })

            result = df.to_dict('records')

        except:
            response = {
                'status_code': 400,
                'message':  self.not_found_msg
            }

            raise NotFound(response)

        return result

    def get_all(self):
        sql_command = """
            SELECT c.CHECKPOINT_ID, CAMERA_CODE, 'Camera' AS TEXT, 'videocam' AS ICON, CHECKPOINT_NICKNAME, CAMERA_NAME FROM CAMERA c
            LEFT JOIN (SELECT CHECKPOINT_ID, CHECKPOINT_NICKNAME, PROJECT_ID FROM CHECKPOINT WHERE PROJECT_ID = 2) ch 
                ON ch.CHECKPOINT_ID=c.CHECKPOINT_ID 
            WHERE c.CAMERA_CODE IS NOT NULL AND ch.PROJECT_ID = 2 
        """

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        try:
            columes = [row[0] for row in cursor.description]
            df = pd.DataFrame(data=data, columns=columes)
            df = df.rename(columns={
                'CAMERA_CODE': 'code',
                'CHECKPOINT_NICKNAME': 'checkpoint',
                'TEXT':'text',
                'ICON':'icon',
                'CAMERA_NAME': 'name',
                'CHECKPOINT_ID': 'checkpoint_id',
            })

            result = df.to_dict('records')

            # result = df['CAMERA_CODE']

        except:
            response = {
                'status_code': 400,
                'message':  self.not_found_msg
            }

            raise NotFound(response)

        return result

    def get_list_cameras(self):
        sql_command = """
            SELECT * FROM CAMERA
        """
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'CAMERA_ID': 'camera_id',
            'CAMERA_CODE': 'camera_code',
            'CAMERA_NAME':'camera_name',
            'MODEL':'model',
            'IP': 'ip',
            'CHECKPOINT_ID': 'checkpoint_id',
            'SERIAL':'serial',
            'BRAND':'brand',
            'BMA_CODE':'bma_code',
            'IS_SAMPLE': 'is_sample',
            'HLS': 'hls',
            'TYPE':'type'
        })
        
        result = df.to_dict('records')

        return result

    def get_checkpoints(self):
        sql_command = """
            SELECT CHECKPOINT_ID,CHECKPOINT_NICKNAME FROM CHECKPOINT
        """
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)        
        data = cursor.fetchall()

        try:
            columes = [row[0] for row in cursor.description]
            df = pd.DataFrame(data=data, columns=columes)
            df = df.rename(columns={
                'CHECKPOINT_ID': 'id',
                'CHECKPOINT_NICKNAME': 'name'
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

    def check_dup_camera(self,payloads):

        sql_command = """
            SELECT COUNT(*) FROM (SELECT * FROM CAMERA
                WHERE CAMERA_ID = '{}')
        """.format(payloads['camera_id']
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        return data[0][0]

    def insert_camera(self,payloads):
        
        sql_command = """
            INSERT INTO CAMERA (CAMERA_ID, CAMERA_NAME, CAMERA_CODE,MODEL,IP,CHECKPOINT_ID,SERIAL,BRAND,
            BMA_CODE,IS_SAMPLE,HLS,TYPE)
            VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}',{},'{}','{}')
        """.format(payloads['camera_id'],payloads['camera_name'],payloads['camera_code'],
            payloads['model'],payloads['ip'],payloads['checkpoint_id'],
            payloads['serial'],payloads['brand'],payloads['bma_code'],
            payloads['is_sample'],payloads['hls'],payloads['type']
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        self.oracle_connection.commit()

        return "success"

    def edit_camera(self,payloads,query):

        sql_command = """
            UPDATE CAMERA SET {}
            WHERE CAMERA_ID = '{}'
        """.format(query,payloads['camera_id']
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        self.oracle_connection.commit()
        return "success"