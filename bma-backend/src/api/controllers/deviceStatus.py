from cgi import test
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from api.validators.session import SessionValidator
from api.validators.feature import FeatureValidator
from api.validators.checkpointDetail import CheckpointDetailValidator

from api.repositories.oracleSNMP import OracleSNMPRepository
from api.repositories.hikCameraStatus import HikCameraStatusRepository
from api.repositories.oracleCheckpoint import OracleCheckpointRepository
from api.repositories.SNMP import SNMPRepository
from api.repositories.hikCamera import HikCameraRepository
from api.repositories.oracleCamera import OracleCameraRepository

class DeviceStatusViewSet(viewsets.ViewSet):

    def __init__(self):
        self.session_validator = SessionValidator()
        self.feature_validator = FeatureValidator()
        self.checkpoint_detail_validator = CheckpointDetailValidator()

        self.checkpoint_repo = OracleCheckpointRepository()
        self.snmp_repo = OracleSNMPRepository()
        self.snmp_status_repo = SNMPRepository()
        self.camera_status_repo = HikCameraStatusRepository()
        self.camera_repo = HikCameraRepository()
        self.oracle_camera_repo = OracleCameraRepository()

        self.get_success_msg = 'request get data success'


    def get_dashboard(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        self.feature_validator.validate_device_status(
            user_id=payloads['user_id']
        )

        camera_tf_status,camera_pv_status = self.camera_status_repo.check_status_all()
        
        df_snmp = self.snmp_repo.get_dataframe_all_config()
        snmp_list_id = df_snmp['id'].to_list()
        snmp_status_list = self.snmp_status_repo.get_all_status(
            list_id=snmp_list_id
        )
        df_snmp['status'] = snmp_status_list

        terninal_status = {
            'online': len(df_snmp[
                (df_snmp['type'] == 'terminal') & 
                (df_snmp['status'] == 'Up')
            ]),
            'offline': len(df_snmp[
                (df_snmp['type'] == 'terminal') & 
                (df_snmp['status'] == 'Down')
            ]),
            'total': len(df_snmp[
                (df_snmp['type'] == 'terminal')
            ])
        }

        switch_status = {
            'online': len(df_snmp[
                (df_snmp['type'] == 'switch') & 
                (df_snmp['status'] == 'Up')
            ]),
            'offline': len(df_snmp[
                (df_snmp['type'] == 'switch') & 
                (df_snmp['status'] == 'Down')
            ]),
            'total': len(df_snmp[
                (df_snmp['type'] == 'switch')
            ])
        }

        ups_status = {
            'online': len(df_snmp[
                (df_snmp['type'] == 'ups') & 
                (df_snmp['status'] == 'Up')
            ]),
            'offline': len(df_snmp[
                (df_snmp['type'] == 'ups') & 
                (df_snmp['status'] == 'Down')
            ]),
            'total': len(df_snmp[
                (df_snmp['type'] == 'ups')
            ])
        }

        server_status = {
            'online': len(df_snmp[
                (df_snmp['type'] == 'server') & 
                (df_snmp['status'] == 'Up')
            ]),
            'offline': len(df_snmp[
                (df_snmp['type'] == 'server') & 
                (df_snmp['status'] == 'Down')
            ]),
            'total': len(df_snmp[
                (df_snmp['type'] == 'server')
            ])
        }

        nvr_status = {
            'online': len(df_snmp[
                (df_snmp['type'] == 'nvr') & 
                (df_snmp['status'] == 'Up')
            ]),
            'offline': len(df_snmp[
                (df_snmp['type'] == 'nvr') & 
                (df_snmp['status'] == 'Down')
            ]),
            'total': len(df_snmp[
                (df_snmp['type'] == 'nvr')
            ])
        }
        camera_total = camera_tf_status['total'] +  camera_pv_status['total']
        camera_online_total = camera_tf_status['online'] +  camera_pv_status['online']
        camera_offline_total = camera_tf_status['offline'] +  camera_pv_status['offline']
        all_sensor_total = len(df_snmp) + camera_total
        all_sensor_online = ((len(df_snmp[df_snmp['status'] == 'Up']) + camera_online_total) / all_sensor_total) * 100
        all_sensor_offline = ((len(df_snmp[df_snmp['status'] == 'Down']) + camera_offline_total) / all_sensor_total) * 100

        all_sensor_status = {
            'online': all_sensor_online,
            'offline': all_sensor_offline
        }

        current_alarm_total = len(df_snmp[df_snmp['status'] == 'Down']) + camera_offline_total
        if current_alarm_total == 0:
            current_alarm_total = 1

        current_alarm_status = {
            'camera': (camera_offline_total / current_alarm_total) * 100,
            'camera_tf':(camera_tf_status['offline']/current_alarm_total)* 100,
            'camera_pv':(camera_pv_status['offline']/current_alarm_total)* 100,
            'terminal': (terninal_status['offline'] / current_alarm_total) * 100,
            'switch': (switch_status['offline'] / current_alarm_total) * 100,
            'ups': (ups_status['offline'] / current_alarm_total) * 100,
            'server': (server_status['offline'] / current_alarm_total) * 100,
            'nvr': (nvr_status['offline'] / current_alarm_total) * 100
        }
        
        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': {
                'camera_tf': camera_tf_status,
                'camera_pv': camera_pv_status,
                'terminal': terninal_status,
                'switch': switch_status,
                'ups': ups_status,
                'server': server_status,
                'nvr':nvr_status,
                'all_sensors': all_sensor_status,
                'current_alarm': current_alarm_status
            }
        }

        return Response(response, status=status.HTTP_200_OK)


    def get_checkpoint_status(self, request, checkpoint_id):
        checkpoint_id = self.checkpoint_detail_validator.validate_checkpoint_id(
            checkpoint_id=checkpoint_id
        )
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        self.feature_validator.validate_device_status(
            user_id=payloads['user_id']
        )

        checkpoint_detail = self.checkpoint_repo.get_by_id(
            id=checkpoint_id
        )

        camera_tf_status,camera_pv_status = self.camera_status_repo.check_checkpoint_status(
            checkpoint_id=checkpoint_id
        )

        df_snmp = self.snmp_repo.get_dataframe_by_checkpoint(
            checkpoint_id=checkpoint_id
        )

        snmp_list_id = df_snmp['id'].to_list()
        snmp_status_list = self.snmp_status_repo.get_all_status(
            list_id=snmp_list_id
        )
        df_snmp['status'] = snmp_status_list

        terninal_status = {
            'online': len(df_snmp[
                (df_snmp['type'] == 'terminal') & 
                (df_snmp['status'] == 'Up')
            ]),
            'offline': len(df_snmp[
                (df_snmp['type'] == 'terminal') & 
                (df_snmp['status'] == 'Down')
            ]),
            'total': len(df_snmp[
                (df_snmp['type'] == 'terminal')
            ])
        }

        switch_status = {
            'online': len(df_snmp[
                (df_snmp['type'] == 'switch') & 
                (df_snmp['status'] == 'Up')
            ]),
            'offline': len(df_snmp[
                (df_snmp['type'] == 'switch') & 
                (df_snmp['status'] == 'Down')
            ]),
            'total': len(df_snmp[
                (df_snmp['type'] == 'switch')
            ])
        }

        ups_status = {
            'online': len(df_snmp[
                (df_snmp['type'] == 'ups') & 
                (df_snmp['status'] == 'Up')
            ]),
            'offline': len(df_snmp[
                (df_snmp['type'] == 'ups') & 
                (df_snmp['status'] == 'Down')
            ]),
            'total': len(df_snmp[
                (df_snmp['type'] == 'ups')
            ])
        }

        nvr_status = {
            'online': len(df_snmp[
                (df_snmp['type'] == 'nvr') & 
                (df_snmp['status'] == 'Up')
            ]),
            'offline': len(df_snmp[
                (df_snmp['type'] == 'nvr') & 
                (df_snmp['status'] == 'Down')
            ]),
            'total': len(df_snmp[
                (df_snmp['type'] == 'nvr')
            ])
        }

        camera_total = camera_tf_status['total'] +  camera_pv_status['total']
        camera_online_total = camera_tf_status['online'] +  camera_pv_status['online']
        camera_offline_total = camera_tf_status['offline'] +  camera_pv_status['offline']
        all_sensor_total = len(df_snmp) + camera_total
        all_sensor_online = ((len(df_snmp[df_snmp['status'] == 'Up']) + camera_online_total) / all_sensor_total) * 100
        all_sensor_offline = ((len(df_snmp[df_snmp['status'] == 'Down']) + camera_offline_total) / all_sensor_total) * 100

        all_sensor_status = {
            'online': all_sensor_online,
            'offline': all_sensor_offline
        }

        current_alarm_total = len(df_snmp[df_snmp['status'] == 'Down']) + camera_offline_total

        if current_alarm_total == 0:
            current_alarm_total = 1

        current_alarm_status = {
            'camera': (camera_offline_total/ current_alarm_total) * 100,
            'camera_tf':(camera_tf_status['offline']/current_alarm_total)* 100,
            'camera_pv':(camera_pv_status['offline']/current_alarm_total)* 100,
            'terminal': (terninal_status['offline'] / current_alarm_total) * 100,
            'switch': (switch_status['offline'] / current_alarm_total) * 100,
            'ups': (ups_status['offline'] / current_alarm_total) * 100,
            'nvr': (nvr_status['offline'] / current_alarm_total) * 100
        }
        
        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': {
                'checkpoint': checkpoint_detail,
                'camera_tf': camera_tf_status,
                'camera_pv': camera_pv_status,
                'terminal': terninal_status,
                'switch': switch_status,
                'ups': ups_status,
                'nvr':nvr_status,
                'all_sensors': all_sensor_status,
                'current_alarm': current_alarm_status
            }
        }

        return Response(response, status=status.HTTP_200_OK)


    def get_all_sensor(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        self.feature_validator.validate_device_status(
            user_id=payloads['user_id']
        )

        df_camera = self.camera_status_repo.get_all_sensor_report()
        df_snmp = self.snmp_repo.get_dataframe_all_sensor_report()
        df_snmp['ip'] = 'ไม่ระบุ'

        snmp_list_id = df_snmp['id'].to_list()
        snmp_status_list, snmp_name_list = self.snmp_status_repo.get_all_sensor_report(
            list_id=snmp_list_id
        )

        df_checkpoint = self.checkpoint_repo.get_all_sensor_report()
        checkpoint_ids = df_checkpoint['id'].to_list()
        checkpoint_name = df_checkpoint['name'].to_list()

        checkpoint_ids.append('999999')
        checkpoint_name.append('ไม่ระบุ')

        df_snmp['status'] = snmp_status_list
        df_snmp['name'] = snmp_name_list
        df_snmp[['checkpoint']] = df_snmp[['checkpoint']].replace(
            checkpoint_ids, checkpoint_name
        )
        df_snmp[['status']] = df_snmp[['status']].replace(
            ['Up', 'Down'], ['online', 'offline']
        )

        df_snmp = df_snmp[['ip', 'name', 'checkpoint', 'status']]
        summary = df_snmp.append(df_camera)

        report_data = {
            'online': summary[summary['status'] == 'online'].to_dict('records'),
            'offline': summary[summary['status'] == 'offline'].to_dict('records')
        }

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': report_data
        }

        return Response(response, status=status.HTTP_200_OK)


    def get_all_sensor_by_checkpoint(self, request, checkpoint_id):
        checkpoint_id = self.checkpoint_detail_validator.validate_checkpoint_id(
            checkpoint_id=checkpoint_id
        )
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        self.feature_validator.validate_device_status(
            user_id=payloads['user_id']
        )

        df_camera = self.camera_status_repo.get_all_sensor_report_by_checkpoint(
            checkpoint_id=checkpoint_id
        )

        df_snmp = self.snmp_repo.get_dataframe_all_sensor_report_by_checkpoint(
            checkpoint_id=checkpoint_id
        )
        df_snmp['ip'] = 'ไม่ระบุ'

        snmp_list_id = df_snmp['id'].to_list()
        snmp_status_list, snmp_name_list = self.snmp_status_repo.get_all_sensor_report(
            list_id=snmp_list_id
        )

        df_checkpoint = self.checkpoint_repo.get_all_sensor_report()
        checkpoint_ids = df_checkpoint['id'].to_list()
        checkpoint_name = df_checkpoint['name'].to_list()

        df_snmp['status'] = snmp_status_list
        df_snmp['name'] = snmp_name_list
        df_snmp[['checkpoint']] = df_snmp[['checkpoint']].replace(
            checkpoint_ids, checkpoint_name
        )
        df_snmp[['status']] = df_snmp[['status']].replace(
            ['Up', 'Down'], ['online', 'offline']
        )

        df_snmp = df_snmp[['ip', 'name', 'checkpoint', 'status']]
        summary = df_snmp.append(df_camera)

        report_data = {
            'online': summary[summary['status'] == 'online'].to_dict('records'),
            'offline': summary[summary['status'] == 'offline'].to_dict('records')
        }

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': report_data
        }

        return Response(response, status=status.HTTP_200_OK)


    def get_current_alarm(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        self.feature_validator.validate_device_status(
            user_id=payloads['user_id']
        )

        df_camera = self.camera_status_repo.get_all_sensor_report()
        df_snmp = self.snmp_repo.get_dataframe_all_sensor_report()
        df_snmp['ip'] = 'ไม่ระบุ'

        snmp_list_id = df_snmp['id'].to_list()
        snmp_status_list, snmp_name_list = self.snmp_status_repo.get_all_sensor_report(
            list_id=snmp_list_id
        )

        df_checkpoint = self.checkpoint_repo.get_all_sensor_report()
        checkpoint_ids = df_checkpoint['id'].to_list()
        checkpoint_name = df_checkpoint['name'].to_list()

        checkpoint_ids.append('999999')
        checkpoint_name.append('ไม่ระบุ')

        df_snmp['status'] = snmp_status_list
        df_snmp['name'] = snmp_name_list
        df_snmp[['checkpoint']] = df_snmp[['checkpoint']].replace(
            checkpoint_ids, checkpoint_name
        )
        df_snmp[['status']] = df_snmp[['status']].replace(
            ['Up', 'Down'], ['online', 'offline']
        )

        df_snmp = df_snmp[['ip', 'name', 'checkpoint', 'status']]
        summary = df_snmp.append(df_camera)

        report_data = {
            'offline': summary[summary['status'] == 'offline'].to_dict('records')
        }

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': report_data
        }

        return Response(response, status=status.HTTP_200_OK)


    def get_current_alarm_by_checkpoint(self, request, checkpoint_id):
        checkpoint_id = self.checkpoint_detail_validator.validate_checkpoint_id(
            checkpoint_id=checkpoint_id
        )
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        self.feature_validator.validate_device_status(
            user_id=payloads['user_id']
        )

        df_camera = self.camera_status_repo.get_all_sensor_report_by_checkpoint(
            checkpoint_id=checkpoint_id
        )

        df_snmp = self.snmp_repo.get_dataframe_all_sensor_report_by_checkpoint(
            checkpoint_id=checkpoint_id
        )
        df_snmp['ip'] = 'ไม่ระบุ'

        snmp_list_id = df_snmp['id'].to_list()
        snmp_status_list, snmp_name_list = self.snmp_status_repo.get_all_sensor_report(
            list_id=snmp_list_id
        )

        df_checkpoint = self.checkpoint_repo.get_all_sensor_report()
        checkpoint_ids = df_checkpoint['id'].to_list()
        checkpoint_name = df_checkpoint['name'].to_list()

        df_snmp['status'] = snmp_status_list
        df_snmp['name'] = snmp_name_list
        df_snmp[['checkpoint']] = df_snmp[['checkpoint']].replace(
            checkpoint_ids, checkpoint_name
        )
        df_snmp[['status']] = df_snmp[['status']].replace(
            ['Up', 'Down'], ['online', 'offline']
        )

        df_snmp = df_snmp[['ip', 'name', 'checkpoint', 'status']]
        summary = df_snmp.append(df_camera)

        report_data = {
            'offline': summary[summary['status'] == 'offline'].to_dict('records')
        }

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': report_data
        }

        return Response(response, status=status.HTTP_200_OK)

    def get_camera_status(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        self.feature_validator.validate_device_status(
            user_id=payloads['user_id']
        )

        cameras = self.oracle_camera_repo.get_all()
        camera_code = [d['code'] for d in cameras]
        hik_cameras = self.camera_repo.get_list()['response']['data']['list']
        list_deactive_camera_code = [camera['cameraIndexCode'] for camera in hik_cameras if camera['status'] == 0 and camera['cameraIndexCode'] in camera_code]
        camera_project = list(filter(lambda cameras: cameras['code'] in list_deactive_camera_code, cameras))

        df_snmps = self.snmp_repo.get_all()
        ptrg_data = self.snmp_status_repo.get_all_sensor_status()
        list_deactive_ptrg_id = [df_snmp['objid'] for df_snmp in ptrg_data if df_snmp['status'] == 'Down']
        ptrg_project = list(filter(lambda df_snmps: df_snmps['id'] in list_deactive_ptrg_id, df_snmps))

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data_camera': camera_project,
            'count_camera': len(camera_project),
            'ptrg_data' : ptrg_project,
            'count_ptrg': len(ptrg_project),
        }

        return Response(response, status=status.HTTP_200_OK)

    def check_device(self, request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )
        self.feature_validator.validate_device_status(
            user_id=payloads['user_id']
        )
        
        cameras = self.oracle_camera_repo.get_all()
        camera_code = [d['code'] for d in cameras]
        hik_cameras = self.camera_repo.get_list()['response']['data']['list']
        list_deactive_camera_code = [camera['cameraIndexCode'] for camera in hik_cameras if camera['status'] == 0 and camera['cameraIndexCode'] in camera_code]

        ptrg_data = self.snmp_status_repo.get_all_sensor_status()
        list_deactive_ptrg_id = [df_snmp['objid'] for df_snmp in ptrg_data if df_snmp['status'] == 'Down']

        count = len(list_deactive_ptrg_id) + len(list_deactive_camera_code)

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': count,
        }

        return Response(response, status=status.HTTP_200_OK)