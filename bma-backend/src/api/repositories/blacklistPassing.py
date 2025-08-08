from django.db import connection

from api.connections.oracle import OracleConnection
from rest_framework.exceptions import NotFound, PermissionDenied
from api.models.blacklistPassing import BlacklistPassingModel

import pandas as pd
from PIL import Image
import requests
from io import BytesIO
import base64

class BlacklistPassingRepository:

    def __init__(self):
        self.oracle_connection = OracleConnection().get_connection()
        self.max_search_record = 10000


    def search_blacklist(self, payload, page_data, blacklist_ids):
        sql_command = """
            SELECT * FROM BMA_PHASE_II.BLACKLISTS_PASSING
            WHERE PLATE_NO LIKE '%{}%'
                AND PROVINCE LIKE '%{}%'
                AND CHECKPOINT LIKE '%{}%'
                AND DIRECTION  LIKE '%{}%'
                AND "TYPE" LIKE '%{}%'
                AND COLOR LIKE '%{}%'
                AND PASS_TIME >= TO_TIMESTAMP('{}', 'YYYY-MM-DD hh24:mi:ss')
                AND PASS_TIME < TO_TIMESTAMP('{}', 'YYYY-MM-DD hh24:mi:ss')
                AND BLACKLIST_ID IN {}
            ORDER BY PASS_TIME DESC 
            OFFSET {} ROWS FETCH NEXT {} ROWS ONLY
        """.format(
            payload['plate_no'], payload['province'], payload['checkpoint'],
            payload['direction'], payload['vehicle_type'], payload['vehicle_color'],
            payload['start_date'], payload['end_date'], blacklist_ids,
            page_data['offset'], page_data['page_size']
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        columns = [row[0] for row in cursor.description]

        df = pd.DataFrame(data=data, columns=columns)

        if not df.empty:
            df = df.rename(columns={
                'ID': 'id',
                'BLACKLIST_ID': 'blacklist_id',
                'PASS_ID': 'pass_id',
                'PLATE_URL': 'plate_picture',
                'IMAGE_URL': 'image_url',
                'PLATE_NO': 'plate_no',
                'PROVINCE': 'province',
                'CHECKPOINT': 'checkpoint',
                'LATITUDE': 'latitude',
                'LONGTITUDE': 'longtitude',
                'DIRECTION': 'direction',
                'PASS_TIME': 'time',
                'TYPE': 'type',
                'COLOR': 'color',
                'RTSP_URL': 'rtsp_url'
            })

            df = df.drop(columns=['pass_id'])
            result = df.to_dict('records')

        else:
            result = []

        return result


    def total_search_blacklist(self, payload, blacklist_ids):
        sql_command = """
            SELECT COUNT(*) FROM (
                SELECT * FROM BMA_PHASE_II.BLACKLISTS_PASSING
                WHERE PLATE_NO LIKE '%{}%'
                    AND PROVINCE LIKE '%{}%'
                    AND CHECKPOINT LIKE '%{}%'
                    AND DIRECTION  LIKE '%{}%'
                    AND "TYPE" LIKE '%{}%'
                    AND COLOR LIKE '%{}%'
                    AND PASS_TIME >= TO_TIMESTAMP('{}', 'YYYY-MM-DD hh24:mi:ss')
                    AND PASS_TIME < TO_TIMESTAMP('{}', 'YYYY-MM-DD hh24:mi:ss')
                    AND BLACKLIST_ID IN {}
                ORDER BY PASS_TIME DESC 
                FETCH NEXT {} ROWS ONLY
            )
        """.format(
            payload['plate_no'], payload['province'], payload['checkpoint'],
            payload['direction'], payload['vehicle_type'], payload['vehicle_color'],
            payload['start_date'], payload['end_date'], blacklist_ids,
            self.max_search_record
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        total = data[0][0]

        return total


    def search_blacklist_master_group(self, payload, page_data):
        sql_command = """
            SELECT * FROM BMA_PHASE_II.BLACKLISTS_PASSING
            WHERE PLATE_NO LIKE '%{}%'
                AND PROVINCE LIKE '%{}%'
                AND CHECKPOINT LIKE '%{}%'
                AND DIRECTION  LIKE '%{}%'
                AND "TYPE" LIKE '%{}%'
                AND COLOR LIKE '%{}%'
                AND PASS_TIME >= TO_TIMESTAMP('{}', 'YYYY-MM-DD hh24:mi:ss')
                AND PASS_TIME < TO_TIMESTAMP('{}', 'YYYY-MM-DD hh24:mi:ss')
            ORDER BY PASS_TIME DESC 
            OFFSET {} ROWS FETCH NEXT {} ROWS ONLY
        """.format(
            payload['plate_no'], payload['province'], payload['checkpoint'],
            payload['direction'], payload['vehicle_type'], payload['vehicle_color'],
            payload['start_date'], payload['end_date'],
            page_data['offset'], page_data['page_size']
        )

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        columns = [row[0] for row in cursor.description]

        df = pd.DataFrame(data=data, columns=columns)

        if not df.empty:
            df = df.rename(columns={
                'ID': 'id',
                'BLACKLIST_ID': 'blacklist_id',
                'PASS_ID': 'pass_id',
                'PLATE_URL': 'plate_picture',
                'IMAGE_URL': 'image_url',
                'PLATE_NO': 'plate_no',
                'PROVINCE': 'province',
                'CHECKPOINT': 'checkpoint',
                'LATITUDE': 'latitude',
                'LONGTITUDE': 'longtitude',
                'DIRECTION': 'direction',
                'PASS_TIME': 'time',
                'TYPE': 'type',
                'COLOR': 'color',
                'RTSP_URL': 'rtsp_url'
            })

            df = df.drop(columns=['pass_id'])
            result = df.to_dict('records')

        else:
            result = []

        return result


    def total_search_blacklist_master_group(self, payload):
        sql_command = """
            SELECT COUNT(*) FROM (
                SELECT * FROM BMA_PHASE_II.BLACKLISTS_PASSING
                WHERE PLATE_NO LIKE '%{}%'
                    AND PROVINCE LIKE '%{}%'
                    AND CHECKPOINT LIKE '%{}%'
                    AND DIRECTION  LIKE '%{}%'
                    AND "TYPE" LIKE '%{}%'
                    AND COLOR LIKE '%{}%'
                    AND PASS_TIME >= TO_TIMESTAMP('{}', 'YYYY-MM-DD hh24:mi:ss')
                    AND PASS_TIME < TO_TIMESTAMP('{}', 'YYYY-MM-DD hh24:mi:ss')
                ORDER BY PASS_TIME DESC 
                FETCH NEXT {} ROWS ONLY
            )
        """.format(
            payload['plate_no'], payload['province'], payload['checkpoint'],
            payload['direction'], payload['vehicle_type'], payload['vehicle_color'],
            payload['start_date'], payload['end_date'],
            self.max_search_record
        )

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        total = data[0][0]

        return total


    def search_notification(self, start_datetime, end_datetime, blacklist_ids):
        sql_command = """
            SELECT ID, PASS_TIME FROM BMA_PHASE_II.BLACKLISTS_PASSING
            WHERE PASS_TIME >= TO_TIMESTAMP('{}', 'YYYY-MM-DD hh24:mi:ss')
                AND PASS_TIME <= TO_TIMESTAMP('{}', 'YYYY-MM-DD hh24:mi:ss')
                AND BLACKLIST_ID IN {}
            ORDER BY ID DESC
        """.format(start_datetime, end_datetime, blacklist_ids)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        columns = [row[0] for row in cursor.description]

        df = pd.DataFrame(data=data, columns=columns)

        if not df.empty:
            df = df.rename(columns={
                'ID': 'id',
                'PASS_TIME': 'time'
            })
            result = df.to_dict('records')

        else:
            result = []

        return result


    def search_notification_master_group(self, start_datetime, end_datetime):
        sql_command = """
            SELECT ID, PASS_TIME FROM BMA_PHASE_II.BLACKLISTS_PASSING
            WHERE PASS_TIME >= TO_TIMESTAMP('{}', 'YYYY-MM-DD hh24:mi:ss')
                AND PASS_TIME <= TO_TIMESTAMP('{}', 'YYYY-MM-DD hh24:mi:ss')
            ORDER BY ID DESC
        """.format(start_datetime, end_datetime)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        columns = [row[0] for row in cursor.description]

        df = pd.DataFrame(data=data, columns=columns)

        if not df.empty:
            df = df.rename(columns={
                'ID': 'id',
                'PASS_TIME': 'time'
            })
            result = df.to_dict('records')

        else:
            result = []

        return result


    def get_by_id(self, id):
        sql_command = """
            SELECT * FROM BMA_PHASE_II.BLACKLISTS_PASSING
            WHERE ID = {}
        """.format(id)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        columns = [row[0] for row in cursor.description]

        df = pd.DataFrame(data=data, columns=columns)

        if not df.empty:
            df = df.rename(columns={
                'ID': 'id',
                'BLACKLIST_ID': 'blacklist_id',
                'PASS_ID': 'pass_id',
                'PLATE_URL': 'plate_picture',
                'IMAGE_URL': 'image_url',
                'PLATE_NO': 'plate_no',
                'PROVINCE': 'province',
                'CHECKPOINT': 'checkpoint',
                'LATITUDE': 'latitude',
                'LONGTITUDE': 'longtitude',
                'DIRECTION': 'direction',
                'PASS_TIME': 'time',
                'TYPE': 'type',
                'COLOR': 'color',
                'RTSP_URL': 'rtsp_url'
            })
            # df = df.drop(columns=['pass_id'])
            result = df.to_dict('records')
            result = result[0]

        else:
            response = {
                'status_code': 404,
                'message': 'Not found'
            }

            raise NotFound(response)

        return result


    def validate_blacklist_passing(self, id, blacklist_ids):
        sql_command = """
            SELECT * FROM BMA_PHASE_II.BLACKLISTS_PASSING
            WHERE ID = {}
                AND BLACKLIST_ID IN {}
        """.format(id, blacklist_ids)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        columns = [row[0] for row in cursor.description]

        df = pd.DataFrame(data=data, columns=columns)

        if df.empty:
            response = {
                'status_code': 403,
                'message': 'permission denied'
            }

            raise PermissionDenied(response)


    def total_status_false(self):
        with connection.cursor() as cursor:
            cursor.execute(
                """
                    SELECT COUNT(*) FROM BMA_PHASE_II.BLACKLISTS_PASSING
                    WHERE STATUS = 'FALSE'
                """
            )

            data = cursor.fetchall()
            total = data[0][0]

        return total

    def update_status(self, id):
        with connection.cursor() as cursor:
            cursor.execute(
                """
                    SELECT COUNT(*) FROM BMA_PHASE_II.BLACKLISTS_PASSING
                    WHERE STATUS = 'TRUE' AND ID = '{}'
                """.format(id)
            )

            data = cursor.fetchall()
            total = data[0][0]

            sql_command = """
                UPDATE BMA_PHASE_II.BLACKLISTS_PASSING
                SET STATUS = 'TRUE'
                WHERE ID = '{}'
            """.format(id)

            cursor.execute(sql_command)

        return total

    def update_status_previous_date(self, now):
        with connection.cursor() as cursor:
            sql_command = """
                UPDATE BMA_PHASE_II.BLACKLISTS_PASSING
                SET STATUS = 'TRUE'
                WHERE TRUNC(PASS_TIME) < TO_TIMESTAMP('{}','YYYY-MM-DD') 
            """.format(now)

            cursor.execute(sql_command)

        return True
