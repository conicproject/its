from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError, PermissionDenied
import datetime
import threading

from api.connections.oracle import OracleConnection

from api.validators.session import SessionValidator
from api.repositories.oracleCamera import OracleCameraRepository
from api.repositories.user import UserRepository
from api.validators.systemConfig import SystemConfigValidator
from api.repositories.manualInsert import OracleManualInsertRepository

class ManualViewSet(viewsets.ViewSet):
    def __init__(self):
        self.session_validator = SessionValidator()
        self.camera_repo = OracleCameraRepository()
        self.user_repo = UserRepository()
        self.system_config = SystemConfigValidator()
        self.manual_config = OracleManualInsertRepository()
        self.get_success_msg = 'request get data success'

    def record_insert(self,request):

        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

       
        user = self.user_repo.get_by_id(id=payloads['user_id'])
        
        is_super_user = user['is_super_user']
        
        if not is_super_user:
            response = {
                'status_code': 403,
                'message': 'permission denied'
            }

            raise PermissionDenied(response)
        time_validate = self.system_config.validate_time_format(
            params= request.data
        )
        startdate = str(time_validate['starttime'])
        enddate = str(time_validate['endtime'])
        record = threading.Thread(target= self.process_daily_record_insert,args=[startdate,enddate])
        record.start()
        # subprocess.run(['python','./api/logics/dailyinsert.py','--startdate',startdate,'--enddate',enddate])
        response = {
            'status_code': 200,
            'message': 'get success',
            'data': 'success'
        }

        return Response(response, status=status.HTTP_200_OK)

    def violation_insert(self,request):

        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

       
        user = self.user_repo.get_by_id(id=payloads['user_id'])
        
        is_super_user = user['is_super_user']
        
        if not is_super_user:
            response = {
                'status_code': 403,
                'message': 'permission denied'
            }

            raise PermissionDenied(response)
        time_validate = self.system_config.validate_time_format(
            params= request.data
        )
        startdate = str(time_validate['starttime'])
        enddate = str(time_validate['endtime'])
        record = threading.Thread(target= self.process_daily_violation_insert,args=[startdate,enddate])
        record.start()
        # subprocess.run(['python','./api/logics/dailyinsert.py','--startdate',startdate,'--enddate',enddate])
        response = {
            'status_code': 200,
            'message': 'get success',
            'data': 'success'
        }

        return Response(response, status=status.HTTP_200_OK)

    def process_daily_record_insert(self,startdate,enddate):
        start_str = startdate
        end_str = enddate
        format_ = '%Y-%m-%d'

        starting_datetime = datetime.datetime.strptime(start_str, format_)
        # end_datetime = datetime.datetime.strptime(end_str, format_)
        end_datetime = datetime.datetime.strptime(end_str, format_) + datetime.timedelta(days=1)

        diff = end_datetime - starting_datetime
        loop_round = diff // datetime.timedelta(minutes=5)
        delete_st_date = starting_datetime.strftime('%Y-%m-%d')
        delete_end_date = end_datetime.strftime('%Y-%m-%d')
        self.manual_config.delete_record(startdate=delete_st_date,enddate=delete_end_date)

        for i in range(loop_round):

            start_datetime = starting_datetime + datetime.timedelta(
                minutes=i*5
            )

            end_datetime = starting_datetime + datetime.timedelta(
                minutes=(i+1)*5
            )

            hm_now = end_datetime.strftime('%H:%M')
            time_range = self.manual_config.get_time_range_by_end_time(time=hm_now)

            time_range_id = time_range[0]
            start_timestamp = start_datetime.strftime('%Y-%m-%d %H:%M:%S')
            end_timestamp = end_datetime.strftime('%Y-%m-%d %H:%M:%S')

            vehicle_data = self.manual_config.get_by_timeStamp_routine(
                start_timestamp=start_timestamp,
                end_timestamp=end_timestamp
            )

            date_stamp = start_datetime.date()
            
            insert_sql_command = self.manual_config.get_insert_manual_command(
                data=vehicle_data['data'], columes=vehicle_data['columes'],
                date=date_stamp, time_range_id=time_range_id
            )
            # print(insert_sql_command)
            connection = OracleConnection().get_connection()
            cursor = connection.cursor()

            cursor.execute(insert_sql_command)
            connection.commit()

    def process_daily_violation_insert(self,startdate,enddate):
        start_str = startdate
        end_str = enddate


        
        format_ = '%Y-%m-%d'

        starting_datetime = datetime.datetime.strptime(start_str, format_)
        end_datetime = datetime.datetime.strptime(end_str, format_)  +  datetime.timedelta(days=1)

        diff = end_datetime - starting_datetime
        loop_round = diff // datetime.timedelta(minutes=5)
        delete_st_date = starting_datetime.strftime('%Y-%m-%d')
        delete_end_date = end_datetime.strftime('%Y-%m-%d')
        self.manual_config.delete_violation(startdate=delete_st_date,enddate=delete_end_date)

        for i in range(loop_round):

            start_datetime = starting_datetime + datetime.timedelta(
                minutes=i*5
            )

            end_datetime = starting_datetime + datetime.timedelta(
                minutes=(i+1)*5
            )

            hm_now = end_datetime.strftime('%H:%M')
            time_range = self.manual_config.get_time_range_by_end_time(time=hm_now)

            time_range_id = time_range[0]
            start_timestamp = start_datetime.strftime('%Y-%m-%d %H:%M:%S')
            end_timestamp = end_datetime.strftime('%Y-%m-%d %H:%M:%S')

            vehicle_data = self.manual_config.get_by_timeStamp_violation_routine(
                start_timestamp=start_timestamp,
                end_timestamp=end_timestamp
            )

            date_stamp = start_datetime.date()
            
            insert_sql_command = self.manual_config.get_insert_violation_manual_command(
                data=vehicle_data['data'], columes=vehicle_data['columes'],
                date=date_stamp, time_range_id=time_range_id
            )
            # print(insert_sql_command)
            connection = OracleConnection().get_connection()
            cursor = connection.cursor()

            cursor.execute(insert_sql_command)
            connection.commit()
