from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError, PermissionDenied

from api.validators.session import SessionValidator
from api.validators.feature import FeatureValidator
from api.validators.vehicle import VehicleValidator

from api.repositories.oracleVehiclePass import OracleVehiclePassRepository
from api.repositories.oracleCheckpoint import OracleCheckpointRepository
from api.repositories.oracleProvince import OracleProvinceRepository
from api.repositories.oracleVehicleColor import OracleVehicleColorRepository
from api.repositories.oracleVehicleType import OracleVehicleTypeRepository
from api.repositories.user import UserRepository
from api.repositories.group import GroupRepository

from urllib.parse import urlparse
import requests
import base64
from datetime import datetime, timedelta
import pandas as pd

class VehiclePassViewSet(viewsets.ViewSet):

    def __init__(self):
        self.session_validator = SessionValidator()
        self.feature_validator = FeatureValidator()
        self.vehicle_validator = VehicleValidator()

        self.vehicle_pass_repo = OracleVehiclePassRepository()
        self.checkpoin_repo = OracleCheckpointRepository()
        self.province_repo = OracleProvinceRepository()
        self.vehicle_color_repo = OracleVehicleColorRepository()
        self.vehicle_type_repo = OracleVehicleTypeRepository()
        self.user_repo = UserRepository()
        self.group_repo = GroupRepository()
        self.get_success_msg = 'request get data success'

    def get_report_detail(self, request):
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

        data = request.data

        data['user'] = user_name
        data['department'] = department_name

        for i in range(len(data)):
            tr_data = data

            my_dict = {}
            base64_plate_pic = ""
            base64_image_pic = ""
            now = datetime.now()

            url_plate = tr_data["picture"]
            url_plate_parsed = urlparse(url_plate)
            url_image = tr_data["image_url"]
            url_image_parsed = urlparse(url_image)

            if(bool(url_plate_parsed.scheme) == True):
                res = requests.get(url_plate)
                base64_plate_pic = base64.b64encode(res.content)
                base64_plate_pic = base64_plate_pic.decode('utf-8')
            else:
                base64_plate_pic = "R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="
                
            if(bool(url_image_parsed.scheme) == True):
                res = requests.get(url_image)
                base64_image_pic = base64.b64encode(res.content)
                base64_image_pic = base64_image_pic.decode('utf-8')
            else:
                base64_image_pic = "R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="

            my_dict = {'img_base64': 'data:image/png;base64,'+base64_plate_pic, 'img_overview_base64': 'data:image/png;base64,'+base64_image_pic, 'report_date': now}

            data.update(my_dict)


        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': {
                'records': data,
                # 'total': len(data)
            }
        }

        return Response(response, status=status.HTTP_200_OK)

    def get_report(self, request):

        data = request.data

        for i in range(len(data)):
            tr_data = data[i]

            my_dict = {}
            base64_plate_pic = ""

            url_plate = tr_data["picture"]
            url_plate_parsed = urlparse(url_plate)

            if(bool(url_plate_parsed.scheme) == True):
                res = requests.get(url_plate)
                base64_plate_pic = base64.b64encode(res.content)
                base64_plate_pic = base64_plate_pic.decode('utf-8')
            else:
                base64_plate_pic = "R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="

            my_dict = {'img_base64': 'data:image/png;base64,'+base64_plate_pic}

            data[i].update(my_dict)


        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': {
                'records': data,
                # 'total': len(data)
            }
        }

        return Response(response, status=status.HTTP_200_OK)

    def search(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        self.feature_validator.validate_vehicle_search(
            user_id=payloads['user_id']
        )
        query_payload = self.vehicle_validator.validate_request(
            params=request.query_params
        )
        page_data = self.vehicle_validator.validate_paginate_over_10k(
            params=request.query_params
        )

        total_data = request.query_params['total']

        checkpoint = self.checkpoin_repo.get_ip_address()

        data, paginate_data = self.vehicle_pass_repo.get_vehicles(
            plate_no=query_payload['plate_no'],
            province=query_payload['province'],
            checkpoint=query_payload['checkpoint'],
            direction=query_payload['direction'],
            vehicle_type=query_payload['vehicle_type'],
            vehicle_color=query_payload['vehicle_color'],
            start_date=query_payload['start_date'],
            end_date=query_payload['end_date'],
            page_data=page_data,
            total=int(total_data),
            type=query_payload['type']
        )

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

                    # print(bool(url_plate_parsed.scheme))

                    if(bool(url_plate_parsed.scheme) == True):

                        bma_url_plate_parsed = url_plate_parsed._replace(netloc=ch_data["BMA_IP"]+":"+ch_data["BMA_RESPONSE_PORT"]).geturl()

                        net_url_plate_parsed = url_plate_parsed._replace(netloc=ch_data["NET_IP"]+":"+ch_data["NET_RESPONSE_PORT"]).geturl()

                    if(bool(url_image_parsed.scheme) == True):

                        bma_url_image_parsed = url_image_parsed._replace(netloc=ch_data["BMA_IP"]+":"+ch_data["BMA_RESPONSE_PORT"]).geturl()

                        net_url_image_parsed = url_image_parsed._replace(netloc=ch_data["NET_IP"]+":"+ch_data["NET_RESPONSE_PORT"]).geturl()

                    my_dict = {'BMA_PLATE_PIC_URL':bma_url_plate_parsed, 'BMA_IMAGE_PATH' : bma_url_image_parsed, 'NET_PLATE_PIC_URL':net_url_plate_parsed, 'NET_IMAGE_PATH' : net_url_image_parsed}

            data[i].update(my_dict)

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'page': paginate_data['page'],
            'page_size': paginate_data['page_size'],
            'page_total': paginate_data['page_total'],
            'total': total_data,
            'data': {
                'records': data,
                'total': len(data),
            }
        }

        return Response(response, status=status.HTTP_200_OK)

    def filter(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        self.feature_validator.validate_vehicle_search(
            user_id=payloads['user_id']
        )
        query_payload = self.vehicle_validator.validate_request(
            params=request.query_params
        )

        total_data = self.vehicle_pass_repo.get_total(
            plate_no=query_payload['plate_no'],
            province=query_payload['province'],
            checkpoint=query_payload['checkpoint'],
            direction=query_payload['direction'],
            vehicle_type=query_payload['vehicle_type'],
            vehicle_color=query_payload['vehicle_color'],
            start_date=query_payload['start_date'],
            end_date=query_payload['end_date'],
            type=query_payload['type'],
        )

        checkpoint = self.checkpoin_repo.get_by_id(query_payload['checkpoint'])
        province = self.province_repo.get_by_id(query_payload['province'])
        color = self.vehicle_color_repo.get_by_name(query_payload['vehicle_color'])
        v_type = self.vehicle_type_repo.get_by_name(query_payload['vehicle_type'])

        filter_data = {
            'checkpoint': checkpoint,
            'color': color,
            'type': v_type,
            'province': province,
            'total': total_data,
        }

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'total': total_data,
            'data': {
                'filter': filter_data
            }
        }

        return Response(response, status=status.HTTP_200_OK)

    def get_vehicle_total(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        self.feature_validator.validate_vehicle_search(
            user_id=payloads['user_id']
        )
        query_payload = self.vehicle_validator.validate_request(
            params=request.query_params
        )

        total_data = self.vehicle_pass_repo.get_vehicle_total(
            plate_no=query_payload['plate_no'],
            province=query_payload['province'],
            checkpoint=query_payload['checkpoint'],
            direction=query_payload['direction'],
            vehicle_type=query_payload['vehicle_type'],
            vehicle_color=query_payload['vehicle_color'],
            start_date=query_payload['start_date'],
            end_date=query_payload['end_date'],
        )



        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'total': total_data,
        }

        return Response(response, status=status.HTTP_200_OK)

    def get_filter(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        self.feature_validator.validate_vehicle_search(
            user_id=payloads['user_id']
        )
        query_payload = self.vehicle_validator.validate_request(
            params=request.query_params
        )
        page_data = self.vehicle_validator.validate_paginate_over_10k(
            params=request.query_params
        )

        if(int(request.query_params.get("total")) != 0):
            total_data = int(request.query_params.get("total"))
        else:
             total_data = self.vehicle_pass_repo.get_vehicle_total(
                plate_no=query_payload['plate_no'],
                province=query_payload['province'],
                checkpoint=query_payload['checkpoint'],
                direction=query_payload['direction'],
                vehicle_type=query_payload['vehicle_type'],
                vehicle_color=query_payload['vehicle_color'],
                start_date=query_payload['start_date'],
                end_date=query_payload['end_date'],
            )

        data, paginate_data = self.vehicle_pass_repo.get_vehicle_all(
            plate_no=query_payload['plate_no'],
            province=query_payload['province'],
            checkpoint=query_payload['checkpoint'],
            direction=query_payload['direction'],
            vehicle_type=query_payload['vehicle_type'],
            vehicle_color=query_payload['vehicle_color'],
            start_date=query_payload['start_date'],
            end_date=query_payload['end_date'],
            page_data=page_data,
            total=total_data
        )

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'page': paginate_data['page'],
            'page_size': paginate_data['page_size'],
            'page_total': paginate_data['page_total'],
            'total': total_data,
            'total2': int(request.query_params.get("total")),
            'data': {
                'records': data,
                'total': len(data)
            }
        }

        return Response(response, status=status.HTTP_200_OK)

    def get_search(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        self.feature_validator.validate_vehicle_search(
            user_id=payloads['user_id']
        )
        query_payload = self.vehicle_validator.validate_request(
            params=request.query_params
        )
        page_data = self.vehicle_validator.validate_paginate(
            params=request.query_params
        )

        # total_data = self.vehicle_pass_repo.get_total(
        #     plate_no=query_payload['plate_no'],
        #     province=query_payload['province'],
        #     checkpoint=query_payload['checkpoint'],
        #     direction=query_payload['direction'],
        #     vehicle_type=query_payload['vehicle_type'],
        #     vehicle_color=query_payload['vehicle_color'],
        #     start_date=query_payload['start_date'],
        #     end_date=query_payload['end_date'],
        # )
        total_data = 10000
       
        data, paginate_data = self.vehicle_pass_repo.get_vehicle(
            plate_no=query_payload['plate_no'],
            province=query_payload['province'],
            checkpoint=query_payload['checkpoint'],
            direction=query_payload['direction'],
            vehicle_type=query_payload['vehicle_type'],
            vehicle_color=query_payload['vehicle_color'],
            start_date=query_payload['start_date'],
            end_date=query_payload['end_date'],
            page_data=page_data,
            total=total_data
        )

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'page': paginate_data['page'],
            'page_size': paginate_data['page_size'],
            'page_total': paginate_data['page_total'],
            'total': total_data,
            'data': {
                'records': data,
                'total': len(data)
            }
        }

        return Response(response, status=status.HTTP_200_OK)

    def get_violation_search(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        self.feature_validator.validate_vehicle_search(
            user_id=payloads['user_id']
        )
        query_payload = self.vehicle_validator.validate_request(
            params=request.query_params
        )
        page_data = self.vehicle_validator.validate_paginate(
            params=request.query_params
        )

        total_data = self.vehicle_pass_repo.get_violation_total(
            plate_no=query_payload['plate_no'],
            province=query_payload['province'],
            checkpoint=query_payload['checkpoint'],
            direction=query_payload['direction'],
            vehicle_type=query_payload['vehicle_type'],
            vehicle_color=query_payload['vehicle_color'],
            start_date=query_payload['start_date'],
            end_date=query_payload['end_date'],
        )
        # total_data = 10000

        data, paginate_data = self.vehicle_pass_repo.get_violation_vehicle(
            plate_no=query_payload['plate_no'],
            province=query_payload['province'],
            checkpoint=query_payload['checkpoint'],
            direction=query_payload['direction'],
            vehicle_type=query_payload['vehicle_type'],
            vehicle_color=query_payload['vehicle_color'],
            start_date=query_payload['start_date'],
            end_date=query_payload['end_date'],
            page_data=page_data,
            total=total_data
        )

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'page': paginate_data['page'],
            'page_size': paginate_data['page_size'],
            'page_total': paginate_data['page_total'],
            'total': total_data,
            'data': {
                'records': data,
                'total': len(data)
            }
        }

        return Response(response, status=status.HTTP_200_OK)

    def search_origin_destination_time(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        self.feature_validator.validate_vehicle_destination_search(
            user_id=payloads['user_id']
        )
        query_payload = self.vehicle_validator.validate_request_destination(
            params=request.query_params
        )
        page_data = self.vehicle_validator.validate_paginate(
            params=request.query_params
        )

        # total_data = self.vehicle_pass_repo.get_total_desination(
        #     date=query_payload['start_date'],
        # )
        total_data = 10000

        # data, paginate_data = self.vehicle_pass_repo.get_destination_times(
        #     province=query_payload['province'],
        #     vehicle_type=query_payload['vehicle_type'],
        #     vehicle_color=query_payload['vehicle_color'],
        #     start_date=query_payload['start_date'],
        #     page_data=page_data,
        #     total=total_data
        # )

        data, paginate_data = self.vehicle_pass_repo.get_destination_times(
            province=query_payload['province'],
            vehicle_type=query_payload['vehicle_type'],
            vehicle_color=query_payload['vehicle_color'],
            start_date=query_payload['start_date'],
            end_date=query_payload['end_date'],
            page_data=page_data,
            total=total_data
        )

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'page': paginate_data['page'],
            'page_size': paginate_data['page_size'],
            'page_total': paginate_data['page_total'],
            'total': total_data,
            'data': {
                'records': data,
                'total': len(data)
            }
        }
        return Response(response, status=status.HTTP_200_OK)

    def get_search_origin_destination(self, request,type):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        self.feature_validator.validate_vehicle_destination_search(
            user_id=payloads['user_id']
        )
        query_payload = self.vehicle_validator.validate_request_destination_vehicle(
            params=request.query_params
        )
        user = self.user_repo.get_by_id(id=payloads['user_id'])
        group = self.group_repo.get_by_id(id=user['group_id'])
        user_name = user['name']
        department_name = group['department_name']
        now = datetime.now()

        data = self.vehicle_pass_repo.get_destination_vehicle(
            plate_no= query_payload['plate_no'],
            province=query_payload['province'],
            vehicle_type=query_payload['vehicle_type'],
            vehicle_color=query_payload['vehicle_color'],
            start_date=query_payload['start_date'],
            end_date=query_payload['end_date']
        )
        df = pd.DataFrame(data)
        df = df.rename(
            columns={
                'time': 'start_time',
                'checkpoint': 'origin',
                'direction':'original_direction'
            }
        )
        df['original_direction'] = df['original_direction'].replace('inbound','IN')
        df['original_direction'] = df['original_direction'].replace('outbound','OUT')
        df['destination_direction'] = df['original_direction'].shift(-1).fillna('None')
        df['destination'] = df['origin'].shift(-1).fillna('None')
        df['end_time'] = df['start_time'].shift(-1).fillna('None')
        df['destination_lat'] = df['latitude'].shift(-1).fillna('None')
        df['destination_long'] = df['longtitude'].shift(-1).fillna('None')

        fmt = '%Y-%m-%d %H:%M:%S'
        df['diff_time'] = 'None'
        for i in range(len(df['end_time'])):
            try:
                tstamp1 = datetime.strptime(df['start_time'][i], fmt)
                tstamp2 = datetime.strptime(df['end_time'][i], fmt)
                sec = tstamp2 - tstamp1
                hour = sec / 60
                df['diff_time'][i] = str(hour)
            except:
                pass
        
        if(type == 'report'):
            base64_plate_pic = []
            base64_image_pic = []

            for url in df['plate_picture']:
                if url:
                    res = requests.get(url)
                    base64_plate_pic.append(base64.b64encode(res.content))
                else:
                    base64_plate_pic.append(url)

            for url in df['image_url']:
                if url:
                    res = requests.get(url)
                    base64_image_pic.append(base64.b64encode(res.content))
                else:
                    base64_image_pic.append(url)

            df['user'] = user_name
            df['department'] = department_name
            df['report_date'] = now
            df['base64_plate_pic'] = base64_plate_pic
            df['base64_image_pic'] = base64_image_pic        
        
        data = df.to_dict('records')
       
        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': {
                'records': data,
                'total': len(data)
            }
        }

        return Response(response, status=status.HTTP_200_OK)

    # def get_origin_destination_report(self, request,vehicle_passing_id):
    #     payloads = self.session_validator.validate_session(
    #         headers=request.headers
    #     )

    #     self.feature_validator.validate_vehicle_search(
    #         user_id=payloads['user_id']
    #     )
    #     try:
    #         vehicle_passing_id = str(vehicle_passing_id)
    #     except:
    #         response = {
    #             'status_code': 400,
    #             'message': 'input type error'
    #         }

    #         raise ParseError(response)
    #     data = self.vehicle_pass_repo.get_destination_by_id(
    #        vehicle_passing_id
    #     )
    #     df = pd.DataFrame(data)
    #     df = df.rename(
    #         columns={
    #             'time': 'start_time',
    #             'checkpoint': 'origin',
    #         }
    #     )
    #     df['destination'] = df['origin'].shift(-1).fillna('None')
    #     df['end_time'] = df['start_time'].shift(-1).fillna('None')
      
    #     fmt = '%Y-%m-%d %H:%M:%S'
    #     df['diff_time'] = 'None'
    #     for i in range(len(df['end_time'])):
    #         try:
    #             tstamp1 = datetime.strptime(df['start_time'][i], fmt)
    #             tstamp2 = datetime.strptime(df['end_time'][i], fmt)
    #             sec = tstamp2 - tstamp1
    #             hour = sec / 60
    #             df['diff_time'][i] = str(hour)
    #         except:
    #             pass
        
       
    #     data = df.to_dict('records')
    #     data = data[0]
    #     response = {
    #         'status_code': 200,
    #         'message': self.get_success_msg,
    #         'data': data
    #     }
    #     return Response(response, status=status.HTTP_200_OK)


    def get_all_report(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        self.feature_validator.validate_vehicle_search(
            user_id=payloads['user_id']
        )
        query_payload = self.vehicle_validator.validate_request(
            params=request.query_params
        )

        data = self.vehicle_pass_repo.get_all_report(
            plate_no=query_payload['plate_no'],
            province=query_payload['province'],
            checkpoint=query_payload['checkpoint'],
            direction=query_payload['direction'],
            vehicle_type=query_payload['vehicle_type'],
            vehicle_color=query_payload['vehicle_color'],
            start_date=query_payload['start_date'],
            end_date=query_payload['end_date'],
        )

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': {
                'records': data,
                'total': len(data)
            }
        }

        return Response(response, status=status.HTTP_200_OK)

    def get_one_report(self, request, vehicle_passing_id):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

        self.feature_validator.validate_vehicle_search(
            user_id=payloads['user_id']
        )

        # self.feature_validator.validate_vehicle_search(
        #     user_id=payloads['user_id']
        # )
        user = self.user_repo.get_by_id(id=payloads['user_id'])
        group = self.group_repo.get_by_id(id=user['group_id'])
        user_name = user['name']
        department_name = group['department_name']
        now = datetime.now()

        try:
            vehicle_passing_id = str(vehicle_passing_id)
        except:
            response = {
                'status_code': 400,
                'message': 'input type error'
            }

            raise ParseError(response)

        data = self.vehicle_pass_repo.get_report_by_id(
            id=vehicle_passing_id
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

    def get_one_violation_report(self, request, vehicle_passing_id):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

        self.feature_validator.validate_vehicle_search(
            user_id=payloads['user_id']
        )

        # self.feature_validator.validate_vehicle_search(
        #     user_id=payloads['user_id']
        # )
        user = self.user_repo.get_by_id(id=payloads['user_id'])
        group = self.group_repo.get_by_id(id=user['group_id'])
        user_name = user['name']
        department_name = group['department_name']
        now = datetime.now()

        try:
            vehicle_passing_id = str(vehicle_passing_id)
        except:
            response = {
                'status_code': 400,
                'message': 'input type error'
            }

            raise ParseError(response)

        data = self.vehicle_pass_repo.get_violation_report_by_id(
            id=vehicle_passing_id
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