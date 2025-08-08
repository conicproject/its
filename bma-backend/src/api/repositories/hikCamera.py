import requests

from rest_framework.exceptions import NotFound

class HikCameraRepository:
    def __init__(self):
        self.app_key = "28943054"
        self.app_password = "DxETP3xhd4oNCOXzCJwm"
        self.url = "http://10.151.1.77:9017/artemis-web/debug"
        self.checkpoint_cameras_path = "/api/resource/v1/regions/regionIndexCode/cameras"
        self.all_camera = "/api/resource/v1/cameras"


    def get_list_by_area_code(self, area_code):
        payloads = {
            "httpMethod": "POST",
            "path": self.checkpoint_cameras_path,
            "headers": {},
            "query": {},
            "parameter": {},
            "body": {
                "pageNo": 1,
                "pageSize": 100,
                "regionIndexCode": area_code,
                "treeCode": "0"
            },
            "contentType": "application/json;charset=UTF-8",
            "mock": False,
            "appKey": self.app_key,
            "appSecret": self.app_password
        }

        try:
            response = requests.post(self.url, json=payloads)
            data = response.json()

        except:
            response = {
                'status_code': 404,
                'message': "can't get rtsp url"
            }

            raise NotFound(response)
        
        return data
    

    def get_total_camera_status(self, area_code):
        data = self.get_list_by_area_code(
            area_code=area_code
        )

        list_data = data['response']['data']['list']

        list_active_camera_code = [camera['cameraIndexCode'] for camera in list_data if camera['status'] == 1]
        list_deactive_camera_code = [camera['cameraIndexCode'] for camera in list_data if camera['status'] == 0]

        result = {
            'active': len(list_active_camera_code),
            'deactive': len(list_deactive_camera_code)
        }

        return result

    def get_list(self):
        payloads = {
            "httpMethod": "POST",
            "path": self.all_camera,
            "headers": {},
            "query": {},
            "parameter": {},
            "body": {
                "pageNo": 1,
                "pageSize": 200,
                "treeCode": "0"
            },
            "contentType": "application/json;charset=UTF-8",
            "mock": False,
            "appKey": self.app_key,
            "appSecret": self.app_password
        }

        try:
            response = requests.post(self.url, json=payloads)
            data = response.json()

        except:
            response = {
                'status_code': 404,
                'message': "can't get rtsp url"
            }

            raise NotFound(response)
        
        return data