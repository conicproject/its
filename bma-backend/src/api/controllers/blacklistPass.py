from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError, PermissionDenied

from api.validators.session import SessionValidator
from api.validators.feature import FeatureValidator
from api.validators.vehicle import VehicleValidator

from api.repositories.blacklist import BlacklistRepository
from api.repositories.user import UserRepository
from api.repositories.group import GroupRepository
from api.repositories.blacklistPassing import BlacklistPassingRepository
from api.repositories.hikCamera import HikCameraRepository
from api.repositories.SNMP import SNMPRepository

import math
import requests
import base64
import pandas as pd
from datetime import datetime


class BlacklistPassViewSet(viewsets.ViewSet):
    def __init__(self):
        self.session_validator = SessionValidator()
        self.feature_validator = FeatureValidator()
        self.vehicle_validator = VehicleValidator()

        self.blacklist_repo = BlacklistRepository()
        self.user_repo = UserRepository()
        self.group_repo = GroupRepository()
        self.blacklist_passing_repo = BlacklistPassingRepository()
        self.camera_repo = HikCameraRepository()
        self.snmp_status_repo = SNMPRepository()
        self.get_success_msg = 'request get data success'


    def get_search(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        # self.feature_validator.validate_vehicle_search(
        #     user_id=payloads['user_id']
        # )
        query_payload = self.vehicle_validator.validate_request_blacklist(
            params=request.query_params
        )
        page_data = self.vehicle_validator.validate_paginate(
            params=request.query_params
        )
        user = self.user_repo.get_by_id(id=payloads['user_id'])
        group = self.group_repo.get_by_id(id=user['group_id'])
        department_id = int(group['department_id'])

        blacklist_data = self.blacklist_repo.get_all_by_department(department_id=department_id)
        blacklist_ids = tuple([ data['id'] for data in blacklist_data ])

        if department_id != 1:
            if len(blacklist_ids) == 1:
                blacklist_ids = str(blacklist_ids)
                blacklist_ids = blacklist_ids.replace(',', '')

            if len(blacklist_ids) != 0:
                data = self.blacklist_passing_repo.search_blacklist(
                    payload=query_payload, page_data=page_data, blacklist_ids=blacklist_ids
                )
                total = self.blacklist_passing_repo.total_search_blacklist(
                    payload=query_payload, blacklist_ids=blacklist_ids
                )
            else:
                data = []
                total = 0
        else:
            data = self.blacklist_passing_repo.search_blacklist_master_group(
                payload=query_payload, page_data=page_data
            )
            total = self.blacklist_passing_repo.total_search_blacklist_master_group(
                payload=query_payload
            )

        page_total = math.ceil(total / page_data['page_size'])
        paginate_data = {
            'page': page_data['page'],
            'page_size': page_data['page_size'],
            'page_total': page_total
        }

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'page': paginate_data['page'],
            'page_size': paginate_data['page_size'],
            'page_total': paginate_data['page_total'],
            'total': total,
            'data': {
                'records': data,
                'total': len(data)
            }
        }

        return Response(response, status=status.HTTP_200_OK)


    def get_one(self, request, blacklist_passing_id):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        # self.feature_validator.validate_vehicle_search(
        #     user_id=payloads['user_id']
        # )
        user = self.user_repo.get_by_id(id=payloads['user_id'])
        group = self.group_repo.get_by_id(id=user['group_id'])
        department_id = int(group['department_id'])

        try:
            blacklist_passing_id = int(blacklist_passing_id)
        except:
            response = {
                'status_code': 400,
                'message': 'input type error'
            }

            raise ParseError(response)

        if department_id != 1:
            blacklist_data = self.blacklist_repo.get_all_by_department(department_id=department_id)
            blacklist_ids = tuple([ data['id'] for data in blacklist_data ])

            if len(blacklist_ids) == 1:
                blacklist_ids = str(blacklist_ids)
                blacklist_ids = blacklist_ids.replace(',', '')

            if len(blacklist_ids) != 0:
                self.blacklist_passing_repo.validate_blacklist_passing(
                    id=blacklist_passing_id, blacklist_ids=blacklist_ids
                )
            else:
                response = {
                    'status_code': 403,
                    'message': 'permission denied'
                }

                raise PermissionDenied(response)

        data = self.blacklist_passing_repo.get_by_id(
            id=blacklist_passing_id
        )

        response = {
            'status_code': 200,
            'message': 'request success',
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)


    def get_one_report(self, request, blacklist_passing_id):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        # self.feature_validator.validate_vehicle_search(
        #     user_id=payloads['user_id']
        # )
        user = self.user_repo.get_by_id(id=payloads['user_id'])
        group = self.group_repo.get_by_id(id=user['group_id'])
        department_id = int(group['department_id'])
        user_name = user['name']
        department_name = group['department_name']
        now = datetime.now()

        try:
            blacklist_passing_id = int(blacklist_passing_id)
        except:
            response = {
                'status_code': 400,
                'message': 'input type error'
            }

            raise ParseError(response)

        if department_id != 1:
            blacklist_data = self.blacklist_repo.get_all_by_department(department_id=department_id)
            blacklist_ids = tuple([ data['id'] for data in blacklist_data ])

            if len(blacklist_ids) == 1:
                blacklist_ids = str(blacklist_ids)
                blacklist_ids = blacklist_ids.replace(',', '')

            if len(blacklist_ids) != 0:
                self.blacklist_passing_repo.validate_blacklist_passing(
                    id=blacklist_passing_id, blacklist_ids=blacklist_ids
                )
            else:
                response = {
                    'status_code': 403,
                    'message': 'permission denied'
                }

                raise PermissionDenied(response)

        data = self.blacklist_passing_repo.get_by_id(
            id=blacklist_passing_id
        )

        data['user'] = user_name
        data['department'] = department_name
        data['report_date'] = now
        ## Handle device's connection 
        try:
            res_plate_pic = requests.get(data['plate_picture'], timeout=3)
            base64_plate_pic = base64.b64encode(res_plate_pic.content)
            data['base64_plate_pic'] = base64_plate_pic
        except:
            data['base64_plate_pic'] = None

        try:
            res_img_url = requests.get(data['image_url'], timeout=3)
            base64_img_pic = base64.b64encode(res_img_url.content)
            data['base64_image_pic'] = base64_img_pic
        except:
            data['base64_image_pic'] = None

        response = {
            'status_code': 200,
            'message': 'request success',
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)

    def check_blacklist(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        self.feature_validator.validate_vehicle_search(
            user_id=payloads['user_id']
        )

        hik_cameras = self.camera_repo.get_list()['response']['data']['list']
        list_deactive_camera_code = [camera['cameraIndexCode'] for camera in hik_cameras if camera['status'] == 0]

        ptrg_data = self.snmp_status_repo.get_all_sensor_status()
        list_deactive_ptrg_id = [df_snmp['objid'] for df_snmp in ptrg_data if df_snmp['status'] == 'Down']

        count = len(list_deactive_ptrg_id) + len(list_deactive_camera_code)

        ## make response
        response = {
            'status_code': 200,
            'message': 'request success',
            'data': self.blacklist_passing_repo.total_status_false(),
            'data_device': count
        }

        return Response(response, status=status.HTTP_200_OK)

    def update_status(self, request, id):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        self.feature_validator.validate_vehicle_search(
            user_id=payloads['user_id']
        )

        ## make response
        response = {
            'status_code': 200,
            'message': 'update success',
            'data': self.blacklist_passing_repo.update_status(id=id)
        }

        return Response(response, status=status.HTTP_200_OK)