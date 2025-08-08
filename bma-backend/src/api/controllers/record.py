from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from api.logics.dashboard import DashboardLogic
from api.logics.checkpointDetail import CheckpointDetailLogic

from api.validators.session import SessionValidator
from api.validators.feature import FeatureValidator
from api.validators.checkpointDetail import CheckpointDetailValidator
from api.validators.trafficDetail import TrafficDetailValidator

from api.logics.trafficDetail import TrafficDetailLogic
from api.repositories.oracleCheckpoint import OracleCheckpointRepository
from api.repositories.oracleCamera import OracleCameraRepository
from api.repositories.record import RecordRepository

from datetime import datetime, timedelta
from django.utils.timezone import now

from django.core.cache import cache

class RecordViewSet(viewsets.ViewSet):

    def __init__(self):
        self.session_validator = SessionValidator()
        self.feature_validator = FeatureValidator()

        self.dashboard_logic = DashboardLogic()

        self.checkpoint_repo = OracleCheckpointRepository()
        self.camera_repo = OracleCameraRepository()

        self.checkpoint_detail_validator = CheckpointDetailValidator()
        self.checkpoint_detail_logic = CheckpointDetailLogic()

        self.traffic_detail_validator = TrafficDetailValidator()
        self.traffic_detail_logic = TrafficDetailLogic()

        self.record_repo = RecordRepository()

        self.get_success_msg = 'request get data success'


    def get_dashboard_data(self, request):
        # validate
        payloads = self.session_validator.validate_session(headers=request.headers)
        self.feature_validator.validate_dashboard(user_id=payloads['user_id'])
        key, timeout = 'dashboard_data_cache', 60 * 15
        cached = cache.get(key)

        if cached and now() < cached.get('_expiry_time', now()):
            print("✅ cache ใช้งานได้", int((cached['_expiry_time'] - now()).total_seconds()))
            return Response(cached['response'], status=status.HTTP_200_OK)
            
        print("🕒 ดึงข้อมูลใหม่")
        data = {
            'checkpoint_total': self.checkpoint_repo.get_count_all(),
            'camera_total': self.camera_repo.get_count_all(),
            'total': self.dashboard_logic.get_total(),
            'direction': self.dashboard_logic.get_direction_volume(),
            'top_rank': self.dashboard_logic.get_top_rank(),
            'graph': self.dashboard_logic.get_graph_data(),
            'total_violation': self.dashboard_logic.get_violation_total(),
            'direction_violation': self.dashboard_logic.get_direction_violation_volume(),
            'top_rank_violation': self.dashboard_logic.get_top_violation_rank(),
            'graph_violation': self.dashboard_logic.get_violation_graph_data(),
            'get_cartype_data': self.checkpoint_detail_logic.get_cartype_all_data(),
        }

        res = {'status_code': 200, 'message': self.get_success_msg, 'data': data}
        cache.set(key, {'response': res, '_expiry_time': now() + timedelta(seconds=timeout)}, timeout)
        return Response(res, status=status.HTTP_200_OK)
        
    def get_dashboard_data_test(self, request):

        response = {
            'get_cartype_data': self.checkpoint_detail_logic.get_cartype_all_data(),

        }
        return Response(response, status=status.HTTP_200_OK)

    def get_dashboard_data_scheduler(self, request):
        ## validate
        # payloads = self.session_validator.validate_session(
        #     headers=request.headers
        # )
        # self.feature_validator.validate_dashboard(
        #     user_id=payloads['user_id']
        # )
        cache_key = 'dashboard_data_cache'
        cache_timeout = 60* 15

        cached_response = cache.get(cache_key)
        if cached_response:
            return Response(cached_response, status=status.HTTP_200_OK)
        ## query & format
        total_checkpoint = self.checkpoint_repo.get_count_all()
        total_camera = self.camera_repo.get_count_all()
        total_data = self.dashboard_logic.get_total()
        direction_data = self.dashboard_logic.get_direction_volume()
        graph_data = self.dashboard_logic.get_graph_data()
        top_rank_data = self.dashboard_logic.get_top_rank()
        total_violation_data = self.dashboard_logic.get_violation_total()
        direction_violation_data = self.dashboard_logic.get_direction_violation_volume()
        graph_violation_data = self.dashboard_logic.get_violation_graph_data()
        top_rank_violation_data = self.dashboard_logic.get_top_violation_rank()

        ## make response
        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': {
                'checkpoint_total': total_checkpoint,
                'camera_total': total_camera,
                'total': total_data,
                'direction': direction_data,
                'top_rank': top_rank_data,
                'graph': graph_data,
                'total_violation': total_violation_data,
                'direction_violation': direction_violation_data,
                'top_rank_violation': top_rank_violation_data,
                'graph_violation': graph_violation_data
            }
        }

        cache.set(cache_key, response, timeout=cache_timeout)

        return Response(response, status=status.HTTP_200_OK)


    def get_checkpoint_detail(self, request, checkpoint_id,type):
        ## validate
        checkpoint_id = self.checkpoint_detail_validator.validate_checkpoint_id(
            checkpoint_id=checkpoint_id
        )
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        cache_key = f'checkpoint_detail{checkpoint_id}'
        cache_timeout = 60* 45

        cached_response = cache.get(cache_key)
        # if cached_response:
        #     return Response(cached_response, status=status.HTTP_200_OK)
        # self.feature_validator.validate_checkpoint(
        #     user_id=payloads['user_id']
        # )

        ## query & format
        cameras_status = self.checkpoint_detail_logic.get_total_cameras_status(checkpoint_id=checkpoint_id)
        checkpoint_detail = self.checkpoint_detail_logic.get_checkpoint_detail(checkpoint_id=checkpoint_id)
        total_data,total_record = self.checkpoint_detail_logic.get_total(checkpoint_id=checkpoint_id, type=type)
        direction_data = self.checkpoint_detail_logic.get_direction_volume(checkpoint_id=checkpoint_id, type=type)
        time_serie_data = self.checkpoint_detail_logic.get_graph_data(checkpoint_id=checkpoint_id, type=type)
        cartype_total = self.checkpoint_detail_logic.get_cartype_data(checkpoint_id=checkpoint_id, type=type)

        ## make response
        if(type == '1'):
            response = {
                'status_code': 200,
                'message': self.get_success_msg,
                'data': {
                    'checkpoint': checkpoint_detail,
                    'cameras_status': cameras_status,
                    'total': total_data,
                    'direction': direction_data,
                    'car_type': cartype_total,
                    'graph': time_serie_data,
                    'graph_inside' : {
                        'violation': (total_data/total_record)*100,
                        'normal': 100 - ((total_data/total_record)*100)
                    }
                }
            }
        elif(type == '0'):    
            response = {
                'status_code': 200,
                'message': self.get_success_msg,
                'data': {
                    'checkpoint': checkpoint_detail,
                    'cameras_status': cameras_status,
                    'total': total_data,
                    'direction': direction_data,
                    'car_type': cartype_total,
                    'graph': time_serie_data
                }
            }
        cache.set(cache_key, response, timeout=cache_timeout)
        return Response(response, status=status.HTTP_200_OK)

    def get_checkpoint_detail_scheduler(self, request, checkpoint_id,type):
        ## validate
        checkpoint_id = self.checkpoint_detail_validator.validate_checkpoint_id(
            checkpoint_id=checkpoint_id
        )
        # payloads = self.session_validator.validate_session(
        #     headers=request.headers
        # )
        cache_key = f'checkpoint_detail{checkpoint_id}'
        cache_timeout = 60* 45

        # cached_response = cache.get(cache_key)
        # if cached_response:
        #     return Response(cached_response, status=status.HTTP_200_OK)
        # self.feature_validator.validate_checkpoint(
        #     user_id=payloads['user_id']
        # )

        ## query & format
        cameras_status = self.checkpoint_detail_logic.get_total_cameras_status(checkpoint_id=checkpoint_id)
        checkpoint_detail = self.checkpoint_detail_logic.get_checkpoint_detail(checkpoint_id=checkpoint_id)
        total_data,total_record = self.checkpoint_detail_logic.get_total(checkpoint_id=checkpoint_id, type=type)
        direction_data = self.checkpoint_detail_logic.get_direction_volume(checkpoint_id=checkpoint_id, type=type)
        time_serie_data = self.checkpoint_detail_logic.get_graph_data(checkpoint_id=checkpoint_id, type=type)
        cartype_total = self.checkpoint_detail_logic.get_cartype_data(checkpoint_id=checkpoint_id, type=type)

        ## make response
        if(type == '1'):
            response = {
                'status_code': 200,
                'message': self.get_success_msg,
                'data': {
                    'checkpoint': checkpoint_detail,
                    'cameras_status': cameras_status,
                    'total': total_data,
                    'direction': direction_data,
                    'car_type': cartype_total,
                    'graph': time_serie_data,
                    'graph_inside' : {
                        'violation': (total_data/total_record)*100,
                        'normal': 100 - ((total_data/total_record)*100)
                    }
                }
            }
        elif(type == '0'):    
            response = {
                'status_code': 200,
                'message': self.get_success_msg,
                'data': {
                    'checkpoint': checkpoint_detail,
                    'cameras_status': cameras_status,
                    'total': total_data,
                    'direction': direction_data,
                    'car_type': cartype_total,
                    'graph': time_serie_data
                }
            }
        cache.set(cache_key, response, timeout=cache_timeout)
        return Response(response, status=status.HTTP_200_OK)


    def get_traffic_detail(self, request,record_type):
        ## validate
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        # self.feature_validator.validate_traffic_detail(
        #     user_id=payloads['user_id']
        # )
        type_, datetime_value, checkpoint_id = self.traffic_detail_validator.validate_request(
            params=request.query_params
        )

        response = self.traffic_detail_logic.get_data(
            type=type_, datetime_value=datetime_value, checkpoint_id=checkpoint_id,record_type = record_type
        )
        checkpoint_detail = self.traffic_detail_logic.get_checkpoint_detail(
            checkpoint_id=checkpoint_id
        )
        response['checkpoint'] = checkpoint_detail

        return Response(response, status=status.HTTP_200_OK)

    def get_record_url(self, request):
        # payloads = self.session_validator.validate_session(
        #     headers=request.headers
        # )

        response = self.checkpoint_repo.get_record_url()
    
        return Response(response, status=status.HTTP_200_OK)


