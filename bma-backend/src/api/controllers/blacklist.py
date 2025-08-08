from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied

import pandas as pd

from api.validators.session import SessionValidator
from api.validators.feature import FeatureValidator
from api.validators.blacklist import BlacklistValidator
from api.validators.vehicle import VehicleValidator
from api.repositories.blacklist import BlacklistRepository
from api.repositories.user import UserRepository
from api.repositories.group import GroupRepository
from api.serializers.blacklist import BlacklistSerializer

class BlacklistViewSet(viewsets.ViewSet):
    def __init__(self):
        self.session_validator = SessionValidator()
        self.feature_validator = FeatureValidator()
        self.blacklist_validator = BlacklistValidator()
        self.vehicle_validator = VehicleValidator()
        self.blacklist_repo = BlacklistRepository()
        self.user_repo = UserRepository()
        self.group_repo = GroupRepository()
        self.blacklist_srz = BlacklistSerializer

        self.get_success_msg = 'request get data success'


    def get_all(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

        page_data = self.vehicle_validator.validate_paginate(
            params=request.query_params
        )

        ##### DO NOT DELETE VALIDATE FEATURE #####
        # self.feature_validator.validate_vehicle_search(
        #     user_id=payloads['user_id']
        # )

        user = self.user_repo.get_by_id(id=payloads['user_id'])
        group = self.group_repo.get_by_id(id=user['group_id'])
        department_id = int(group['department_id'])
        total_blacklist = self.blacklist_repo.get_total()
        if department_id == 1:
            data,paginate_data = self.blacklist_repo.get_all_config(page_data=page_data,total =total_blacklist[0][0])
        else:
            data,paginate_data = self.blacklist_repo.get_all_by_department_config(department_id=department_id,page_data=page_data,total =total_blacklist[0][0])

        df = pd.DataFrame(data)

        if not df.empty:
            df['is_editable'] = (df['department_id'] == department_id)
            df['is_deletable'] = (df['department_id'] == department_id)
            df = df.drop(columns=['department_id'])

        response_data = df.to_dict('records')

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'page': paginate_data['page'],
            'page_size': paginate_data['page_size'],
            'page_total': paginate_data['page_total'],
            'total': total_blacklist[0][0],
            'data': response_data
        }

        return Response(response, status=status.HTTP_200_OK)


    def create(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

        ##### DO NOT DELETE VALIDATE FEATURE #####
        # self.feature_validator.validate_vehicle_search(
        #     user_id=payloads['user_id']
        # )

        query_payload = self.blacklist_validator.validate_request(
            params=request.data
        )
        user = self.user_repo.get_by_id(id=payloads['user_id'])
        group = self.group_repo.get_by_id(id=user['group_id'])
        department_id = int(group['department_id'])

        data = self.blacklist_repo.insert(
            payloads=query_payload, department_id=department_id
        )

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)


    def update(self, request, blacklist_id):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

        ##### DO NOT DELETE VALIDATE FEATURE #####
        # self.feature_validator.validate_vehicle_search(
        #     user_id=payloads['user_id']
        # )

        query_payload = self.blacklist_validator.validate_request(
            params=request.data
        )
        self.blacklist_validator.validate_blacklist_id(id=blacklist_id)
        blacklist_data = self.blacklist_repo.is_exist(id=blacklist_id)

        user = self.user_repo.get_by_id(id=payloads['user_id'])
        group = self.group_repo.get_by_id(id=user['group_id'])
        department_id = int(group['department_id'])

        if department_id != blacklist_data['department_id']:
            response = {
                'status_code': 403,
                'message': 'permission denied'
            }

            raise PermissionDenied(response)

        data = self.blacklist_repo.update(
            id=blacklist_id ,payloads=query_payload
        )

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)


    def delete(self, request, blacklist_id):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

        ##### DO NOT DELETE VALIDATE FEATURE #####
        # self.feature_validator.validate_vehicle_search(
        #     user_id=payloads['user_id']
        # )

        self.blacklist_validator.validate_blacklist_id(id=blacklist_id)
        blacklist_data = self.blacklist_repo.is_exist(id=blacklist_id)

        user = self.user_repo.get_by_id(id=payloads['user_id'])
        group = self.group_repo.get_by_id(id=user['group_id'])
        department_id = int(group['department_id'])

        if department_id != blacklist_data['department_id']:
            response = {
                'status_code': 403,
                'message': 'permission denied'
            }

            raise PermissionDenied(response)

        self.blacklist_repo.delete(id=blacklist_id)

        response = {
            'status_code': 200,
            'message': self.get_success_msg
        }

        return Response(response, status=status.HTTP_200_OK)
