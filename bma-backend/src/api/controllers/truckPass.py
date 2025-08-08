from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError, PermissionDenied
from django.forms.models import model_to_dict

from api.validators.session import SessionValidator
from api.validators.feature import FeatureValidator
from api.validators.vehicle import VehicleValidator

from api.repositories.truckPassing import TruckPassingRepository

from api.repositories.blacklist import BlacklistRepository
from api.repositories.user import UserRepository
from api.repositories.group import GroupRepository
from api.repositories.blacklistPassing import BlacklistPassingRepository
from api.repositories.oracleCheckpoint import OracleCheckpointRepository
from api.models.blacklistPassing import BlacklistPassingModel

import math
import requests
import base64
from datetime import datetime
from urllib.parse import urlparse

class TruckPassViewSet(viewsets.ViewSet):
    def __init__(self):
        self.session_validator = SessionValidator()
        self.feature_validator = FeatureValidator()
        self.vehicle_validator = VehicleValidator()

        self.truck_passing_repo = TruckPassingRepository()

        self.blacklist_repo = BlacklistRepository()
        self.user_repo = UserRepository()
        self.group_repo = GroupRepository()
        self.checkpoin_repo = OracleCheckpointRepository()
        self.blacklist_passing_repo = BlacklistPassingRepository()

        self.get_success_msg = 'request get data success'


    def get_search(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        self.feature_validator.validate_vehicle_search(
            user_id=payloads['user_id']
        )
        query_payload = self.vehicle_validator.validate_request_truck(
            params=request.query_params
        )
        page_data = self.vehicle_validator.validate_paginate(
            params=request.query_params
        )

        data = self.truck_passing_repo.search_truck(
            payload=query_payload, page_data=page_data
        )
        total = self.truck_passing_repo.total_search_truck(
            payload=query_payload
        )

        checkpoint = self.checkpoin_repo.get_ip_address()

        for i in range(len(data)):
            tr_data = data[i]

            my_dict = {}

            for j in range(len(checkpoint)):
                ch_data = checkpoint[j]

                bma_url_plate_parsed = ""
                net_url_plate_parsed = ""
                bma_url_image_parsed = ""
                net_url_image_parsed = ""

                if(ch_data["CHECKPOINT_NICKNAME"] == tr_data["checkpoint"]):

                    url_plate = tr_data["plate_picture"]
                    url_image = tr_data["image_url"]

                    url_plate_parsed = urlparse(url_plate)
                    url_image_parsed = urlparse(url_image)

                    if(bool(url_plate_parsed.scheme) == True):

                        bma_url_plate_parsed = url_plate_parsed._replace(netloc=ch_data["BMA_IP"]+":"+ch_data["BMA_RESPONSE_PORT"]).geturl()

                        net_url_plate_parsed = url_plate_parsed._replace(netloc=ch_data["NET_IP"]+":"+ch_data["NET_RESPONSE_PORT"]).geturl()

                    if(bool(url_image_parsed.scheme) == True):

                        bma_url_image_parsed = url_image_parsed._replace(netloc=ch_data["BMA_IP"]+":"+ch_data["BMA_RESPONSE_PORT"]).geturl()

                        net_url_image_parsed = url_image_parsed._replace(netloc=ch_data["NET_IP"]+":"+ch_data["NET_RESPONSE_PORT"]).geturl()

                    my_dict = {'bma_plate':bma_url_plate_parsed, 'bma_image' : bma_url_image_parsed, 'net_plate':net_url_plate_parsed, 'net_image' : net_url_image_parsed}

            data[i].update(my_dict)

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


    def get_one(self, request, truck_passing_id):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        self.feature_validator.validate_vehicle_search(
            user_id=payloads['user_id']
        )
        
        try:
            truck_passing_id = int(truck_passing_id)
        except:
            response = {
                'status_code': 400,
                'message': 'input type error'
            }

            raise ParseError(response)

        data = self.truck_passing_repo.get_by_id(
            id=truck_passing_id
        )
        # data = model_to_dict(data)
        data['plate_picture'] = data['plate_url']
        data['time'] = data['pass_time']

        del data['plate_url']
        del data['pass_time']

        response = {
            'status_code': 200,
            'message': 'request success',
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)


    def get_one_report(self, request, truck_passing_id):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        self.feature_validator.validate_vehicle_search(
            user_id=payloads['user_id']
        )
        user = self.user_repo.get_by_id(id=payloads['user_id'])
        group = self.group_repo.get_by_id(id=user['group_id'])
        user_name = user['name']
        department_name = group['department_name']
        now = datetime.now()

        try:
            truck_passing_id = int(truck_passing_id)
        except:
            response = {
                'status_code': 400,
                'message': 'input type error'
            }

            raise ParseError(response)

        checkpoint = self.checkpoin_repo.get_ip_address()
        
        data = self.truck_passing_repo.get_by_id(
            id=truck_passing_id
        )
        # data = model_to_dict(data)
        data['plate_picture'] = data['plate_url']
        data['time'] = data['pass_time']
        data['user'] = user_name
        data['department'] = department_name
        data['report_date'] = now

        my_dict = {}

        for j in range(len(checkpoint)):
            ch_data = checkpoint[j]

            bma_url_plate_parsed = ""
            net_url_plate_parsed = ""
            bma_url_image_parsed = ""
            net_url_image_parsed = ""

            if(ch_data["CHECKPOINT_NICKNAME"] == data["checkpoint"]):

                url_plate = data["plate_picture"]
                url_image = data["image_url"]

                url_plate_parsed = urlparse(url_plate)
                url_image_parsed = urlparse(url_image)

                if(bool(url_plate_parsed.scheme) == True):

                    bma_url_plate_parsed = url_plate_parsed._replace(netloc=ch_data["BMA_IP"]+":"+ch_data["BMA_RESPONSE_PORT"]).geturl()

                    net_url_plate_parsed = url_plate_parsed._replace(netloc=ch_data["NET_IP"]+":"+ch_data["NET_RESPONSE_PORT"]).geturl()

                if(bool(url_image_parsed.scheme) == True):

                    bma_url_image_parsed = url_image_parsed._replace(netloc=ch_data["BMA_IP"]+":"+ch_data["BMA_RESPONSE_PORT"]).geturl()

                    net_url_image_parsed = url_image_parsed._replace(netloc=ch_data["NET_IP"]+":"+ch_data["NET_RESPONSE_PORT"]).geturl()

                my_dict = {'bma_plate':bma_url_plate_parsed, 'bma_image' : bma_url_image_parsed, 'net_plate':net_url_plate_parsed, 'net_image' : net_url_image_parsed}

        data.update(my_dict)

        del data['plate_url']
        del data['pass_time']

        res_plate_pic = requests.get(data['bma_plate'])
        base64_plate_pic = base64.b64encode(res_plate_pic.content)

        res_img_url = requests.get(data['bma_image'])
        base64_img_pic = base64.b64encode(res_img_url.content)

        data['base64_plate_pic'] = base64_plate_pic
        data['base64_image_pic'] = base64_img_pic

        response = {
            'status_code': 200,
            'message': 'request success',
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)