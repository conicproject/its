from api.repositories.oracleCheckpoint import OracleCheckpointRepository
from api.repositories.oracleCamera import OracleCameraRepository

from rest_framework.exceptions import NotFound
import requests

class TrafficViewLogic:

    def __init__(self):
        self.checkpoint_repo = OracleCheckpointRepository()
        self.camera_repo = OracleCameraRepository()

        self.app_key = "28943054"
        self.app_password = "DxETP3xhd4oNCOXzCJwm"
        self.url = "http://10.151.1.77:9017/artemis-web/debug"
        self.live_view_api_path = "/api/video/v1/cameras/previewURLs"
        self.playback_api_path = "/api/video/v1/cameras/playbackURLs"


    def get_rstp_live_view(self, camera_code):
        payloads = {
            "httpMethod":"POST",
            "path": self.live_view_api_path,
            "headers": {},
            "query": {},
            "parameter": {},
            "body": {
                "cameraIndexCode": camera_code,
                "streamType": 0,
                "protocol": "hls",
                "transmode": 1,
                "expand": "streamform=rtp"
            },
            "contentType": "application/json;charset=UTF-8",
            "mock":False,
            "appKey": self.app_key,
            "appSecret": self.app_password
        }

        try:
            response = requests.post(self.url, json=payloads)
            response = response.json()
            rstp_url = response['response']['data']['url']

        except:
            response = {
                'status_code': 404,
                'message': "can't get rstp url"
            }

            raise NotFound(response)
        
        return rstp_url


    def get_rstp_playback(self, camera_code, start_time, end_time):
        payloads = {
            "httpMethod": "POST",
            "path": self.playback_api_path,
            "headers": {},
            "query": {},
            "parameter": {},
            "body": {
                "cameraIndexCode": camera_code,
                "beginTime": start_time,
                "endTime": end_time,
                "recordLocation": "1",
                "protocol": "rtsp",
                "needReturnClipInfo": True,
                "expand": "streamform=rtp"
            },
            "contentType": "application/json;charset=UTF-8",
            "mock": False,
            "appKey": self.app_key,
            "appSecret": self.app_password
        }

        try:
            response = requests.post(self.url, json=payloads)
            response = response.json()
            rstp_url = response['response']['data']['url']

        except:
            rstp_url = None
        
        return rstp_url


    def get_sample_live_view(self, checkpoint_id):
        data = self.camera_repo.get_sample_camera(
            id=checkpoint_id
        )

        ## select only first index
        sample = data[0]
        camera_code = sample['code']
        rstp_url = self.get_rstp_live_view(camera_code=camera_code)

        return rstp_url, camera_code


    def get_live_view(self, checkpoint_id, camera_code):
        data = self.camera_repo.get_checkpoint_camera(
            id=checkpoint_id, camera_code=camera_code
        )

        camera_code = data['code']
        rstp_url = self.get_rstp_live_view(camera_code=camera_code)

        return rstp_url, camera_code


    def get_playback_view(self, checkpoint_id, camera_code, start_time, end_time):
        data = self.camera_repo.get_checkpoint_camera(
            id=checkpoint_id, camera_code=camera_code
        )

        camera_code = data['code']

        rstp_url = self.get_rstp_playback(
            camera_code=camera_code, start_time=start_time, end_time=end_time
        )

        return rstp_url, camera_code


    def get_checkpoint_cameras(self, checkpoint_id):
        data = self.camera_repo.get_by_id(
            id=checkpoint_id
        )

        return data

    def get_sample_live_view_by_id(self, camera_id):
        data = self.camera_repo.get_sample_camera_id(
            id=camera_id
        )

        ## select only first index
        sample = data[0]
        camera_code = sample['code']
        rstp_url = self.get_rstp_live_view(camera_code=camera_code)

        return rstp_url, camera_code