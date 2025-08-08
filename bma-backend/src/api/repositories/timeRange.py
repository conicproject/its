from api.models.timeRange import TimeRangeModel
from rest_framework.exceptions import NotFound
from api.connections.oracle import OracleConnection

import pandas as pd

class TimeRangeRepository:

    def __init__(self):
        self.oracle_connection = OracleConnection().get_connection()
        self.not_found_msg = 'time range now found'
    

    def get_all(self):
        sql_command = 'SELECT * FROM BMA_PHASE_II.TIME_RANGES'

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        columns = [row[0] for row in cursor.description]

        df = pd.DataFrame(data=data, columns=columns)
        df = df.rename(columns={
            "ID": "id",
            "START_TIME": "start_time",
            "END_TIME": "end_time"
        })

        result = df.to_dict('records')

        return result


    def get_by_id(self, id):
        try:
            data = TimeRangeModel.objects.get(id=id)
        
        except TimeRangeModel.DoesNotExist:
            response = {
                'status_code': 404,
                'message': self.not_found_msg
            }

            raise NotFound(response)
    

    def get_by_endtime(self, end_time):
        sql_command = """
            SELECT * FROM BMA_PHASE_II.TIME_RANGES
            WHERE END_TIME = '{}'
        """.format(end_time)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        columns = [row[0] for row in cursor.description]

        df = pd.DataFrame(data=data, columns=columns)

        if not df.empty:
            df = df.rename(columns={
                "ID": "id",
                "START_TIME": "start_time",
                "END_TIME": "end_time"
            })
            result = df.to_dict('records')
            data = result[0]

        else:
            response = {
                'status_code': 404,
                'message': self.not_found_msg
            }

            raise NotFound(response)
        
        return data


    def get_by_starttime(self, start_time):
        try:
            data = TimeRangeModel.objects.get(start_time=start_time)
        
        except TimeRangeModel.DoesNotExist:
            response = {
                'status_code': 404,
                'message': self.not_found_msg
            }

            raise NotFound(response)
        
        return data


    def get_first_record(self):
        data = TimeRangeModel.objects.first()

        return data
    

    def get_last_record(self):
        data = TimeRangeModel.objects.latest('id')

        return data