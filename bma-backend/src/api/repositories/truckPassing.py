from api.connections.oracle import OracleConnection

from rest_framework.exceptions import NotFound
from api.models.truckPassing import TruckPassingModel

import pandas as pd

class TruckPassingRepository:

    def __init__(self):
        self.oracle_connection = OracleConnection().get_connection()
        self.max_search_record = 10000


    def search_truck(self, payload, page_data):
        sql_command = """
            SELECT * FROM BMA_PHASE_II.TRUCKS_PASSING tp
            WHERE CHECKPOINT like '%{}%'
                AND DIRECTION like '%{}%'
                AND PASS_TIME >= TO_DATE('{}','YYYY-MM-DD hh24:mi:ss')
                AND PASS_TIME < TO_DATE('{}','YYYY-MM-DD hh24:mi:ss')
                AND EXTRACT(HOUR FROM PASS_TIME) >= '{}'
                AND EXTRACT(HOUR FROM PASS_TIME) < '{}'
            ORDER BY ID DESC
            OFFSET {} ROWS FETCH NEXT {} ROWS ONLY
        """.format(
            payload['checkpoint'], payload['direction'], 
            payload['start_date'], payload['end_date'],
            payload['starttime'], payload['endtime'],
            page_data['offset'], page_data['page_size']
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        columns = [col[0].lower() for col in cursor.description]
        
        try:
            df = pd.DataFrame(data=data, columns=columns)
            df = df.rename(columns={
                'plate_url': 'plate_picture',
                'pass_time': 'time'
            })

            result = df.to_dict('records')
        # result = sql_command
        except:
            result = []
        
        return result


    def total_search_truck(self, payload):
        sql_command = """
            SELECT COUNT(*) AS counting FROM (
                SELECT * FROM BMA_PHASE_II.TRUCKS_PASSING tp
                WHERE CHECKPOINT like '%{}%'
                    AND DIRECTION like '%{}%'
                    AND PASS_TIME >= TO_DATE('{}','YYYY-MM-DD hh24:mi:ss')
                    AND PASS_TIME < TO_DATE('{}','YYYY-MM-DD hh24:mi:ss')
                AND ROWNUM <= {}
            ) 
        """.format(
            payload['checkpoint'], payload['direction'], 
            payload['start_date'], payload['end_date'],
            self.max_search_record
        )
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        total = data[0][0]

        return total


    def get_by_id(self, id):
        sql_command = """
            SELECT * FROM BMA_PHASE_II.TRUCKS_PASSING tp
            WHERE ID = {}
        """.format(id)
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        columns = [col[0].lower()  for col in cursor.description]
        
        try:
            df = pd.DataFrame(data=data, columns=columns)

            result = df.to_dict('records')
        # result = sql_command
        except:
            response = {
                'status_code': 404,
                'message': 'Not found'
            }

            raise NotFound(response)
        return result[0]