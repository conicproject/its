from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed

from api.validators.session import SessionValidator
from api.validators.trafficDetail import TrafficDetailValidator

from api.repositories.user import UserRepository
from api.repositories.oracleCheckpoint import OracleCheckpointRepository

from api.logics.bkkReport import BkkReportLogic

class BkkReportViewSet(viewsets.ViewSet):

    def __init__(self):
        self.user_repo = UserRepository()
        self.checkpoint_repo = OracleCheckpointRepository()

        self.session_validator = SessionValidator()
        self.traffic_detail_validator = TrafficDetailValidator()
        self.bkk_report_logic = BkkReportLogic()


    def get_report(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        user = self.user_repo.get_by_id(id=payloads['user_id'])
        group_id = user["group_id"]
        is_super_user = user["is_super_user"]

        if (group_id != 1) or (is_super_user != True):
            response = {
                'status_code': 403,
                'message': 'permission denied'
            }

            raise AuthenticationFailed(response)
        
        type_, datetime_value = self.traffic_detail_validator.validate_report_request(
            params=request.query_params
        )
        checkpoints = self.checkpoint_repo.get_all_active_report()

        report_data = []

        for checkpoint in checkpoints:
            response = self.bkk_report_logic.get_data(
                type=type_, datetime_value=datetime_value, checkpoint_id=checkpoint['id']
            )
            response['checkpoint'] = checkpoint
           
            report_data.append(response)
        
        response = {
            'status_code': 200,
            'message': 'request success',
            'data': report_data
        }

        return Response(response, status=status.HTTP_200_OK)