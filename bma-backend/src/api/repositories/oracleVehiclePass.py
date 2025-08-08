from re import I
from unittest import result
from rest_framework.exceptions import NotFound, PermissionDenied
from api.connections.oracle import OracleConnection

import base64
import requests
import pandas as pd
import math

class OracleVehiclePassRepository:

    def __init__(self):
        self.oracle_connection = OracleConnection().get_connection()
        self.limit_rows_query = 10000

    def get_vehicle_total(self, plate_no, province, checkpoint, direction, vehicle_type, vehicle_color, start_date, end_date):

        if plate_no != '':
            # plate_no = f" AND PLATE_NO like '%{plate_no}%' "
            plate_no = f" AND REGEXP_LIKE(lower(PLATE_NO), '%{plate_no}%')  "

        if province != '':
            province = f" AND PLATE_PROVINCE = {province} "

        if checkpoint != '':
            checkpoint = f" AND ch.CHECKPOINT_ID = {checkpoint} "

        if direction != '':
            direction = f" AND ROAD_DIRECTION = '{direction}' "

        if vehicle_type != '':
            vehicle_type = f" AND VEHICLE_TYPE = '{vehicle_type}' "

        if vehicle_color != '':
            vehicle_color = f" AND VEHICLE_COLOR = '{vehicle_color}' "

        sql_command = """
            SELECT COUNT(PASS_ID) 
            FROM (
                SELECT 
                    vp.PASS_ID
                    FROM XVOT_XVOTDB_USER.VEHICLE_PASS vp
                    LEFT JOIN (
                                SELECT AREA_CODE, CHECKPOINT_ID, PROJECT_ID
                                    FROM CHECKPOINT 
                                    WHERE PROJECT_ID = 2
                                ) ch 
                                ON ch.AREA_CODE=vp.AREA_CODE 
                    LEFT JOIN (
                                SELECT LANE_CODE, CHECKPOINT_ID,ROAD_DIRECTION
                                    FROM LANE 
                                ) la
                                    ON la.CHECKPOINT_ID=ch.CHECKPOINT_ID
                                    AND la.LANE_CODE =vp.LANE_NO
                    
                    WHERE  vp.PASS_TIME >= TO_TIMESTAMP('{}', 'YYYY-MM-DD')
                        AND vp.PASS_TIME < TO_TIMESTAMP('{}', 'YYYY-MM-DD')
                        AND PROJECT_ID = 2  {} {} {} {} {} {}
            ) 
        """.format(
            start_date, end_date, checkpoint, direction,
            vehicle_color, province, vehicle_type, plate_no
        )

        print(sql_command)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        total = data[0][0]

        return total

    def get_vehicles(self, plate_no, province, checkpoint, direction, vehicle_type, vehicle_color, start_date, end_date, page_data, total, type):
        if plate_no != '':
            # plate_no = f" AND vp.PLATE_NO like '%{plate_no}%' "
            plate_no = f" AND REGEXP_LIKE(lower(vp.PLATE_NO), '{plate_no}') "

        if province != '':
            province = f" AND PLATE_PROVINCE = {province} "

        if checkpoint != '':
            checkpoint = f" AND ch.CHECKPOINT_ID = {checkpoint} "

        if direction != '':
            direction = f" AND ROAD_DIRECTION = '{direction}' "

        if vehicle_type != '':
            vehicle_type = f" AND VEHICLE_TYPE = '{vehicle_type}' "

        if vehicle_color != '':
            vehicle_color = f" AND VEHICLE_COLOR = '{vehicle_color}' "

        if type == 'violation':
            table_from = f" FROM XVOT_XVOTDB_USER.VEHICLE_ALARM vp "
        else:
            table_from = f" FROM XVOT_XVOTDB_USER.VEHICLE_PASS vp "

        sql_command = """
            SELECT *
                FROM (
                    SELECT
                        PASS_ID, ch.CHECKPOINT_ID, ROAD_DIRECTION, VEHICLE_COLOR, PLATE_PROVINCE, VEHICLE_TYPE, vp.PLATE_NO
                        , ch.CHECKPOINT_NICKNAME, ch.LATITUDE, ch.LONGTITUDE, vp.LANE_NO, vp.PASS_TIME
                        {}
                        LEFT JOIN (
                                    SELECT AREA_CODE, CHECKPOINT_ID, PROJECT_ID, LATITUDE, LONGTITUDE, CHECKPOINT_NICKNAME
                                        FROM CHECKPOINT 
                                        WHERE PROJECT_ID = 2
                                    ) ch 
                                    ON ch.AREA_CODE=vp.AREA_CODE 
                        LEFT JOIN (
                                    SELECT LANE_CODE, CHECKPOINT_ID,ROAD_DIRECTION
                                        FROM LANE 
                                    ) la
                                        ON la.CHECKPOINT_ID=ch.CHECKPOINT_ID
                                        AND la.LANE_CODE =vp.LANE_NO
                    
                    WHERE  vp.PASS_TIME >= TO_TIMESTAMP('{}', 'YYYY-MM-DD')
                        AND vp.PASS_TIME < TO_TIMESTAMP('{}', 'YYYY-MM-DD')
                        AND PROJECT_ID = 2  {} {} {} {} {} {}
                        ORDER BY vp.PASS_TIME ASC
                        OFFSET {} ROWS FETCH NEXT {} ROWS ONLY
             ) x
            LEFT JOIN VEHICLE_TYPE vt
                ON vt.TYPE_NAME=x.VEHICLE_TYPE
            LEFT JOIN VEHICLE_COLOR vc
                ON vc.COLOR_NAME=x.VEHICLE_COLOR 
            LEFT JOIN (
                SELECT PASS_ID, PLATE_PIC_URL, IMAGE_PATH
                FROM XVOT_XVOTDB_USER.VEHICLE_URL
            ) vu
                ON vu.PASS_ID=x.PASS_ID
            LEFT JOIN (
                SELECT PROVINCE_ID, PROVINCE_NAMETH
                FROM PROVINCE
            ) p
            ON p.PROVINCE_ID=x.PLATE_PROVINCE
        """.format(table_from,
            start_date, end_date, checkpoint, direction,
            vehicle_color, province, vehicle_type, plate_no,
            page_data['offset'], page_data['page_size']
        )

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'PASS_ID': 'id',
            'PLATE_PIC_URL': 'plate_picture',
            'IMAGE_PATH': 'image_url',
            'PLATE_NO': 'plate_no',
            'PROVINCE_NAMETH': 'province',
            'CHECKPOINT_NICKNAME': 'checkpoint',
            'LATITUDE': 'latitude',
            'LONGTITUDE': 'longtitude',
            'ROAD_DIRECTION': 'direction',
            'PASS_TIME': 'time',
            'TYPE_NAMETH': 'type',
            'COLOR_NAMETH': 'color'
        })

        df['base64_plate_pic'] = None

        result = df.to_dict('records')
        page_total = math.ceil(total / page_data['page_size'])

        paginate_data = {
            'page': page_data['page'],
            'page_size': page_data['page_size'],
            'page_total': page_total
        }

        return result, paginate_data

    def get_total(self, plate_no, province, checkpoint, direction, vehicle_type, vehicle_color, start_date, end_date, type):
        if plate_no != '':
            plate_no = f" AND REGEXP_LIKE(lower(vp.PLATE_NO), '{plate_no}') "


        if province != '':
            province = f" AND PLATE_PROVINCE = {province} "

        if checkpoint != '':
            checkpoint = f" AND ch.CHECKPOINT_ID = {checkpoint} "

        if direction != '':
            direction = f" AND ROAD_DIRECTION = '{direction}' "

        if vehicle_type != '':
            vehicle_type = f" AND VEHICLE_TYPE = '{vehicle_type}' "

        if vehicle_color != '':
            vehicle_color = f" AND VEHICLE_COLOR = '{vehicle_color}' "

        if type == 'violation':
            table_from = f" FROM XVOT_XVOTDB_USER.VEHICLE_ALARM vp "
        else:
            table_from = f" FROM XVOT_XVOTDB_USER.VEHICLE_PASS vp "

        sql_command = """
            SELECT COUNT(PASS_ID) 
            FROM (
                SELECT 
                    vp.PASS_ID
                    {}
                    LEFT JOIN (
                                SELECT AREA_CODE, CHECKPOINT_ID, PROJECT_ID
                                    FROM CHECKPOINT 
                                    WHERE PROJECT_ID = 2
                                ) ch 
                                ON ch.AREA_CODE=vp.AREA_CODE 
                    LEFT JOIN (
                                SELECT LANE_CODE, CHECKPOINT_ID,ROAD_DIRECTION
                                    FROM LANE 
                                ) la
                                    ON la.CHECKPOINT_ID=ch.CHECKPOINT_ID
                                    AND la.LANE_CODE =vp.LANE_NO
                    
                    WHERE  vp.PASS_TIME >= TO_TIMESTAMP('{}', 'YYYY-MM-DD')
                        AND vp.PASS_TIME < TO_TIMESTAMP('{}', 'YYYY-MM-DD')
                        AND PROJECT_ID = 2  {} {} {} {} {} {}
            ) 
        """.format(table_from,
            start_date, end_date, checkpoint, direction,
            vehicle_color, province, vehicle_type, plate_no
        )

        print(sql_command)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        total = data[0][0]

        return total
    
    def get_violation_total(self, plate_no, province, checkpoint, direction, vehicle_type, vehicle_color, start_date, end_date):
        sql_command = """
            SELECT COUNT(*) FROM (
                SELECT vp.PLATE_NO  
                FROM XVOT_XVOTDB_USER.VEHICLE_ALARM vp
                LEFT JOIN CHECKPOINT ch 
                    ON ch.AREA_CODE=vp.AREA_CODE AND ch.PROJECT_ID = 2
                LEFT JOIN VEHICLE_TYPE vt
                    ON vt.TYPE_NAME=vp.VEHICLE_TYPE
                LEFT JOIN VEHICLE_COLOR vc
                    ON vc.COLOR_NAME=vp.VEHICLE_COLOR 
                LEFT JOIN LANE la
                    ON la.CHECKPOINT_ID=ch.CHECKPOINT_ID
                    AND la.LANE_CODE =vp.LANE_NO
                LEFT JOIN PROVINCE p 
                    ON p.PROVINCE_ID=vp.PLATE_PROVINCE  
                WHERE vp.PLATE_NO like '%{}%'
                    AND p.PROVINCE_NAMETH LIKE '%{}%'
                    AND ch.CHECKPOINT_NAMETH LIKE '%{}%'
                    AND la.ROAD_DIRECTION LIKE '%{}%'
                    AND vt.TYPE_NAMETH LIKE '%{}%'
                    AND vc.COLOR_NAMETH LIKE '%{}%'
                    AND vp.PASS_TIME >= TO_TIMESTAMP('{}', 'YYYY-MM-DD')
                    AND vp.PASS_TIME < TO_TIMESTAMP('{}', 'YYYY-MM-DD')
                    AND vp.VIOLATIVE_ACTION = '1625'
                ORDER BY vp.PASS_TIME DESC
                FETCH NEXT {} ROWS ONLY
            )
        """.format(
            plate_no, province, checkpoint, direction, 
            vehicle_type, vehicle_color, start_date, end_date,
            self.limit_rows_query
        )
        # sql_command = """
        #     SELECT COUNT(*) FROM (
        #         SELECT vu.PLATE_PIC_URL, vu.IMAGE_PATH, vp.PLATE_NO, p.PROVINCE_NAMETH, ch.CHECKPOINT_NICKNAME, ch.LATITUDE, ch.LONGTITUDE, la.ROAD_DIRECTION, vp.PASS_TIME, vt.TYPE_NAMETH, vc.COLOR_NAMETH  
        #         FROM XVOT_XVOTDB_USER.VEHICLE_ALARM vp
        #         JOIN CHECKPOINT ch 
        #             ON ch.AREA_CODE=vp.AREA_CODE AND ch.PROJECT_ID = 2
        #         JOIN VEHICLE_TYPE vt
        #             ON vt.TYPE_NAME=vp.VEHICLE_TYPE
        #         JOIN VEHICLE_COLOR vc
        #             ON vc.COLOR_NAME=vp.VEHICLE_COLOR 
        #         JOIN LANE la
        #             ON la.CHECKPOINT_ID=ch.CHECKPOINT_ID
        #             AND la.LANE_CODE =vp.LANE_NO
        #         JOIN XVOT_XVOTDB_USER.VEHICLE_URL vu
        #             ON vu.PASS_ID=vp.PASS_ID
        #         JOIN PROVINCE p 
        #             ON p.PROVINCE_ID=vp.PLATE_PROVINCE  
        #         WHERE vp.PLATE_NO like '%{}%'
        #             AND p.PROVINCE_NAMETH LIKE '%{}%'
        #             AND ch.CHECKPOINT_NAMETH LIKE '%{}%'
        #             AND la.ROAD_DIRECTION LIKE '%{}%'
        #             AND vt.TYPE_NAMETH LIKE '%{}%'
        #             AND vc.COLOR_NAMETH LIKE '%{}%'
        #             AND vp.PASS_TIME >= TO_TIMESTAMP('{}', 'YYYY-MM-DD')
        #             AND vp.PASS_TIME < TO_TIMESTAMP('{}', 'YYYY-MM-DD')
        #         ORDER BY vp.PASS_TIME DESC
        #         FETCH NEXT {} ROWS ONLY
        #     )
        # """.format(
        #     plate_no, province, checkpoint, direction, 
        #     vehicle_type, vehicle_color, start_date, end_date,
        #     self.limit_rows_query
        # )

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        total = data[0][0]

        return total

    def get_all_report(self, plate_no, province, checkpoint, direction, vehicle_type, vehicle_color, start_date, end_date):
        sql_command = """
            SELECT vu.PLATE_PIC_URL, vp.PLATE_NO, p.PROVINCE_NAMETH, ch.CHECKPOINT_NICKNAME, la.ROAD_DIRECTION, vp.PASS_TIME, vt.TYPE_NAMETH, vc.COLOR_NAMETH  
            FROM XVOT_XVOTDB_USER.VEHICLE_PASS vp
            JOIN CHECKPOINT ch 
                ON ch.AREA_CODE=vp.AREA_CODE AND ch.PROJECT_ID = 2
            JOIN VEHICLE_TYPE vt
                ON vt.TYPE_NAME=vp.VEHICLE_TYPE
            JOIN VEHICLE_COLOR vc
                ON vc.COLOR_NAME=vp.VEHICLE_COLOR 
            JOIN LANE la
                ON la.CHECKPOINT_ID=ch.CHECKPOINT_ID
                AND la.LANE_CODE =vp.LANE_NO
            JOIN XVOT_XVOTDB_USER.VEHICLE_URL vu
                ON vu.PASS_ID=vp.PASS_ID
            JOIN PROVINCE p 
                ON p.PROVINCE_ID=vp.PLATE_PROVINCE  
            WHERE vp.PLATE_NO like '%{}%'
                AND p.PROVINCE_NAMETH LIKE '%{}%'
                AND ch.CHECKPOINT_NAMETH LIKE '%{}%'
                AND la.ROAD_DIRECTION LIKE '%{}%'
                AND vt.TYPE_NAMETH LIKE '%{}%'
                AND vc.COLOR_NAMETH LIKE '%{}%'
                AND vp.PASS_TIME >= TO_TIMESTAMP('{}', 'YYYY-MM-DD')
                AND vp.PASS_TIME < TO_TIMESTAMP('{}', 'YYYY-MM-DD')
            ORDER BY vp.PASS_TIME DESC
            FETCH NEXT {} ROWS ONLY
        """.format(
            plate_no, province, checkpoint, direction, 
            vehicle_type, vehicle_color, start_date, end_date,
            self.limit_rows_query
        )

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'PLATE_PIC_URL': 'plate_picture',
            'PLATE_NO': 'plate_no',
            'PROVINCE_NAMETH': 'province',
            'CHECKPOINT_NICKNAME': 'checkpoint',
            'ROAD_DIRECTION': 'direction',
            'PASS_TIME': 'time',
            'TYPE_NAMETH': 'type',
            'COLOR_NAMETH': 'color'
        })

        base64_plate_pic = []

        for url in df['plate_picture']:
            if url:
                res = requests.get(url)
                base64_plate_pic.append(base64.b64encode(res.content))
            else:
                base64_plate_pic.append(url)

        df['base64_plate_pic'] = base64_plate_pic

        result = df.to_dict('records')

        return result

    def get_vehicle_all(self, plate_no, province, checkpoint, direction, vehicle_type, vehicle_color, start_date, end_date, page_data, total):
        if plate_no != '':
            plate_no = f" AND vp.PLATE_NO like '%{plate_no}%' "

        if province != '':
            province = f" AND PROVINCE_ID = {province} "

        if checkpoint != '':
            checkpoint = f" AND ch.CHECKPOINT_ID = {checkpoint} "

        if direction != '':
            direction = f" AND ROAD_DIRECTION = '{direction}' "

        if vehicle_type != '':
            if vehicle_type == 'vehicle':
                vehicle_type = f" AND VEHICLE_TYPE IN ('{vehicle_type}','motorVehicle')"
            else:
                vehicle_type = f" AND VEHICLE_TYPE = '{vehicle_type}' "

        if vehicle_color != '':
            vehicle_color = f" AND VEHICLE_COLOR = '{vehicle_color}' "

        sql_command = """
            SELECT 
                vp.PLATE_NO, vp.PASS_TIME
                ,vp.PASS_ID, vu.PLATE_PIC_URL, vu.IMAGE_PATH, vp.VEHICLE_COLOR, vp.VEHICLE_TYPE, p.PROVINCE_NAMETH, la.ROAD_DIRECTION ,ch.CHECKPOINT_NICKNAME, ch.LATITUDE, ch.LONGTITUDE, TYPE_NAMETH, COLOR_NAMETH
                FROM XVOT_XVOTDB_USER.VEHICLE_PASS vp
                LEFT JOIN CHECKPOINT ch 
                            ON ch.AREA_CODE=vp.AREA_CODE 
                LEFT JOIN PROVINCE p 
                            ON p.PROVINCE_ID=vp.PLATE_PROVINCE  
                LEFT JOIN (SELECT LANE_CODE, CHECKPOINT_ID,ROAD_DIRECTION FROM LANE ) la
                            ON la.CHECKPOINT_ID=ch.CHECKPOINT_ID
                            AND la.LANE_CODE =vp.LANE_NO             
                LEFT JOIN (SELECT PASS_ID, PLATE_PIC_URL, IMAGE_PATH 
                            FROM XVOT_XVOTDB_USER.VEHICLE_URL) vu
                            ON vu.PASS_ID=vp.PASS_ID
                LEFT JOIN (SELECT TYPE_NAME, TYPE_NAMETH FROM VEHICLE_TYPE ) vt 
                            ON vt.TYPE_NAME=vp.VEHICLE_TYPE
                LEFT JOIN VEHICLE_COLOR vc
                            ON vc.COLOR_NAME=vp.VEHICLE_COLOR 
                WHERE  vp.PASS_TIME >= TO_TIMESTAMP('{}', 'YYYY-MM-DD')
                    AND vp.PASS_TIME < TO_TIMESTAMP('{}', 'YYYY-MM-DD')
                    AND PROJECT_ID = 2 {} {} {} {} {} {}
                    ORDER BY vp.PASS_TIME DESC
                    
                
            OFFSET {} ROWS FETCH NEXT {} ROWS ONLY
        """.format(start_date, end_date,
            vehicle_color, vehicle_type, province, direction, 
            plate_no,checkpoint,
            page_data['offset'], page_data['page_size']
        )

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'PASS_ID': 'id',
            'PLATE_PIC_URL': 'plate_picture',
            'IMAGE_PATH': 'image_url',
            'PLATE_NO': 'plate_no',
            'PROVINCE_NAMETH': 'province',
            'CHECKPOINT_NICKNAME': 'checkpoint',
            'LATITUDE': 'latitude',
            'LONGTITUDE': 'longtitude',
            'ROAD_DIRECTION': 'direction',
            'PASS_TIME': 'time',
            'TYPE_NAMETH': 'type',
            'COLOR_NAMETH': 'color'
        })

        base64_plate_pic = []

        for url in df['plate_picture']:
            if url:
                try:
                    res = requests.get(url)
                    base64_plate_pic.append(base64.b64encode(res.content))
                except:
                    base64_plate_pic.append(url)
            else:
                base64_plate_pic.append(url)
            

        df['base64_plate_pic'] = base64_plate_pic

        result = df.to_dict('records')
        page_total = math.ceil(total / page_data['page_size'])

        paginate_data = {
            'page': page_data['page'],
            'page_size': page_data['page_size'],
            'page_total': page_total
        }

        return result, paginate_data

    def get_vehicle(self, plate_no, province, checkpoint, direction, vehicle_type, vehicle_color, start_date, end_date, page_data, total):
        sql_command = """
            SELECT vp.PASS_ID,vu.PLATE_PIC_URL, vu.IMAGE_PATH, vp.PLATE_NO, p.PROVINCE_NAMETH, ch.CHECKPOINT_NICKNAME, ch.LATITUDE, ch.LONGTITUDE, la.ROAD_DIRECTION, vp.PASS_TIME, vt.TYPE_NAMETH, vc.COLOR_NAMETH  
            FROM XVOT_XVOTDB_USER.VEHICLE_PASS vp
            JOIN CHECKPOINT ch 
                ON ch.AREA_CODE=vp.AREA_CODE AND ch.PROJECT_ID = 2
            JOIN VEHICLE_TYPE vt
                ON vt.TYPE_NAME=vp.VEHICLE_TYPE
            JOIN VEHICLE_COLOR vc
                ON vc.COLOR_NAME=vp.VEHICLE_COLOR 
            JOIN LANE la
                ON la.CHECKPOINT_ID=ch.CHECKPOINT_ID
                AND la.LANE_CODE =vp.LANE_NO
            JOIN XVOT_XVOTDB_USER.VEHICLE_URL vu
                ON vu.PASS_ID=vp.PASS_ID
            JOIN PROVINCE p 
                ON p.PROVINCE_ID=vp.PLATE_PROVINCE  
            WHERE vp.PLATE_NO like '%{}%'
                AND p.PROVINCE_NAMETH LIKE '%{}%'
                AND ch.CHECKPOINT_NAMETH LIKE '%{}%'
                AND la.ROAD_DIRECTION LIKE '%{}%'
                AND vt.TYPE_NAMETH LIKE '%{}%'
                AND vc.COLOR_NAMETH LIKE '%{}%'
                AND vp.PASS_TIME >= TO_TIMESTAMP('{}', 'YYYY-MM-DD')
                AND vp.PASS_TIME < TO_TIMESTAMP('{}', 'YYYY-MM-DD')
            ORDER BY vp.PASS_TIME DESC
            OFFSET {} ROWS FETCH NEXT {} ROWS ONLY
        """.format(
            plate_no, province, checkpoint, direction, 
            vehicle_type, vehicle_color, start_date, end_date,
            page_data['offset'], page_data['page_size']
        )

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'PASS_ID': 'id',
            'PLATE_PIC_URL': 'plate_picture',
            'IMAGE_PATH': 'image_url',
            'PLATE_NO': 'plate_no',
            'PROVINCE_NAMETH': 'province',
            'CHECKPOINT_NICKNAME': 'checkpoint',
            'LATITUDE': 'latitude',
            'LONGTITUDE': 'longtitude',
            'ROAD_DIRECTION': 'direction',
            'PASS_TIME': 'time',
            'TYPE_NAMETH': 'type',
            'COLOR_NAMETH': 'color'
        })

        base64_plate_pic = []

        for url in df['plate_picture']:
            if url:
                res = requests.get(url)
                base64_plate_pic.append(base64.b64encode(res.content))
            else:
                base64_plate_pic.append(url)

        df['base64_plate_pic'] = base64_plate_pic

        result = df.to_dict('records')
        page_total = math.ceil(total / page_data['page_size'])

        paginate_data = {
            'page': page_data['page'],
            'page_size': page_data['page_size'],
            'page_total': page_total
        }

        return result, paginate_data

    def get_violation_vehicle(self, plate_no, province, checkpoint, direction, vehicle_type, vehicle_color, start_date, end_date, page_data, total):
        sql_command = """
            SELECT vp.PASS_ID,vu.PLATE_PIC_URL, vu.IMAGE_PATH, vp.PLATE_NO, p.PROVINCE_NAMETH, ch.CHECKPOINT_NICKNAME, ch.LATITUDE, ch.LONGTITUDE, la.ROAD_DIRECTION, vp.PASS_TIME, vt.TYPE_NAMETH, vc.COLOR_NAMETH  
            FROM XVOT_XVOTDB_USER.VEHICLE_ALARM vp
            JOIN CHECKPOINT ch 
                ON ch.AREA_CODE=vp.AREA_CODE AND ch.PROJECT_ID = 2
            JOIN VEHICLE_TYPE vt
                ON vt.TYPE_NAME=vp.VEHICLE_TYPE
            JOIN VEHICLE_COLOR vc
                ON vc.COLOR_NAME=vp.VEHICLE_COLOR 
            JOIN LANE la
                ON la.CHECKPOINT_ID=ch.CHECKPOINT_ID
                AND la.LANE_CODE =vp.LANE_NO
            JOIN XVOT_XVOTDB_USER.VEHICLE_URL vu
                ON vu.PASS_ID=vp.PASS_ID
            JOIN PROVINCE p 
                ON p.PROVINCE_ID=vp.PLATE_PROVINCE  
            WHERE vp.PLATE_NO like '%{}%'
                AND p.PROVINCE_NAMETH LIKE '%{}%'
                AND ch.CHECKPOINT_NAMETH LIKE '%{}%'
                AND la.ROAD_DIRECTION LIKE '%{}%'
                AND vt.TYPE_NAMETH LIKE '%{}%'
                AND vc.COLOR_NAMETH LIKE '%{}%'
                AND vp.PASS_TIME >= TO_TIMESTAMP('{}', 'YYYY-MM-DD')
                AND vp.PASS_TIME < TO_TIMESTAMP('{}', 'YYYY-MM-DD')
                AND vp.VIOLATIVE_ACTION = '1625'
            ORDER BY vp.PASS_TIME DESC
            OFFSET {} ROWS FETCH NEXT {} ROWS ONLY
        """.format(
            plate_no, province, checkpoint, direction, 
            vehicle_type, vehicle_color, start_date, end_date,
            page_data['offset'], page_data['page_size']
        )

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'PASS_ID': 'id',
            'PLATE_PIC_URL': 'plate_picture',
            'IMAGE_PATH': 'image_url',
            'PLATE_NO': 'plate_no',
            'PROVINCE_NAMETH': 'province',
            'CHECKPOINT_NICKNAME': 'checkpoint',
            'LATITUDE': 'latitude',
            'LONGTITUDE': 'longtitude',
            'ROAD_DIRECTION': 'direction',
            'PASS_TIME': 'time',
            'TYPE_NAMETH': 'type',
            'COLOR_NAMETH': 'color'
        })

        base64_plate_pic = []

        for url in df['plate_picture']:
            if url:
                res = requests.get(url)
                base64_plate_pic.append(base64.b64encode(res.content))
            else:
                base64_plate_pic.append(url)

        df['base64_plate_pic'] = base64_plate_pic

        result = df.to_dict('records')
        page_total = math.ceil(total / page_data['page_size'])

        paginate_data = {
            'page': page_data['page'],
            'page_size': page_data['page_size'],
            'page_total': page_total
        }

        return result, paginate_data

    def get_blacklist(self, plate_no, province, checkpoint, direction, vehicle_type, vehicle_color, start_date, end_date, page_data, total, sub_query):
        sql_command = """
            SELECT * FROM (
                SELECT vu.PLATE_PIC_URL, vu.IMAGE_PATH, vp.PLATE_NO, p.PROVINCE_NAMETH, ch.CHECKPOINT_NICKNAME, ch.LATITUDE, ch.LONGTITUDE, la.ROAD_DIRECTION, vp.PASS_TIME, vt.TYPE_NAMETH, vc.COLOR_NAMETH  
                FROM XVOT_XVOTDB_USER.VEHICLE_PASS vp
                JOIN CHECKPOINT ch 
                    ON ch.AREA_CODE=vp.AREA_CODE AND ch.PROJECT_ID = 2
                JOIN VEHICLE_TYPE vt
                    ON vt.TYPE_NAME=vp.VEHICLE_TYPE
                JOIN VEHICLE_COLOR vc
                    ON vc.COLOR_NAME=vp.VEHICLE_COLOR 
                JOIN LANE la
                    ON la.CHECKPOINT_ID=ch.CHECKPOINT_ID
                    AND la.LANE_CODE =vp.LANE_NO
                JOIN XVOT_XVOTDB_USER.VEHICLE_URL vu
                    ON vu.PASS_ID=vp.PASS_ID
                JOIN PROVINCE p 
                    ON p.PROVINCE_ID=vp.PLATE_PROVINCE  
                WHERE {}
                    AND vp.PASS_TIME >= TO_TIMESTAMP('{}', 'YYYY-MM-DD')
                    AND vp.PASS_TIME < TO_TIMESTAMP('{}', 'YYYY-MM-DD')
                ORDER BY vp.PASS_TIME DESC
            )
            WHERE PLATE_NO like '%{}%'
                AND PROVINCE_NAMETH LIKE '%{}%'
                AND CHECKPOINT_NICKNAME LIKE '%{}%'
                AND ROAD_DIRECTION LIKE '%{}%'
                AND TYPE_NAMETH LIKE '%{}%'
                AND COLOR_NAMETH LIKE '%{}%' 
            OFFSET {} ROWS FETCH NEXT {} ROWS ONLY
        """.format(
            sub_query, start_date, end_date,
            plate_no, province, checkpoint, direction, 
            vehicle_type, vehicle_color,
            page_data['offset'], page_data['page_size']
        )

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'PLATE_PIC_URL': 'plate_picture',
            'IMAGE_PATH': 'image_url',
            'PLATE_NO': 'plate_no',
            'PROVINCE_NAMETH': 'province',
            'CHECKPOINT_NICKNAME': 'checkpoint',
            'LATITUDE': 'latitude',
            'LONGTITUDE': 'longtitude',
            'ROAD_DIRECTION': 'direction',
            'PASS_TIME': 'time',
            'TYPE_NAMETH': 'type',
            'COLOR_NAMETH': 'color'
        })

        base64_plate_pic = []
        base64_image_pic = []

        for url in df['plate_picture']:
            if url:
                res = requests.get(url)
                base64_plate_pic.append(base64.b64encode(res.content))
            else:
                base64_plate_pic.append(url)

        for url in df['image_url']:
            if url:
                res = requests.get(url)
                base64_image_pic.append(base64.b64encode(res.content))
            else:
                base64_image_pic.append(url)

        df['base64_plate_pic'] = base64_plate_pic
        df['base64_image_pic'] = base64_image_pic

        result = df.to_dict('records')
        page_total = math.ceil(total / page_data['page_size'])

        paginate_data = {
            'page': page_data['page'],
            'page_size': page_data['page_size'],
            'page_total': page_total
        }

        return result, paginate_data

    def get_blacklist_total(self, plate_no, province, checkpoint, direction, vehicle_type, vehicle_color, start_date, end_date, sub_query):
        sql_command = """
            select COUNT(*) from (
                SELECT vu.PLATE_PIC_URL, vu.IMAGE_PATH, vp.PLATE_NO, p.PROVINCE_NAMETH, ch.CHECKPOINT_NICKNAME, ch.LATITUDE, ch.LONGTITUDE, la.ROAD_DIRECTION, vp.PASS_TIME, vt.TYPE_NAMETH, vc.COLOR_NAMETH  
                FROM XVOT_XVOTDB_USER.VEHICLE_PASS vp
                JOIN CHECKPOINT ch 
                    ON ch.AREA_CODE=vp.AREA_CODE AND ch.PROJECT_ID = 2
                JOIN VEHICLE_TYPE vt
                    ON vt.TYPE_NAME=vp.VEHICLE_TYPE
                JOIN VEHICLE_COLOR vc
                    ON vc.COLOR_NAME=vp.VEHICLE_COLOR 
                JOIN LANE la
                    ON la.CHECKPOINT_ID=ch.CHECKPOINT_ID
                    AND la.LANE_CODE =vp.LANE_NO
                JOIN XVOT_XVOTDB_USER.VEHICLE_URL vu
                    ON vu.PASS_ID=vp.PASS_ID
                JOIN PROVINCE p 
                    ON p.PROVINCE_ID=vp.PLATE_PROVINCE  
                WHERE {}
                    AND vp.PASS_TIME >= TO_TIMESTAMP('{}', 'YYYY-MM-DD')
                    AND vp.PASS_TIME < TO_TIMESTAMP('{}', 'YYYY-MM-DD')
                ORDER BY vp.PASS_TIME DESC
            )
            WHERE PLATE_NO like '%{}%'
                AND PROVINCE_NAMETH LIKE '%%'
                AND CHECKPOINT_NICKNAME LIKE '%{}%'
                AND ROAD_DIRECTION LIKE '%{}%'
                AND TYPE_NAMETH LIKE '%{}%'
                AND COLOR_NAMETH LIKE '%{}%' 

            FETCH NEXT {} ROWS ONLY
        """.format(
            sub_query, start_date, end_date,
            plate_no, province, checkpoint, direction, 
            vehicle_type, vehicle_color,
            self.limit_rows_query
        )

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        total = data[0][0]

        return total

    def get_playback_data_by_pass_id(self, pass_id):
        sql_command = """
            SELECT vp.PASS_ID, ch.CHECKPOINT_ID, c.CAMERA_CODE, to_char(vp.PASS_TIME ,'YYYY-MM-DD hh24:mi:ss') AS PASS_TIME 
            FROM XVOT_XVOTDB_USER.VEHICLE_PASS vp
            JOIN CHECKPOINT ch 
                ON ch.AREA_CODE=vp.AREA_CODE AND ch.PROJECT_ID = 2
            JOIN LANE la
                ON la.CHECKPOINT_ID=ch.CHECKPOINT_ID
                AND la.LANE_CODE =vp.LANE_NO
            JOIN CAMERA c
                ON c.CAMERA_ID=la.CAMERA_ID
            JOIN PROVINCE p 
                ON p.PROVINCE_ID=vp.PLATE_PROVINCE
            WHERE vp.PASS_ID = '{}'
        """.format(pass_id)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'PASS_ID': 'pass_id',
            'CHECKPOINT_ID': 'checkpoint',
            'CAMERA_CODE': 'camera_code',
            'PASS_TIME': 'pass_time'
        })

        result = df.to_dict('records')

        return result

    def get_playback_data_by_violation_pass_id(self, pass_id):
        sql_command = """
            SELECT vp.PASS_ID, ch.CHECKPOINT_ID, c.CAMERA_CODE, to_char(vp.PASS_TIME ,'YYYY-MM-DD hh24:mi:ss') AS PASS_TIME 
            FROM XVOT_XVOTDB_USER.VEHICLE_ALARM vp
            JOIN CHECKPOINT ch 
                ON ch.AREA_CODE=vp.AREA_CODE AND ch.PROJECT_ID = 2
            JOIN LANE la
                ON la.CHECKPOINT_ID=ch.CHECKPOINT_ID
                AND la.LANE_CODE =vp.LANE_NO
            JOIN CAMERA c
                ON c.CAMERA_ID=la.CAMERA_ID
            JOIN PROVINCE p 
                ON p.PROVINCE_ID=vp.PLATE_PROVINCE
            WHERE vp.PASS_ID = '{}' AND vp.VIOLATIVE_ACTION = '1625'
        """.format(pass_id)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'PASS_ID': 'pass_id',
            'CHECKPOINT_ID': 'checkpoint',
            'CAMERA_CODE': 'camera_code',
            'PASS_TIME': 'pass_time'
        })

        result = df.to_dict('records')

        return result

    def get_report_by_id(self, id):
        sql_command = """
            SELECT vp.PASS_ID,vu.PLATE_PIC_URL, vu.IMAGE_PATH, vp.PLATE_NO, p.PROVINCE_NAMETH, ch.CHECKPOINT_NICKNAME, vp.PASS_TIME, vt.TYPE_NAMETH, vc.COLOR_NAMETH  
                FROM XVOT_XVOTDB_USER.VEHICLE_PASS vp
                JOIN CHECKPOINT ch 
                    ON ch.AREA_CODE=vp.AREA_CODE AND ch.PROJECT_ID = 2
                JOIN VEHICLE_TYPE vt
                    ON vt.TYPE_NAME=vp.VEHICLE_TYPE
                JOIN VEHICLE_COLOR vc
                    ON vc.COLOR_NAME=vp.VEHICLE_COLOR
                JOIN XVOT_XVOTDB_USER.VEHICLE_URL vu
                    ON vu.PASS_ID=vp.PASS_ID
                JOIN PROVINCE p 
                    ON p.PROVINCE_ID=vp.PLATE_PROVINCE  
                WHERE vp.PASS_ID = '{}'
        """.format(id)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        columns = [row[0] for row in cursor.description]

        df = pd.DataFrame(data=data, columns=columns)

        if not df.empty:
            df = df.rename(columns={
                'PASS_ID': 'id',
                'PLATE_PIC_URL': 'plate_picture',
                'IMAGE_PATH': 'image_url',
                'PLATE_NO': 'plate_no',
                'PROVINCE_NAMETH': 'province',
                'CHECKPOINT_NICKNAME': 'checkpoint',
                'PASS_TIME': 'time',
                'TYPE_NAMETH': 'type',
                'COLOR_NAMETH': 'color'
            })
            result = df.to_dict('records')
            result = result[0]

        else:
            response = {
                'status_code': 404,
                'message': 'Not found'
            }

            raise NotFound(response)

        return result

    def get_violation_report_by_id(self, id):
        sql_command = """
            SELECT vp.PASS_ID,vu.PLATE_PIC_URL, vu.IMAGE_PATH, vp.PLATE_NO, p.PROVINCE_NAMETH, ch.CHECKPOINT_NICKNAME, vp.PASS_TIME, vt.TYPE_NAMETH, vc.COLOR_NAMETH  
                FROM XVOT_XVOTDB_USER.VEHICLE_ALARM vp
                JOIN CHECKPOINT ch 
                    ON ch.AREA_CODE=vp.AREA_CODE AND ch.PROJECT_ID = 2
                JOIN VEHICLE_TYPE vt
                    ON vt.TYPE_NAME=vp.VEHICLE_TYPE
                JOIN VEHICLE_COLOR vc
                    ON vc.COLOR_NAME=vp.VEHICLE_COLOR
                JOIN XVOT_XVOTDB_USER.VEHICLE_URL vu
                    ON vu.PASS_ID=vp.PASS_ID
                JOIN PROVINCE p 
                    ON p.PROVINCE_ID=vp.PLATE_PROVINCE  
                WHERE vp.PASS_ID = '{}' AND vp.VIOLATIVE_ACTION = '1625'
        """.format(id)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        columns = [row[0] for row in cursor.description]

        df = pd.DataFrame(data=data, columns=columns)

        if not df.empty:
            df = df.rename(columns={
                'PASS_ID': 'id',
                'PLATE_PIC_URL': 'plate_picture',
                'IMAGE_PATH': 'image_url',
                'PLATE_NO': 'plate_no',
                'PROVINCE_NAMETH': 'province',
                'CHECKPOINT_NICKNAME': 'checkpoint',
                'PASS_TIME': 'time',
                'TYPE_NAMETH': 'type',
                'COLOR_NAMETH': 'color'
            })
            result = df.to_dict('records')
            result = result[0]

        else:
            response = {
                'status_code': 404,
                'message': 'Not found'
            }

            raise NotFound(response)

        return result

    def get_total_desination(self, date):
        sql_command = """
           SELECT TOTAL FROM BMA_PHASE_II.DESTINATIONS d WHERE CREATED_DATE = TO_TIMESTAMP('{}', 'YYYY-MM-DD')
           FETCH FIRST 1 ROWS ONLY
        """.format( date
        )

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        total = data[0][0]
        if total > self.limit_rows_query:
            total = self.limit_rows_query
        return total

    def get_destination_times_test(self, province, vehicle_type, vehicle_color, start_date, page_data, total):
        sql_command = """
            SELECT d.PLATE_NO, p.PROVINCE_NAMETH ,vt.TYPE_NAMETH, vc.COLOR_NAMETH, d.COUNT AS TIMES
            FROM BMA_PHASE_II.DESTINATIONS d
                JOIN PROVINCE p 
                    ON p.PROVINCE_ID = d.PROVINCE_ID
                JOIN VEHICLE_TYPE vt
                    ON vt.TYPE_ID = d.TYPE_ID
                JOIN VEHICLE_COLOR vc
                    ON vc.COLOR_ID = d.COLOR_ID
                WHERE d.CREATED_DATE  = TO_TIMESTAMP('{}', 'YYYY-MM-DD')
                    AND d.PROVINCE_ID LIKE '%{}%'
                    AND d.TYPE_ID LIKE '%{}%'
                    AND d.COLOR_ID LIKE '%{}%'
                    AND d.PLATE_NO != 'unknown'
                ORDER BY d.ID ASC
                OFFSET {} ROWS FETCH NEXT {} ROWS ONLY
        """.format(start_date,
            province,
            vehicle_type, vehicle_color, 
            page_data['offset'], page_data['page_size']
        )

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'PLATE_NO': 'plate_no',
            'PROVINCE_NAMETH': 'province',
            'TYPE_NAMETH': 'type',
            'COLOR_NAMETH': 'color',
            'TIMES':'times'
        })

        result = df.to_dict('records')
        page_total = math.ceil(total / page_data['page_size'])

        paginate_data = {
            'page': page_data['page'],
            'page_size': page_data['page_size'],
            'page_total': page_total
        }

        return result, paginate_data

    def get_destination_times(self, province, vehicle_type, vehicle_color, start_date,end_date, page_data, total):
        sql_command = """
            SELECT vp.PLATE_NO, p.PROVINCE_NAMETH ,vt.TYPE_NAMETH, vc.COLOR_NAMETH, COUNT(ch.CHECKPOINT_ID) AS TIMES
            FROM XVOT_XVOTDB_USER.VEHICLE_PASS vp
                JOIN CHECKPOINT ch 
                    ON ch.AREA_CODE=vp.AREA_CODE AND ch.PROJECT_ID = 2
                JOIN PROVINCE p 
                    ON p.PROVINCE_ID=vp.PLATE_PROVINCE
                JOIN VEHICLE_TYPE vt
                    ON vt.TYPE_NAME=vp.VEHICLE_TYPE
                JOIN VEHICLE_COLOR vc
                    ON vc.COLOR_NAME=vp.VEHICLE_COLOR
                WHERE vp.PASS_TIME >= TO_TIMESTAMP('{}', 'YYYY-MM-DD')
                    AND vp.PASS_TIME < TO_TIMESTAMP('{}', 'YYYY-MM-DD')
                    AND p.PROVINCE_NAMETH LIKE '%{}%'
                    AND vt.TYPE_NAMETH LIKE '%{}%'
                    AND vc.COLOR_NAMETH LIKE '%{}%'
                    AND vp.PLATE_NO != 'unknown'
                GROUP BY vp.PLATE_NO,p.PROVINCE_NAMETH,vt.TYPE_NAMETH, vc.COLOR_NAMETH
                HAVING
                    COUNT( ch.CHECKPOINT_ID ) > 1
                OFFSET {}  ROWS FETCH NEXT {} ROWS ONLY
        """.format(start_date,end_date,
            province,
            vehicle_type, vehicle_color, 
            page_data['offset'], page_data['page_size']
        )

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'PLATE_NO': 'plate_no',
            'PROVINCE_NAMETH': 'province',
            'TYPE_NAMETH': 'type',
            'COLOR_NAMETH': 'color',
            'TIMES':'times'
        })

        result = df.to_dict('records')
        page_total = math.ceil(total / page_data['page_size'])

        paginate_data = {
            'page': page_data['page'],
            'page_size': page_data['page_size'],
            'page_total': page_total
        }

        return result, paginate_data

    def get_destination_vehicle(self,plate_no, province, vehicle_type, vehicle_color, start_date, end_date):
        sql_command = """
            SELECT vp.PASS_ID,vu.PLATE_PIC_URL,vu.IMAGE_PATH, ch.CHECKPOINT_NICKNAME, ch.LATITUDE, ch.LONGTITUDE ,la.ROAD_DIRECTION, TO_CHAR(vp.PASS_TIME,'YYYY-MM-DD HH24:MI:SS') AS PASS_TIME
            FROM XVOT_XVOTDB_USER.VEHICLE_PASS vp
                JOIN CHECKPOINT ch 
                    ON ch.AREA_CODE=vp.AREA_CODE AND ch.PROJECT_ID = 2
                JOIN VEHICLE_TYPE vt
                    ON vt.TYPE_NAME=vp.VEHICLE_TYPE
                JOIN VEHICLE_COLOR vc
                    ON vc.COLOR_NAME=vp.VEHICLE_COLOR 
                JOIN LANE la
                    ON la.CHECKPOINT_ID=ch.CHECKPOINT_ID
                    AND la.LANE_CODE =vp.LANE_NO
                JOIN XVOT_XVOTDB_USER.VEHICLE_URL vu
                    ON vu.PASS_ID=vp.PASS_ID
                JOIN PROVINCE p 
                    ON p.PROVINCE_ID=vp.PLATE_PROVINCE  
                WHERE vp.PLATE_NO like '%{}%'
                    AND p.PROVINCE_NAMETH LIKE '%{}%'
                    AND vt.TYPE_NAMETH LIKE '%{}%'
                    AND vc.COLOR_NAMETH LIKE '%{}%'
                    AND vp.PASS_TIME >= TO_TIMESTAMP('{}', 'YYYY-MM-DD')
                    AND vp.PASS_TIME < TO_TIMESTAMP('{}', 'YYYY-MM-DD')
                ORDER BY vp.PASS_TIME ASC
        """.format(plate_no,province,vehicle_type, vehicle_color,
        start_date, end_date
        )

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'PASS_ID': 'id',
            'PLATE_PIC_URL': 'plate_picture',
            'IMAGE_PATH': 'image_url',
            'ROAD_DIRECTION': 'direction',
            'CHECKPOINT_NICKNAME': 'checkpoint',
            'PASS_TIME': 'time',
            'LATITUDE': 'latitude',
            'LONGTITUDE': 'longtitude',
        })

        result = df.to_dict('records')

        return result

    # def get_destination_by_id(self, id):
    #     sql_command = """
    #         SELECT vp.PASS_ID,vu.PLATE_PIC_URL, vu.IMAGE_PATH, vp.PLATE_NO, p.PROVINCE_NAMETH, ch.CHECKPOINT_NICKNAME, vp.PASS_TIME, vt.TYPE_NAMETH, vc.COLOR_NAMETH, ch.LATITUDE, ch.LONGTITUDE 
    #             FROM XVOT_XVOTDB_USER.VEHICLE_PASS vp
    #             JOIN CHECKPOINT ch 
    #                 ON ch.AREA_CODE=vp.AREA_CODE AND ch.PROJECT_ID = 1
    #             JOIN VEHICLE_TYPE vt
    #                 ON vt.TYPE_NAME=vp.VEHICLE_TYPE
    #             JOIN VEHICLE_COLOR vc
    #                 ON vc.COLOR_NAME=vp.VEHICLE_COLOR
    #             JOIN XVOT_XVOTDB_USER.VEHICLE_URL vu
    #                 ON vu.PASS_ID=vp.PASS_ID
    #             JOIN PROVINCE p 
    #                 ON p.PROVINCE_ID=vp.PLATE_PROVINCE  
    #             WHERE vp.PASS_ID = '{}'
    #     """.format(id)

    #     cursor = self.oracle_connection.cursor()
    #     cursor.execute(sql_command)
    #     data = cursor.fetchall()
    #     columns = [row[0] for row in cursor.description]

    #     df = pd.DataFrame(data=data, columns=columns)

    #     if not df.empty:
    #         df = df.rename(columns={
    #             'PASS_ID': 'id',
    #             'PLATE_PIC_URL': 'plate_picture',
    #             'IMAGE_PATH': 'image_url',
    #             'PLATE_NO': 'plate_no',
    #             'PROVINCE_NAMETH': 'province',
    #             'CHECKPOINT_NICKNAME': 'checkpoint',
    #             'PASS_TIME': 'time',
    #             'TYPE_NAMETH': 'type',
    #             'LATITUDE': 'latitude',
    #             'LONGTITUDE': 'longtitude',
    #             'COLOR_NAMETH': 'color'
    #         })
    #         result = df.to_dict('records')
    #         # result = result[0]

    #     else:
    #         response = {
    #             'status_code': 404,
    #             'message': 'Not found'
    #         }

    #         raise NotFound(response)

    #     return result