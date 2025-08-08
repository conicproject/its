from api.connections.oracle import OracleConnection
from rest_framework.exceptions import NotFound
from api.repositories.oracleVehicleType import OracleVehicleTypeRepository
from api.repositories.oracleCheckpoint import OracleCheckpointRepository

import pandas as pd
import datetime

class OracleManualInsertRepository:
    
    def __init__(self):
        self.oracle_connection = OracleConnection().get_connection()
        self.vehicle_type_repo = OracleVehicleTypeRepository()
        self.checkpoint_repo = OracleCheckpointRepository()
        self.time_stamp_format = '%Y-%m-%d %H:%M:%S'

    def to_dataframe(self, columes, data):
        df = pd.DataFrame(
            columns=columes,
            data=data
        )

        return df


    def get_config(self):
        vehicle_type_list_id = self.vehicle_type_repo.get_all_list_id()
        checkpoint_list_id = self.checkpoint_repo.get_all_list_id()
        list_direction = [
            {
                'raw': 'inbound',
                'insert': 'IN'
            },
            {
                'raw': 'outbound',
                'insert': 'OUT'
            }
        ]

        return vehicle_type_list_id, checkpoint_list_id, list_direction


    def get_volume(self, df, checkpoint_id, type_id, direction):
        try:
            volume = df[
                (df['CHECKPOINT_ID'] == checkpoint_id) &
                (df['CAR_TYPE_ID'] == type_id) &
                (df['DIRECTION'] == direction['raw'])
            ]['VOLUME'].values[0]
        except:
            volume = 0

        return volume
    

    def get_created_at(self):
        now = datetime.datetime.now()
        created_at = now.strftime(self.time_stamp_format)

        return created_at

    def get_by_timeStamp_routine(self, start_timestamp: str, end_timestamp: str):
        sql_command = """
            SELECT ch.CHECKPOINT_ID AS checkpoint_id, la.ROAD_DIRECTION AS direction, vt.TYPE_ID AS car_type_id, count(*) AS volume
            FROM XVOT_XVOTDB_USER.VEHICLE_PASS vp
            JOIN CHECKPOINT ch 
                ON ch.AREA_CODE=vp.AREA_CODE AND ch.PROJECT_ID = 2
            JOIN VEHICLE_TYPE vt
                ON vt.TYPE_NAME=vp.VEHICLE_TYPE
            JOIN LANE la
                ON la.CHECKPOINT_ID=ch.CHECKPOINT_ID
                AND la.LANE_CODE =vp.LANE_NO 
            WHERE vp.PASS_TIME >= TO_TIMESTAMP('{}', 'YYYY-MM-DD hh24:mi:ss')
                AND vp.PASS_TIME < TO_TIMESTAMP('{}', 'YYYY-MM-DD hh24:mi:ss')
            GROUP BY ch.CHECKPOINT_ID, la.ROAD_DIRECTION ,vt.TYPE_ID
            ORDER BY ch.CHECKPOINT_ID, vt.TYPE_ID
        """.format(start_timestamp, end_timestamp)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)      
        data = cursor.fetchall()

        result = {
            'columes': [row[0] for row in cursor.description],
            'data': data
        }

        return result

    def get_by_timeStamp_violation_routine(self, start_timestamp: str, end_timestamp: str):
        sql_command = """
            SELECT ch.CHECKPOINT_ID AS checkpoint_id, la.ROAD_DIRECTION AS direction, vt.TYPE_ID AS car_type_id, count(*) AS volume
            FROM XVOT_XVOTDB_USER.VEHICLE_ALARM va
            JOIN CHECKPOINT ch 
                ON ch.AREA_CODE=va.AREA_CODE AND ch.PROJECT_ID = 2
            JOIN VEHICLE_TYPE vt
                ON vt.TYPE_NAME=va.VEHICLE_TYPE
            JOIN LANE la
                ON la.CHECKPOINT_ID=ch.CHECKPOINT_ID
                AND la.LANE_CODE =va.LANE_NO 
            WHERE va.PASS_TIME >= TO_TIMESTAMP('{}', 'YYYY-MM-DD hh24:mi:ss')
                AND va.PASS_TIME < TO_TIMESTAMP('{}', 'YYYY-MM-DD hh24:mi:ss')
                AND va.VIOLATIVE_ACTION = '1625'
            GROUP BY ch.CHECKPOINT_ID, la.ROAD_DIRECTION ,vt.TYPE_ID
            ORDER BY ch.CHECKPOINT_ID, vt.TYPE_ID
        """.format(start_timestamp, end_timestamp)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)      
        data = cursor.fetchall()

        result = {
            'columes': [row[0] for row in cursor.description],
            'data': data
        }

        return result

    def get_time_range_by_end_time(self, time: str):
        sql_command = 'select * from BMA_PHASE_II.time_ranges where "END_TIME" = ' + "'" + time + "'"

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)      
        result = cursor.fetchone()

        return result

    def get_insert_manual_command(self, data, columes, date, time_range_id):
        insert_sql_command = "INSERT INTO BMA_PHASE_II.RECORDS (direction, checkpoint_id, time_range_id, car_type_id ,volume, created_date, created_at) SELECT * FROM ( "
        # insert_sql_command = """
        #     INSERT INTO BMA_PHASE_II.records (direction, checkpoint_id, time_range_id, car_type_id ,volume, "date", created_at) values 
        # """
        vehicle_type_list_id, checkpoint_list_id, list_direction = self.get_config()
        df_raw_data = self.to_dataframe(
            data=data, columes=columes
        )

        for direction in list_direction:
            for checkpoint_id in checkpoint_list_id:
                for type_id in vehicle_type_list_id:

                    volume = self.get_volume(
                        df=df_raw_data, checkpoint_id=checkpoint_id,
                        type_id=type_id, direction=direction
                    )

                    created_at = self.get_created_at()
                    insert_data = """SELECT '{}'as direction, {} as checkpoint_id, {} as time_range_id, {} as car_type_id, {} as volume, TO_DATE('{}','YYYY-MM-DD') as created_date, TO_DATE('{}','YYYY-MM-DD hh24:mi:ss') as created_at FROM DUAL UNION ALL """.format(
                        direction['insert'], checkpoint_id, time_range_id, 
                        type_id, volume, date, created_at
                    )
                    # insert_data = "('{}', {}, {}, {}, {}, '{}', '{}'),".format(
                    #     direction['insert'], checkpoint_id, time_range_id, 
                    #     type_id, volume, date, created_at
                    # )
                    insert_sql_command += insert_data
                    # print(created_at)
        
        
        insert_sql_command = insert_sql_command[:-11]
        insert_endline_command = ')'
        insert_sql_command += insert_endline_command

        return insert_sql_command

    def get_insert_violation_manual_command(self, data, columes, date, time_range_id):
        insert_sql_command = "INSERT INTO BMA_PHASE_II.VIOLATION_RECORDS (direction, checkpoint_id, time_range_id, car_type_id ,volume, created_date, created_at) "
        vehicle_type_list_id, checkpoint_list_id, list_direction = self.get_config()
        df_raw_data = self.to_dataframe(
            data=data, columes=columes
        )

        for direction in list_direction:
            for checkpoint_id in checkpoint_list_id:
                for type_id in vehicle_type_list_id:

                    volume = self.get_volume(
                        df=df_raw_data, checkpoint_id=checkpoint_id,
                        type_id=type_id, direction=direction
                    )

                    created_at = self.get_created_at()
                    insert_data = """SELECT '{}'as direction, {} as checkpoint_id, {} as time_range_id, {} as car_type_id, {} as volume, TO_DATE('{}','YYYY-MM-DD') as created_date, TO_DATE('{}','YYYY-MM-DD hh24:mi:ss') as created_at FROM DUAL UNION ALL """.format(
                        direction['insert'], checkpoint_id, time_range_id, 
                        type_id, volume, date, created_at
                    )
                  
                    insert_sql_command += insert_data
        
        insert_sql_command = insert_sql_command[:-11]

        return insert_sql_command

    def delete_record(self,startdate,enddate):
        sql_command = """
                DELETE FROM BMA_PHASE_II.RECORDS
                WHERE CREATED_DATE >= TO_DATE('{}', 'YYYY-MM-DD') AND CREATED_DATE < TO_DATE('{}', 'YYYY-MM-DD')
            """.format(startdate,enddate
            )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        self.oracle_connection.commit()
        return 'del success'

    def delete_violation(self,startdate,enddate):
        sql_command = """
                DELETE FROM BMA_PHASE_II.VIOLATION_RECORDS
                WHERE CREATED_DATE >= TO_DATE('{}', 'YYYY-MM-DD') AND CREATED_DATE < TO_DATE('{}', 'YYYY-MM-DD')
            """.format(startdate,enddate
            )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        self.oracle_connection.commit()
        return 'del success'