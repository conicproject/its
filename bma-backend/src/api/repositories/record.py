from unittest import result
from api.models.record import RecordModel
from django.db.models import Sum
from api.connections.oracle import OracleConnection

import datetime
import pandas as pd

class RecordRepository:

    def __init__(self):
        self.oracle_connection = OracleConnection().get_connection()


    def get_by_time_payloads(self, payload):
        data = RecordModel.objects.filter(
            date=payload['date'],
            time_range_id__gt=payload['start_time_id'],
            time_range_id__lte=payload['end_time_id']
        )

        return data


    def get_total(self, payload):
        sql_command = '''
            SELECT SUM(VOLUME) AS total FROM BMA_PHASE_II.RECORDS
            WHERE CREATED_DATE = TO_DATE('{}', 'YYYY-MM-DD')
                AND TIME_RANGE_ID > {}
                AND TIME_RANGE_ID <= {}
        '''.format(
            payload['date'], payload['start_time_id'], payload['end_time_id']
        )

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        total = data[0][0]

        return total


    def get_total_by_checkpoint(self, payload, checkpoint_id):
        sql_command = '''
            SELECT SUM(VOLUME) AS total FROM BMA_PHASE_II.RECORDS
            WHERE CREATED_DATE = TO_DATE('{}', 'YYYY-MM-DD')
                AND TIME_RANGE_ID > {}
                AND TIME_RANGE_ID <= {}
                AND CHECKPOINT_ID = {}
        '''.format(
            payload['date'], 
            payload['start_time_id'], payload['end_time_id'],
            checkpoint_id
        )

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        total = data[0][0]

        return total

    # def get_checkpoint(self):
    #     sql_command = '''
    #         SELECT DISTINCT TO_NUMBER(CHECKPOINT_ID) AS CHECKPOINT_ID
    #         FROM SYS.CHECKPOINT
    #         ORDER BY TO_NUMBER(CHECKPOINT_ID) ASC
    #     '''
    #     cursor = self.oracle_connection.cursor()
    #     cursor.execute(sql_command)
    #     data = cursor.fetchall()

    #     columns = [col[0] for col in cursor.description]
    #     df = pd.DataFrame(data, columns=columns)
    #     result = df.to_dict('records')

    #     return result
    
    def get_all_car_type(self, payload):
        sql_command = '''
            SELECT CAR_TYPE_ID, SUM(VOLUME) AS VOLUME 
            FROM BMA_PHASE_II.RECORDS 
            WHERE CREATED_DATE = TO_DATE('{}', 'YYYY-MM-DD')
                AND TIME_RANGE_ID > {}
                AND TIME_RANGE_ID <= {}
            GROUP BY CAR_TYPE_ID
            ORDER BY CAR_TYPE_ID
        '''.format(
            payload['date'], payload['start_time_id'], payload['end_time_id']
        )

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        columns = [row[0] for row in cursor.description]

        df = pd.DataFrame(data=data, columns=columns)
        df = df.rename(columns={
            "CAR_TYPE_ID": "car_type_id",
            "VOLUME": "volume"
        })

        result = df.to_dict('records')

        return result

    def get_sum_group_by_car_type(self, payload, checkpoint_id):
        sql_command = '''
            SELECT CAR_TYPE_ID, SUM(VOLUME) AS VOLUME FROM BMA_PHASE_II.RECORDS 
            WHERE CREATED_DATE = TO_DATE('{}', 'YYYY-MM-DD')
                AND TIME_RANGE_ID > {}
                AND TIME_RANGE_ID <= {}
                AND CHECKPOINT_ID = {}
            GROUP BY CAR_TYPE_ID
            ORDER BY CAR_TYPE_ID
        '''.format(
            payload['date'], 
            payload['start_time_id'], payload['end_time_id'],
            checkpoint_id
        )

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        columns = [row[0] for row in cursor.description]

        df = pd.DataFrame(data=data, columns=columns)
        df = df.rename(columns={
            "CAR_TYPE_ID": "car_type_id",
            "VOLUME": "volume"
        })

        result = df.to_dict('records')

        return result 


    def get_sum_group_by_dir(self, payload):
        sql_command = '''
            SELECT DIRECTION, SUM(VOLUME) AS VOLUME FROM BMA_PHASE_II.RECORDS
            WHERE CREATED_DATE = TO_DATE('{}', 'YYYY-MM-DD')
                AND TIME_RANGE_ID > {}
                AND TIME_RANGE_ID <= {}
            GROUP BY DIRECTION
            ORDER BY DIRECTION
        '''.format(
            payload['date'], payload['start_time_id'], payload['end_time_id'],
        )

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        columns = [row[0] for row in cursor.description]

        df = pd.DataFrame(data=data, columns=columns)
        df = df.rename(columns={
            "DIRECTION": "direction",
            "VOLUME": "volume"
        })

        result = df.to_dict('records')

        return result


    def get_sum_group_by_dir_checkpoint(self, payload, checkpoint_id):
        sql_command = '''
            SELECT DIRECTION, SUM(VOLUME) AS VOLUME FROM BMA_PHASE_II.RECORDS
            WHERE CREATED_DATE = TO_DATE('{}', 'YYYY-MM-DD')
                AND TIME_RANGE_ID > {}
                AND TIME_RANGE_ID <= {}
                AND CHECKPOINT_ID = {}
            GROUP BY DIRECTION
            ORDER BY DIRECTION
        '''.format(
            payload['date'], 
            payload['start_time_id'], payload['end_time_id'],
            checkpoint_id
        )

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        columns = [row[0] for row in cursor.description]

        df = pd.DataFrame(data=data, columns=columns)
        df = df.rename(columns={
            "DIRECTION": "direction",
            "VOLUME": "volume"
        })

        result = df.to_dict('records')

        return result


    def get_by_date(self, date, checkpoint_id):
        sql_command = '''
            SELECT DIRECTION, TIME_RANGE_ID, CREATED_DATE, CAR_TYPE_ID, VOLUME FROM BMA_PHASE_II.RECORDS
            WHERE CREATED_DATE = TO_DATE('{}', 'YYYY-MM-DD')
                AND CHECKPOINT_ID = {}
        '''.format(date, checkpoint_id)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        columns = [row[0] for row in cursor.description]

        df = pd.DataFrame(data=data, columns=columns)
        df = df.rename(columns={
            "DIRECTION": "direction",
            "TIME_RANGE_ID": "time_range_id",
            "CREATED_DATE": "date",
            "CAR_TYPE_ID": "car_type_id",
            "VOLUME": "volume"
        })

        data = df.to_dict('records')

        return data


    def get_time_type_direction_by_date_range(self, start_date, end_date, checkpoint_id):
        # data = (RecordModel.objects.filter(
        #     date__gte=start_date,
        #     date__lt=end_date,
        #     checkpoint_id=checkpoint_id)
        #     .values('time_range_id', 'direction', 'car_type_id')
        #     .annotate(volume=Sum('volume'))
        #     .order_by('time_range_id', 'direction', 'car_type_id')
        # )

        sql_command = '''
            SELECT TIME_RANGE_ID, DIRECTION, CAR_TYPE_ID, SUM(VOLUME) AS VOLUME FROM BMA_PHASE_II.RECORDS
            WHERE CREATED_DATE >= TO_DATE('{}', 'YYYY-MM-DD')
                AND CREATED_DATE < TO_DATE('{}', 'YYYY-MM-DD')
                AND CHECKPOINT_ID = {}
            GROUP BY TIME_RANGE_ID, DIRECTION, CAR_TYPE_ID 
            ORDER BY TIME_RANGE_ID, DIRECTION, CAR_TYPE_ID
        '''.format(start_date, end_date, checkpoint_id)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        columns = [row[0] for row in cursor.description]

        df = pd.DataFrame(data=data, columns=columns)
        df = df.rename(columns={
            "TIME_RANGE_ID": "time_range_id",
            "DIRECTION": "direction",
            "CAR_TYPE_ID": "car_type_id",
            "VOLUME": "volume"
        })

        result = df.to_dict('records')

        return result

        return data


    def get_by_date_range(self, start_date, end_date, checkpoint_id):
        sql_command = '''
            SELECT DIRECTION, CREATED_DATE, CAR_TYPE_ID, SUM(VOLUME) AS VOLUME FROM BMA_PHASE_II.RECORDS
            WHERE CREATED_DATE >= TO_DATE('{}', 'YYYY-MM-DD')
                AND CREATED_DATE < TO_DATE('{}', 'YYYY-MM-DD')
                AND CHECKPOINT_ID = {}
            GROUP BY DIRECTION, CREATED_DATE, CAR_TYPE_ID 
            ORDER BY DIRECTION, CREATED_DATE, CAR_TYPE_ID
        '''.format(start_date, end_date, checkpoint_id)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        columns = [row[0] for row in cursor.description]

        df = pd.DataFrame(data=data, columns=columns)
        df = df.rename(columns={
            "DIRECTION": "direction",
            "CREATED_DATE": "date",
            "CAR_TYPE_ID": "car_type_id",
            "VOLUME": "volume"
        })

        result = df.to_dict('records')

        return result

    def get_time_type_direction_by_year(self, year, checkpoint_id):

        # data = (RecordModel.objects.filter(
        #     date__year=year,
        #     checkpoint_id=checkpoint_id)
        #     .values('time_range_id', 'direction', 'car_type_id')
        #     .annotate(volume=Sum('volume'))
        #     .order_by('time_range_id', 'direction', 'car_type_id')
        # )
        
        sql_command = '''
            SELECT TIME_RANGE_ID, DIRECTION, CAR_TYPE_ID, SUM(VOLUME) AS VOLUME FROM BMA_PHASE_II.RECORDS 
            WHERE EXTRACT(YEAR FROM CREATED_DATE) = '{}'
                AND CHECKPOINT_ID = {}
            GROUP BY TIME_RANGE_ID, DIRECTION, CAR_TYPE_ID 
            ORDER BY TIME_RANGE_ID, DIRECTION, CAR_TYPE_ID
        '''.format(
            year, 
            checkpoint_id
        )

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        columns = [row[0] for row in cursor.description]

        df = pd.DataFrame(data=data, columns=columns)
        df = df.rename(columns={
            "TIME_RANGE_ID":"time_range_id",
            "DIRECTION": "direction",
            "CAR_TYPE_ID": "car_type_id",
            "VOLUME": "volume"
        })

        result = df.to_dict('records')
        
        return result

    def get_by_year(self, year, checkpoint_id):
        # data = (RecordModel.objects.filter(
        #     date__year=year,
        #     checkpoint_id=checkpoint_id)
        #     .values('direction', 'date__month', 'car_type_id')
        #     .annotate(volume=Sum('volume'))
        #     .order_by('direction', 'date__month', 'car_type_id')
        # )
        sql_command = '''
            SELECT DIRECTION, EXTRACT( MONTH FROM CREATED_DATE ) AS CREATED_DATE, CAR_TYPE_ID, SUM(VOLUME) AS VOLUME FROM BMA_PHASE_II.RECORDS 
            WHERE EXTRACT(YEAR FROM CREATED_DATE) = '{}'
                AND CHECKPOINT_ID = {}
            GROUP BY DIRECTION, CREATED_DATE, CAR_TYPE_ID 
            ORDER BY DIRECTION, CREATED_DATE, CAR_TYPE_ID
        '''.format(
            year, 
            checkpoint_id
        )

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        columns = [row[0] for row in cursor.description]

        df = pd.DataFrame(data=data, columns=columns)
        df = df.rename(columns={
            "DIRECTION": "direction",
            "CREATED_DATE": "date__month",
            "CAR_TYPE_ID": "car_type_id",
            "VOLUME": "volume"
        })

        result = df.to_dict('records')

        return result

        return data


    def get_inbound_checkpoint_time_range(self, payload, checkpoint_id):
        sql_command = '''
            SELECT TIME_RANGE_ID, CREATED_DATE, SUM(VOLUME) AS VOLUME FROM BMA_PHASE_II.RECORDS
            WHERE CREATED_DATE = TO_DATE('{}', 'YYYY-MM-DD')
                AND TIME_RANGE_ID > {}
                AND TIME_RANGE_ID <= {}
                AND CHECKPOINT_ID = {}
                AND DIRECTION = 'IN'
            GROUP BY TIME_RANGE_ID, CREATED_DATE
            ORDER BY TIME_RANGE_ID, CREATED_DATE
        '''.format(
            payload['date'], 
            payload['start_time_id'], payload['end_time_id'],
            checkpoint_id
        )

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        columns = [row[0] for row in cursor.description]

        df = pd.DataFrame(data=data, columns=columns)
        df = df.rename(columns={
            "TIME_RANGE_ID": "time_range_id",
            "CREATED_DATE": "date",
            "VOLUME": "volume"
        })

        result = df.to_dict('records')

        return result


    def get_outbound_checkpoint_time_range(self, payload, checkpoint_id):
        sql_command = '''
            SELECT TIME_RANGE_ID, CREATED_DATE, SUM(VOLUME) AS VOLUME FROM BMA_PHASE_II.RECORDS
            WHERE CREATED_DATE = TO_DATE('{}', 'YYYY-MM-DD')
                AND TIME_RANGE_ID > {}
                AND TIME_RANGE_ID <= {}
                AND CHECKPOINT_ID = {}
                AND DIRECTION = 'OUT'
            GROUP BY TIME_RANGE_ID, CREATED_DATE
            ORDER BY TIME_RANGE_ID, CREATED_DATE
        '''.format(
            payload['date'], 
            payload['start_time_id'], payload['end_time_id'],
            checkpoint_id
        )

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        columns = [row[0] for row in cursor.description]

        df = pd.DataFrame(data=data, columns=columns)
        df = df.rename(columns={
            "TIME_RANGE_ID": "time_range_id",
            "CREATED_DATE": "date",
            "VOLUME": "volume"
        })

        result = df.to_dict('records')

        return result


    def get_outbound_time_range(self, payload):
        data = (RecordModel.objects.filter(
            date=payload['date'],
            time_range_id__gt=payload['start_time_id'],
            time_range_id__lte=payload['end_time_id'],
            direction='OUT'
            )
            .values('direction', 'time_range_id', 'date')
            .annotate(volume=Sum('volume'))
            .order_by()
        )

        return data


    def get_inbound_dashboard(self, payload):
        sql_command = '''
            SELECT DIRECTION, CHECKPOINT_ID, SUM(VOLUME) AS VOLUME FROM BMA_PHASE_II.RECORDS
            WHERE CREATED_DATE = TO_DATE('{}', 'YYYY-MM-DD')
                AND TIME_RANGE_ID > {}
                AND TIME_RANGE_ID <= {}
                AND DIRECTION = 'IN'
            GROUP BY DIRECTION, CHECKPOINT_ID
            ORDER BY DIRECTION, CHECKPOINT_ID
        '''.format(
            payload['date'], payload['start_time_id'], payload['end_time_id'],
        )

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        columns = [row[0] for row in cursor.description]

        df = pd.DataFrame(data=data, columns=columns)
        df = df.rename(columns={
            "DIRECTION": "direction",
            "CHECKPOINT_ID": 'checkpoint',
            "VOLUME": "volume"
        })
        df = df.sort_values(by=['checkpoint'])

        return df


    def get_outbound_dashboard(self, payload):
        sql_command = '''
            SELECT DIRECTION, CHECKPOINT_ID, SUM(VOLUME) AS VOLUME FROM BMA_PHASE_II.RECORDS
            WHERE CREATED_DATE = TO_DATE('{}', 'YYYY-MM-DD')
                AND TIME_RANGE_ID > {}
                AND TIME_RANGE_ID <= {}
                AND DIRECTION = 'OUT'
            GROUP BY DIRECTION, CHECKPOINT_ID
            ORDER BY DIRECTION, CHECKPOINT_ID
        '''.format(
            payload['date'], payload['start_time_id'], payload['end_time_id'],
        )

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        columns = [row[0] for row in cursor.description]

        df = pd.DataFrame(data=data, columns=columns)
        df = df.rename(columns={
            "DIRECTION": "direction",
            "CHECKPOINT_ID": 'checkpoint',
            "VOLUME": "volume"
        })
        df = df.sort_values(by=['checkpoint'])

        return df
    
    def get_total_count_type(self):
        sql_command = '''
            SELECT * AS total FROM BMA_PHASE_II.RECORDS
            WHERE CREATED_DATE = TO_DATE('{}', 'YYYY-MM-DD')
                AND TIME_RANGE_ID > {}
                AND TIME_RANGE_ID <= {}
        '''
        
        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
        print(data)
        # result = {}
        return 0