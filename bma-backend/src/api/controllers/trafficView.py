from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from api.validators.session import SessionValidator
from api.validators.feature import FeatureValidator
from api.validators.trafficView import TrafficViewValidator

from api.repositories.oracleCheckpoint import OracleCheckpointRepository
from api.logics.trafficView import TrafficViewLogic


class TrafficViewViewSet(viewsets.ViewSet):
    def __init__(self):
        self.session_validator = SessionValidator()
        self.feature_validator = FeatureValidator()
        self.traffic_view_validator = TrafficViewValidator()

        self.checkpoint_repo = OracleCheckpointRepository()
        self.traffic_view_logic = TrafficViewLogic()

        self.get_success_msg = 'request get data success'


    def get_all_current_traffic(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        self.feature_validator.validate_traffic_view(
            user_id=payloads['user_id']
        )

        data = self.checkpoint_repo.get_all_traffic_view()
        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)


    def get_live_view_sample(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        self.feature_validator.validate_traffic_view(
            user_id=payloads['user_id']
        )
        checkpoint_id = self.traffic_view_validator.validate_request_sample(
            params=request.query_params
        )

        # rstp_url, camera_code = self.traffic_view_logic.get_sample_live_view(
        #     checkpoint_id=checkpoint_id
        # )
        # checkpoint_data = self.checkpoint_repo.get_by_id(
        #     id=checkpoint_id
        # )

        if 'code_id' not in request.query_params:
            rstp_url, camera_code = self.traffic_view_logic.get_sample_live_view(
                checkpoint_id=checkpoint_id
            )
        else:
            rstp_url, camera_code = self.traffic_view_logic.get_sample_live_view_by_id(
                camera_id=request.query_params.get('code_id')
            )
        
        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': {
                'camera_code': camera_code,
                'url': rstp_url
            }
        }

        return Response(response, status=status.HTTP_200_OK)


    def get_live_view(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        self.feature_validator.validate_traffic_view(
            user_id=payloads['user_id']
        )
        checkpoint_id, camera_code = self.traffic_view_validator.validate_request(
            params=request.query_params
        )

        rstp_url, camera_code = self.traffic_view_logic.get_live_view(
            checkpoint_id=checkpoint_id, camera_code=camera_code
        )
        checkpoint_data = self.checkpoint_repo.get_by_id(
            id=checkpoint_id
        )

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': {
                'camera_code': camera_code,
                'url': rstp_url,
                'checkpoint': checkpoint_data
            }
        }

        return Response(response, status=status.HTTP_200_OK)


    def get_checkpoint_cameras(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        checkpoint_id = self.traffic_view_validator.validate_request_sample(
            params=request.query_params
        )

        cameras = self.traffic_view_logic.get_checkpoint_cameras(
            checkpoint_id=checkpoint_id
        )
        checkpoint_detail = self.checkpoint_repo.get_by_id(id=checkpoint_id)

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': {
                'checkpoint': checkpoint_detail,
                'cameras': cameras
            }
        }

        return Response(response, status=status.HTTP_200_OK)


    def get_playback_checkpoint_camera(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        self.feature_validator.validate_traffic_view(
            user_id=payloads['user_id']
        )
        checkpoint_id, camera_code, start_time, end_time = self.traffic_view_validator.validate_request_playback(
            params=request.query_params
        )

        rstp_url, camera_code = self.traffic_view_logic.get_playback_view(
            checkpoint_id=checkpoint_id, camera_code=camera_code,
            start_time=start_time, end_time=end_time
        )

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': {
                'camera_code': camera_code,
                'url': rstp_url
            }
        }

        return Response(response, status=status.HTTP_200_OK)