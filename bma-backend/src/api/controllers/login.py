from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from api.repositories.login import LoginRepository
from api.logics.session import SessionLogic
from api.repositories.blacklistPassing import BlacklistPassingRepository
from api.validators.login import LoginValidator
from api.serializers.login import LoginSessionSerializer
import datetime

class LoginViewSet(viewsets.ViewSet):

    def __init__(self):
        self.login_repo = LoginRepository()
        self.login_validator = LoginValidator()
        self.sesion_interface = SessionLogic()
        self.login_session_srz = LoginSessionSerializer
        self.blacklist_passing_repo = BlacklistPassingRepository()
        self.login_success_msg = 'request success'


    def auth(self, request):
        ## validate
        print("Request data:", request.data)
        user = self.login_validator.validate(payloads=request.data)

        ## query & format
        now = datetime.datetime.now()
        now_date = now.strftime('%Y-%m-%d')
        data = self.login_repo.stamp_login(user_id=user['id'])
        serializer = self.login_session_srz(data)
        session = self.sesion_interface.get_session(payloads=serializer.data)
        self.blacklist_passing_repo.update_status_previous_date(now=now_date)

        ## make response
        response = {
            'status_code': 200,
            'message': self.login_success_msg,
            'data': session,
            'count_notification':self.blacklist_passing_repo.total_status_false()
        }

        return Response(response, status=status.HTTP_200_OK)