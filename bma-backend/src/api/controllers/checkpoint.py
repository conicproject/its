from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError, PermissionDenied

from api.validators.session import SessionValidator
from api.repositories.oracleCamera import OracleCameraRepository
from api.repositories.user import UserRepository
from api.validators.systemConfig import SystemConfigValidator
from api.repositories.oracleCheckpoint import OracleCheckpointRepository

class CheckpointViewSet(viewsets.ViewSet):

    def __init__(self):
        self.session_validator = SessionValidator()
        self.checkpoint_repo = OracleCheckpointRepository()
        self.camera_repo = OracleCameraRepository()
        self.system_config = SystemConfigValidator()
        self.user_repo = UserRepository()
        self.get_success_msg = 'request get data success'


    def get_all_active(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

        data = self.checkpoint_repo.get_all_active()

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)


    def get_all_detail(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

        data = self.checkpoint_repo.get_all_traffic_view()
        for i in range(len(data)):
            cameras = self.camera_repo.get_by_checkpoint(data[i]['id'])
            data[i]['cameras'] = cameras

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)

    def list_checkpoints(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

        data = self.checkpoint_repo.get_list_checkpoints()

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)

    def get_district(self,request):
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

        data = self.checkpoint_repo.get_district()
        
        response = {
                'status_code': 200,
                'message': 'get success',
                'data': data
            }

        return Response(response, status=status.HTTP_200_OK)

    def get_road(self,request):
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

        data = self.checkpoint_repo.get_road()
        
        response = {
                'status_code': 200,
                'message': 'get success',
                'data': data
            }

        return Response(response, status=status.HTTP_200_OK)

    def add_checkpoint(self, request):

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

        checkpoint = self.system_config.validate_request_add_checkpoint(
            params= request.data
        )

        dup_checkpoint = self.checkpoint_repo.check_dup_checkpoint(
            payloads= request.data
        )
        data = 'error'
        if dup_checkpoint != 0:
            response = {
                'status_code': 400,
                'message': 'checkpoint have been used'
            }

            raise ParseError(response)
        elif dup_checkpoint == 0:
            data = self.checkpoint_repo.insert_checkpoint(
                payloads=checkpoint
            )

        response = {
            'status_code': 200,
            'message': 'get success',
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)
    
    def edit_checkpoint(self, request):

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
        
        checkpoint = self.system_config.validate_request_edit_checkpoint(
            params= request.data
        )
        except_key = 'checkpoint_id'
        query_string = ''
        for key in checkpoint:
            if checkpoint[key] != '' and key not in except_key:
                if type(checkpoint[key]) == str:
                    query_string = query_string + "{} = '{}',".format(key,checkpoint[key])
                else:
                    query_string = query_string + "{} = {},".format(key,checkpoint[key])
            

        query_string = query_string[:-1]
        
        data = self.checkpoint_repo.edit_checkpoint(
            payloads=checkpoint,
            query=query_string
        )

        response = {
            'status_code': 200,
            'message': 'get success',
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)

    def list_road(self,request):
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

        data = self.checkpoint_repo.get_road()
        
        response = {
                'status_code': 200,
                'message': 'get success',
                'data': data
            }

        return Response(response, status=status.HTTP_200_OK)

    def add_road(self, request):

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

        road = self.system_config.validate_request_add_road(
            params= request.data
        )

        dup_road = self.checkpoint_repo.check_dup_road(
            payloads= request.data
        )
        data = 'error'
        if dup_road != 0:
            response = {
                'status_code': 400,
                'message': 'road id have been used'
            }

            raise ParseError(response)
        elif dup_road == 0:
            data = self.checkpoint_repo.insert_road(
                payloads=road
            )

        response = {
            'status_code': 200,
            'message': 'get success',
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)

    def edit_road(self, request):

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
        
        road = self.system_config.validate_request_edit_road(
            params= request.data
        )
        except_key = 'road_id'
        query_string = ''
        for key in road:
            if road[key] != '' and key not in except_key:
                if type(road[key]) == str:
                    query_string = query_string + "{} = '{}',".format(key,road[key])
                else:
                    query_string = query_string + "{} = {},".format(key,road[key])
            

        query_string = query_string[:-1]
        
        data = self.checkpoint_repo.edit_road(
            payloads=road,
            query=query_string
        )

        response = {
            'status_code': 200,
            'message': 'get success',
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)


    def list_lane(self,request):
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

        data = self.checkpoint_repo.get_lane()
        
        response = {
                'status_code': 200,
                'message': 'get success',
                'data': data
            }

        return Response(response, status=status.HTTP_200_OK)

    def add_lane(self, request):

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

        lane = self.system_config.validate_request_add_lane(
            params= request.data
        )

        dup_lane = self.checkpoint_repo.check_dup_lane(
            payloads= request.data
        )
        data = 'error'
        if dup_lane != 0:
            response = {
                'status_code': 400,
                'message': 'lane id have been used'
            }

            raise ParseError(response)
        elif dup_lane == 0:
            data = self.checkpoint_repo.insert_lane(
                payloads=lane
            )

        response = {
            'status_code': 200,
            'message': 'get success',
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)

    def edit_lane(self, request):

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
        
        lane = self.system_config.validate_request_edit_lane(
            params= request.data
        )
        except_key = 'lane_id'
        query_string = ''
        for key in lane:
            if lane[key] != '' and key not in except_key:
                if type(lane[key]) == str:
                    query_string = query_string + "{} = '{}',".format(key,lane[key])
                else:
                    query_string = query_string + "{} = {},".format(key,lane[key])
            

        query_string = query_string[:-1]
        
        data = self.checkpoint_repo.edit_lane(
            payloads=lane,
            query=query_string
        )

        response = {
            'status_code': 200,
            'message': 'get success',
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)
