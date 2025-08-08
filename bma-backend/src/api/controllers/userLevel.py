from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from api.validators.session import SessionValidator

from api.repositories.userLevel import userLevel

class userLevelViewSet(viewsets.ViewSet):
    
    def __init__(self):
        
        self.session_validator = SessionValidator()
        
        self.userLevel_repo = userLevel()

        self.get_success_msg = 'request get data success'

    
    def get_all_name(self, request):

        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

        data = self.userLevel_repo.get_list_user_level()
        
        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': data
        }
        
        return Response(response, status=status.HTTP_200_OK)