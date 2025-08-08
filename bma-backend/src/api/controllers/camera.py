from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError, PermissionDenied

from api.validators.session import SessionValidator
from api.repositories.oracleCamera import OracleCameraRepository
from api.repositories.user import UserRepository
from api.validators.systemConfig import SystemConfigValidator

class CameraViewSet(viewsets.ViewSet):
    def __init__(self):
        self.session_validator = SessionValidator()
        self.camera_repo = OracleCameraRepository()
        self.user_repo = UserRepository()
        self.system_config = SystemConfigValidator()
        self.get_success_msg = 'request get data success'

    def list_cameras(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

        check_user = self.user_repo.get_by_id(id=payloads['user_id'])
        
        is_super_user = check_user['is_super_user']
        
        if not is_super_user:
            response = {
                'status_code': 403,
                'message': 'permission denied'
            }

            raise PermissionDenied(response)


        data = self.camera_repo.get_list_cameras()

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)

    def get_checkpoints(self,request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

        check_user = self.user_repo.get_by_id(id=payloads['user_id'])
        
        is_super_user = check_user['is_super_user']
        
        if not is_super_user:
            response = {
                'status_code': 403,
                'message': 'permission denied'
            }

            raise PermissionDenied(response)

        data = self.camera_repo.get_checkpoints()
        
        response = {
                'status_code': 200,
                'message': 'get success',
                'data': data
            }

        return Response(response, status=status.HTTP_200_OK)

    def add_camera(self, request):

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

        camera = self.system_config.validate_request_add_camera(
            params= request.data
        )

        dup_camera = self.camera_repo.check_dup_camera(
            payloads= request.data
        )
        data = 'error'
        if dup_camera != 0:
            response = {
                'status_code': 400,
                'message': 'camera id have been used'
            }

            raise ParseError(response)
        elif dup_camera == 0:
            data = self.camera_repo.insert_camera(
                payloads=camera
            )

        response = {
            'status_code': 200,
            'message': 'get success',
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)

    def edit_camera(self, request):

        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

       
        check_user = self.user_repo.get_by_id(id=payloads['user_id'])
        
        is_super_user = check_user['is_super_user']
        
        if not is_super_user:
            response = {
                'status_code': 403,
                'message': 'permission denied'
            }

            raise PermissionDenied(response)
        
        camera = self.system_config.validate_request_edit_camera(
            params= request.data
        )
        except_key = 'camera_id'
        query_string = ''
        for key in camera:
            if camera[key] != '' and key not in except_key:
                if type(camera[key]) == str:
                    query_string = query_string + "{} = '{}',".format(key,camera[key])
                else:
                    query_string = query_string + "{} = {},".format(key,camera[key])
            

        query_string = query_string[:-1]
        
        data = self.camera_repo.edit_camera(
            payloads=camera,
            query=query_string
        )

        response = {
            'status_code': 200,
            'message': 'get success',
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)

        
    