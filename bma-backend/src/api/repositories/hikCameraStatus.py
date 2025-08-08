from api.repositories.oracleCamera import OracleCameraRepository
from api.repositories.oracleCheckpoint import OracleCheckpointRepository

import requests

class HikCameraStatusRepository:
    def __init__(self):
        self.camera_repo = OracleCameraRepository()
        self.checkpoint_repo = OracleCheckpointRepository()

        self.url = 'http://10.151.1.77:9017/artemis-web/debug'
        self.app_key = "28943054"
        self.app_password = "DxETP3xhd4oNCOXzCJwm"


    def check_status_all(self):
        total_2_phase_camera = self.camera_repo.get_count_2_phase_all()
        # total_camera = self.camera_repo.get_count_all()
        camera_codes = self.camera_repo.get_all_camera_code_phase_2()
        payload = {
            "httpMethod": "POST",
            "path": "/api/resource/v1/cameras",
            "headers": {},
            "query": {},
            "parameter": {},
            "body": {
                "pageNo": 1,
                "pageSize": total_2_phase_camera,
                "treeCode": "0"
            },
            "contentType": "application/json;charset=UTF-8",
            "mock": False,
            "appKey": self.app_key,
            "appSecret": self.app_password
        }
        camera_status_response = requests.post(self.url, json=payload)
        camera_status_data = camera_status_response.json()
        camera_tf = [d['code'] for d in camera_codes if d['type'] == 'TF']
        total_tf = len(camera_tf)
        camera_pv = [d['code'] for d in camera_codes if d['type'] == 'PV']
        total_pv = len(camera_pv)
        camera_online_tf = len([
            camera_data['status'] for camera_data in camera_status_data['response']['data']['list'] if camera_data['status'] == 1 and camera_data['cameraIndexCode'] in camera_tf
        ])
        camera_online_pv = len([
            camera_data['status'] for camera_data in camera_status_data['response']['data']['list'] if camera_data['status'] == 1 and camera_data['cameraIndexCode'] in camera_pv
        ])
        
        camera_tf_status = {
            'online': camera_online_tf,
            'offline': total_tf - camera_online_tf,
            'total': total_tf
        }
        camera_pv_status = {
            'online': camera_online_pv,
            'offline': total_pv - camera_online_pv,
            'total': total_pv
        }

        return camera_tf_status,camera_pv_status


    def check_checkpoint_status(self, checkpoint_id):
        total_camera_data = self.camera_repo.get_by_id(
            id=checkpoint_id
        )
        total_camera = len(total_camera_data)
        
        area_code = self.checkpoint_repo.get_area_code_by_id(
            id=checkpoint_id
        )

        payload = {
            "httpMethod": "POST",
            "path": "/api/resource/v1/regions/regionIndexCode/cameras",
            "headers": {},
            "query": {},
            "parameter": {},
            "body": {
                "pageNo": 1,
                "pageSize": 20,
                "regionIndexCode": area_code,
                "treeCode": "0"
            },
            "contentType": "application/json;charset=UTF-8",
            "mock": False,
            "appKey": self.app_key,
            "appSecret": self.app_password
        }

        camera_status_response = requests.post(self.url, json=payload)
        camera_status_data = camera_status_response.json()
        camera_tf = [d['CAMERA_CODE'] for d in total_camera_data if d['type'] == 'TF']
        total_tf = len(camera_tf)
        camera_pv = [d['CAMERA_CODE'] for d in total_camera_data if d['type'] == 'PV']
        total_pv = len(camera_pv)
        camera_online_tf = len([
            camera_data['status'] for camera_data in camera_status_data['response']['data']['list'] if camera_data['status'] == 1 and camera_data['cameraIndexCode'] in camera_tf
        ])
        camera_online_pv = len([
            camera_data['status'] for camera_data in camera_status_data['response']['data']['list'] if camera_data['status'] == 1 and camera_data['cameraIndexCode'] in camera_pv
        ])
        # camera_online = len([
        #     camera_data['status'] for camera_data in camera_status_data['response']['data']['list'] if camera_data['status'] == 1
        # ])

        # camera_status = {
        #     'online': camera_online,
        #     'offline': total_camera - camera_online,
        #     'total': total_camera
        # }
        camera_tf_status = {
            'online': camera_online_tf,
            'offline': total_tf - camera_online_tf,
            'total': total_tf
        }
        camera_pv_status = {
            'online': camera_online_pv,
            'offline': total_pv - camera_online_pv,
            'total': total_pv
        }

        return camera_tf_status,camera_pv_status


    def get_all_sensor_report(self):
        total_camera = self.camera_repo.get_count_2_phase_all()
        payload = {
            "httpMethod": "POST",
            "path": "/api/resource/v1/cameras",
            "headers": {},
            "query": {},
            "parameter": {},
            "body": {
                "pageNo": 1,
                "pageSize": total_camera,
                "treeCode": "0"
            },
            "contentType": "application/json;charset=UTF-8",
            "mock": False,
            "appKey": self.app_key,
            "appSecret": self.app_password
        }
        camera_status_response = requests.post(self.url, json=payload)
        camera_status_data = camera_status_response.json()

        df_camera = self.camera_repo.get_all_sensor_report()
        df_camera['status'] = 0
        for camera_data in camera_status_data['response']['data']['list']:
            df_camera.loc[df_camera['code'] == camera_data['cameraIndexCode'], 'status'] = camera_data['status']
                

        df_camera[['status']] = df_camera[['status']].replace(
            [0, 1], ['offline', 'online']
        )

        result = df_camera[['ip', 'name', 'checkpoint', 'status']]
        return result


    def get_all_sensor_report_by_checkpoint(self, checkpoint_id):
        total_camera = self.camera_repo.get_by_id(
            id=checkpoint_id
        )
        total_camera = len(total_camera)
        area_code = self.checkpoint_repo.get_area_code_by_id(
            id=checkpoint_id
        )

        payload = {
            "httpMethod": "POST",
            "path": "/api/resource/v1/regions/regionIndexCode/cameras",
            "headers": {},
            "query": {},
            "parameter": {},
            "body": {
                "pageNo": 1,
                "pageSize": 20,
                "regionIndexCode": area_code,
                "treeCode": "0"
            },
            "contentType": "application/json;charset=UTF-8",
            "mock": False,
            "appKey": self.app_key,
            "appSecret": self.app_password
        }

        camera_status_response = requests.post(self.url, json=payload)
        camera_status_data = camera_status_response.json()

        df_camera = self.camera_repo.get_all_sensor_report_by_checkpoint(
            checkpoint_id=checkpoint_id
        )
        df_camera['status'] = 0

        for camera_data in camera_status_data['response']['data']['list']:
            df_camera.loc[df_camera['code'] == camera_data['cameraIndexCode'], 'status'] = camera_data['status']

        df_camera[['status']] = df_camera[['status']].replace(
            [0, 1], ['offline', 'online']
        )

        result = df_camera[['ip', 'name', 'checkpoint', 'status']]

        return result