from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from api.validators.session import SessionValidator

from api.repositories.oracleProvince import OracleProvinceRepository

class ProvinceViewSet(viewsets.ViewSet):

    def __init__(self):
        self.session_validator = SessionValidator()
        self.province_repo = OracleProvinceRepository()

        self.get_success_msg = 'request get data success'


    def get_all_name(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

        data = self.province_repo.get_list_name()

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)

    def get_all(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

        data = self.province_repo.list()

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)