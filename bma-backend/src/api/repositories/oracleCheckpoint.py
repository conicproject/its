from api.connections.oracle import OracleConnection
from rest_framework.exceptions import NotFound

import pandas as pd


class OracleCheckpointRepository:
    
    def __init__(self):
        self.oracle_connection = OracleConnection().get_connection()

        self.not_found_msg = 'checkpoint not found'


    def get_by_id(self, id):
        sql_command = """
            SELECT CHECKPOINT_ID, CHECKPOINT_NAMETH, CHECKPOINT_NICKNAME  FROM CHECKPOINT c 
            WHERE CHECKPOINT_CODE IS NOT NULL AND PROJECT_ID = 2
                AND AREA_CODE IS NOT NULL
                and CHECKPOINT_ID = '{}'
        """.format(id)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        try:
            columes = [row[0] for row in cursor.description]
            df = pd.DataFrame(data=data, columns=columes)
            df = df.rename(columns={
                'CHECKPOINT_ID': 'id',
                'CHECKPOINT_NAMETH': 'name',
                'CHECKPOINT_NICKNAME': 'short_name'
            })

            result = df.to_dict('records')
            result = result[0]

        except:
            result = {
                'id': "0",
                'name': "-",
                'short_name': "-",
            }
            # response = {
            #     'status_code': 400,
            #     'message':  self.not_found_msg
            # }

            # raise NotFound(response)

        return result
    

    def get_area_code_by_id(self, id):
        sql_command = """
            SELECT CHECKPOINT_ID, AREA_CODE  FROM CHECKPOINT c
            WHERE CHECKPOINT_ID = '{}' AND PROJECT_ID = 2
                AND AREA_CODE IS NOT NULL
            ORDER BY LPAD(CHECKPOINT_ID, (SELECT MAX(LENGTH(CHECKPOINT_ID)) FROM CHECKPOINT))
        """.format(id)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        try:
            columes = [row[0] for row in cursor.description]
            df = pd.DataFrame(data=data, columns=columes)
            df = df.rename(columns={
                'CHECKPOINT_ID': 'id',
                'AREA_CODE': 'area_code'
            })

            result = df.to_dict('records')
            area_code = result[0]['area_code']

        except:
            response = {
                'status_code': 400,
                'message':  self.not_found_msg
            }

            raise NotFound(response)

        return area_code



    def get_all_active(self):
        sql_command = """
            SELECT CHECKPOINT_ID, CHECKPOINT_NAMETH, CHECKPOINT_NICKNAME, CHECKPOINT_PROJECT_NO  FROM CHECKPOINT c 
            WHERE CHECKPOINT_CODE IS NOT NULL AND PROJECT_ID = 2
                AND AREA_CODE IS NOT NULL
            ORDER BY LPAD(CHECKPOINT_PROJECT_NO, (SELECT MAX(LENGTH(CHECKPOINT_PROJECT_NO)) FROM CHECKPOINT))
        """

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'CHECKPOINT_ID': 'id',
            'CHECKPOINT_NAMETH': 'name',
            'CHECKPOINT_NICKNAME': 'short_name',
            'CHECKPOINT_PROJECT_NO': 'checkpoint_project_no'
        })
        result = df.to_dict('records')

        return result


    def get_all_active_report(self):
        sql_command = """
            SELECT c.CHECKPOINT_ID, c.CHECKPOINT_NAMETH, c.CHECKPOINT_NICKNAME, r.ROAD_NAME FROM CHECKPOINT c
            JOIN ROAD r ON r.ROAD_ID = c.ROAD_ID
            WHERE CHECKPOINT_CODE IS NOT NULL AND PROJECT_ID = 2
                AND AREA_CODE IS NOT NULL
            ORDER BY LPAD(CHECKPOINT_ID, (SELECT MAX(LENGTH(CHECKPOINT_ID)) FROM CHECKPOINT))
        """

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'CHECKPOINT_ID': 'id',
            'CHECKPOINT_NAMETH': 'name',
            'CHECKPOINT_NICKNAME': 'short_name',
            'ROAD_NAME': 'road'
        })
        result = df.to_dict('records')

        return result


    def get_all(self):
        sql_command = """
            SELECT CHECKPOINT_ID, CHECKPOINT_NAMETH, CHECKPOINT_NICKNAME, CHECKPOINT_CODE, AREA_CODE  FROM CHECKPOINT c WHERE PROJECT_ID = 2
            ORDER BY LPAD(CHECKPOINT_ID, (SELECT MAX(LENGTH(CHECKPOINT_ID)) FROM CHECKPOINT)) 
        """

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'CHECKPOINT_ID': 'id',
            'CHECKPOINT_NAMETH': 'name',
            'CHECKPOINT_NICKNAME': 'short_name'
        })

        df['is_active'] = True
        df.loc[(df['CHECKPOINT_CODE'].isnull()) | (df['AREA_CODE'].isnull()), 'is_active'] = False
        df = df.drop(columns=['CHECKPOINT_CODE', 'AREA_CODE'])

        result = df.to_dict('records')

        return result


    def get_all_sensor_report(self):
        sql_command = """
            SELECT CHECKPOINT_ID, CHECKPOINT_NICKNAME, CHECKPOINT_CODE, AREA_CODE  FROM CHECKPOINT c WHERE PROJECT_ID = 2
            ORDER BY LPAD(CHECKPOINT_ID, (SELECT MAX(LENGTH(CHECKPOINT_ID)) FROM CHECKPOINT)) 
        """

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'CHECKPOINT_ID': 'id',
            'CHECKPOINT_NICKNAME': 'name'
        })

        return df


    def get_all_traffic_view(self):
        sql_command = """
            SELECT CHECKPOINT_ID, CHECKPOINT_NAMETH, CHECKPOINT_NICKNAME, LATITUDE, LONGTITUDE, CHECKPOINT_CODE, AREA_CODE, CHECKPOINT_PROJECT_NO FROM CHECKPOINT WHERE PROJECT_ID = 2
            ORDER BY LPAD(CHECKPOINT_PROJECT_NO, (SELECT MAX(LENGTH(CHECKPOINT_PROJECT_NO)) FROM CHECKPOINT))
        """

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'CHECKPOINT_ID': 'id',
            'CHECKPOINT_NAMETH': 'name',
            'CHECKPOINT_NICKNAME': 'short_name',
            'LATITUDE': 'latitude',
            'LONGTITUDE': 'longtitude',
            'CHECKPOINT_PROJECT_NO':'checkpoint_project_no'
        })

        df['is_active'] = True
        df.loc[(df['CHECKPOINT_CODE'].isnull()) | (df['AREA_CODE'].isnull()), 'is_active'] = False
        df = df.drop(columns=['CHECKPOINT_CODE', 'AREA_CODE'])

        result = df.to_dict('records')

        return result


    def get_count_all(self):
        sql_command = """
            SELECT count(*) AS total FROM CHECKPOINT WHERE PROJECT_ID = 2
        """
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        total = data[0][0]

        return total


    def get_list_checkpoints(self):
        sql_command = """
            SELECT * FROM CHECKPOINT
        """
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'CHECKPOINT_ID': 'checkpoint_id',
            'CHECKPOINT_CODE': 'checkpoint_code',
            'CHECKPOINT_NAME':'checkpoint_name',
            'SPEEDLIMIT':'speedlimit',
            'LATITUDE': 'latitude',
            'LONGTITUDE': 'longtitude',
            'ROAD_ID':'road_id',
            'DISTRICT_ID':'district_id',
            'ROAD_CONDITION_ID':'road_condition_id',
            'CHECKPOINT_NAMETH': 'checkpoint_nameth',
            'CHECKPOINT_NICKNAME': 'checkpoint_nickname',
            'AREA_CODE':'area_code',
            'PROJECT_ID':'project_id'
        })
        
        result = df.to_dict('records')

        return result

    def get_district(self):
        sql_command = """
            SELECT DISTRICT_ID,DISTRICT_NAME FROM DISTRICT
        """
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)        
        data = cursor.fetchall()

        try:
            columes = [row[0] for row in cursor.description]
            df = pd.DataFrame(data=data, columns=columes)
            df = df.rename(columns={
                'DISTRICT_ID': 'id',
                'DISTRICT_NAME': 'name'
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

    def get_road(self):
        sql_command = """
            SELECT ROAD_ID,ROAD_NAME FROM ROAD
        """
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)        
        data = cursor.fetchall()

        try:
            columes = [row[0] for row in cursor.description]
            df = pd.DataFrame(data=data, columns=columes)
            df = df.rename(columns={
                'ROAD_ID': 'id',
                'ROAD_NAME': 'name'
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
    
    def check_dup_checkpoint(self,payloads):

        sql_command = """
            SELECT COUNT(*) FROM (SELECT * FROM CHECKPOINT
                WHERE CHECKPOINT_ID = '{}')
        """.format(payloads['checkpoint_id']
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        return data[0][0]
    
    def insert_checkpoint(self,payloads):
        
        sql_command = """
            INSERT INTO CHECKPOINT (CHECKPOINT_ID, CHECKPOINT_CODE, CHECKPOINT_NAME,SPEEDLIMIT,LATITUDE,LONGTITUDE,ROAD_ID,DISTRICT_ID,
            ROAD_CONDITION_ID,CHECKPOINT_NAMETH,CHECKPOINT_NICKNAME,AREA_CODE,PROJECT_ID)
            VALUES ('{}','{}','{}',{},'{}','{}','{}','{}','{}','{}','{}','{}',{})
        """.format(payloads['checkpoint_id'],payloads['checkpoint_code'],payloads['checkpoint_name'],
            payloads['speedlimit'],payloads['latitude'],payloads['longtitude'],
            payloads['road_id'],payloads['district_id'],payloads['road_condition_id'],
            payloads['checkpoint_nameth'],payloads['checkpoint_nickname'],payloads['area_code'],
            payloads['project_id']
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        self.oracle_connection.commit()

        return "success"

    def edit_checkpoint(self,payloads,query):

        sql_command = """
            UPDATE CHECKPOINT SET {}
            WHERE CHECKPOINT_ID = '{}'
        """.format(query,payloads['checkpoint_id']
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        self.oracle_connection.commit()
        return "success"

    def get_road(self):
        sql_command = """
            SELECT * FROM ROAD r 
        """
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)        
        data = cursor.fetchall()

        try:
            columes = [col[0].lower() for col in cursor.description]
            df = pd.DataFrame(data=data, columns=columes)
            

            result = df.to_dict('records')
            data = result

        except:
            response = {
                'status_code': 404,
                'message': self.not_found_msg
            }

            raise NotFound(response)
        
        return data

    def get_lane(self):
        sql_command = """
            SELECT * FROM LANE l 
        """
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)        
        data = cursor.fetchall()

        try:
            columes = [col[0].lower() for col in cursor.description]
            df = pd.DataFrame(data=data, columns=columes)
            

            result = df.to_dict('records')
            data = result

        except:
            response = {
                'status_code': 404,
                'message': self.not_found_msg
            }

            raise NotFound(response)
        
        return data

    def check_dup_road(self,payloads):

        sql_command = """
            SELECT COUNT(*) FROM (SELECT * FROM ROAD
                WHERE ROAD_ID = '{}')
        """.format(payloads['road_id']
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        return data[0][0]

    def insert_road(self,payloads):
        sql_command = """
            INSERT INTO ROAD (ROAD_ID, ROAD_CODE, FROM_SECTION,TO_SECTION,ROAD_NAME)
            VALUES ('{}','{}','{}','{}','{}')
        """.format(payloads['road_id'],payloads['road_code'],payloads['from_section'],
            payloads['to_section'],payloads['road_name']
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        self.oracle_connection.commit()

        return "success"

    def edit_road(self,payloads,query):

        sql_command = """
            UPDATE ROAD SET {}
            WHERE ROAD_ID = '{}'
        """.format(query,payloads['road_id']
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        self.oracle_connection.commit()
        return "success"

    def check_dup_lane(self,payloads):

        sql_command = """
            SELECT COUNT(*) FROM (SELECT * FROM LANE
                WHERE LANE_ID = '{}')
        """.format(payloads['lane_id']
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        return data[0][0]

    def insert_lane(self,payloads):
        sql_command = """
            INSERT INTO LANE (LANE_ID, LANE_CODE, LANE_NAME ,ROAD_DIRECTION,ROAD_ID,CAMERA_ID,CHECKPOINT_ID)
            VALUES ('{}','{}','{}','{}','{}','{}','{}')
        """.format(payloads['lane_id'],payloads['lane_code'],payloads['lane_name'],
            payloads['road_direction'],payloads['road_id'],payloads['camera_id'],
            payloads['checkpoint_id']
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        self.oracle_connection.commit()

        return "success"

    def edit_lane(self,payloads,query):

        sql_command = """
            UPDATE LANE SET {}
            WHERE LANE_ID = '{}'
        """.format(query,payloads['lane_id']
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        self.oracle_connection.commit()
        return "success"

    def get_all_list_id(self):
        sql_command = """
            SELECT CHECKPOINT_ID  FROM CHECKPOINT WHERE PROJECT_ID = 2
            ORDER BY LPAD(CHECKPOINT_ID, (SELECT MAX(LENGTH(CHECKPOINT_ID)) FROM CHECKPOINT))
        """

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        list_id = [rec[0] for rec in data]

        return list_id

    def get_ip_address(self):
        sql_command = """
            SELECT 
                CHECKPOINT_ID, CHECKPOINT_NICKNAME
                , BMA_IP, BMA_REQUEST_PORT, BMA_RESPONSE_PORT
                , NET_IP, NET_REQUEST_PORT, NET_RESPONSE_PORT
            	FROM CHECKPOINT c 
            	WHERE c.PROJECT_ID = 2
            		AND CHECKPOINT_ID > 27 
            	ORDER BY LPAD(CHECKPOINT_ID, (SELECT MAX(LENGTH(CHECKPOINT_ID)) FROM CHECKPOINT)) 
        """

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)

        result = df.to_dict('records')

        return result

    def get_record_url(self):
        sql_command="""
            SELECT c.CHECKPOINT_ID , CHECKPOINT_NICKNAME , PROJECT_ID  ,TERMINAL FROM CHECKPOINT 
            JOIN CAMERA c ON c.CHECKPOINT_ID = CHECKPOINT.CHECKPOINT_ID 
            """
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        df = pd.DataFrame(data, columns=['CHECKPOINT_ID', 'CHECKPOINT_NICKNAME', 'PROJECT_ID', 'TERMINAL'])
        df['Camera_number'] = df.groupby(['CHECKPOINT_ID', 'TERMINAL']).cumcount() + 1
        result_dict = df.to_dict(orient='records')


        return result_dict