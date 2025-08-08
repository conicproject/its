from django.urls import path

from api.controllers.login import LoginViewSet
from api.controllers.menu import MenuViewSet
from api.controllers.test import TestViewSet
from api.controllers.record import RecordViewSet
from api.controllers.vehicle import VehiclePassViewSet
from api.controllers.trafficView import TrafficViewViewSet

from api.controllers.user import UserViewSet

from api.controllers.camera import CameraViewSet
from api.controllers.checkpoint import CheckpointViewSet
from api.controllers.vehicleColor import VehicleColorViewSet
from api.controllers.vehicleType import VehicleTypeViewSet
from api.controllers.province import ProvinceViewSet
from api.controllers.userLevel import userLevelViewSet
from api.controllers.blacklist import BlacklistViewSet
from api.controllers.deviceStatus import DeviceStatusViewSet
from api.controllers.blacklistPass import BlacklistPassViewSet
from api.controllers.bkkReport import BkkReportViewSet
from api.controllers.truckPass import TruckPassViewSet
from api.controllers.manualInsert import ManualViewSet
from api.controllers.bkkReport2 import BkkReport2ViewSet

from api.controllers.test import TestViewSet 

from api.controllers import playback
from api.controllers import blacklistPlayback
from api.controllers import violationPayback
from api.controllers import notification

from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    # path('testing', TestViewSet.as_view({'get': 'test_space'}), name='create user'),

    # path('notification-blacklist', notification.stream),

    # path('user', UserViewSet.as_view({'post': 'create'}), name='create user'),
    path('get-user', UserViewSet.as_view({'get': 'get_user'}), name='get get-user'),
    path('add-user', UserViewSet.as_view({'post': 'add_user'}), name='add add-user'),
    path('edit-user',UserViewSet.as_view({'post': 'edit_user'}), name='edit user'),
    path('del-user',UserViewSet.as_view({'delete': 'del_user'}), name='delete user'),
    path('list-user',UserViewSet.as_view({'get': 'list_user'}), name='list user'),
    path('get-department-group',UserViewSet.as_view({'get': 'get_group_department'}), name='list department include group'),
    path('get-department',UserViewSet.as_view({'get': 'get_department'}), name='get department'),
    path('get-user-level',UserViewSet.as_view({'get': 'get_user_level'}), name='get user level'),
    path('edit-user-group',UserViewSet.as_view({'post': 'edit_user_group'}),name='edit user group'),
    path('add-user-group', UserViewSet.as_view({'post': 'add_user_group'}), name='add group'),
    path('list-user-group',UserViewSet.as_view({'get': 'list_group_user'}),name='list user group'),
    path('del-user-group',UserViewSet.as_view({'delete': 'del_user_group'}), name='delete user group'),
    path('list-user-permission',UserViewSet.as_view({'get': 'list_user_permission'}),name='list user permission'),
    path('add-user-level', UserViewSet.as_view({'post': 'add_user_level'}), name='add user level permission'),
    path('edit-user-level', UserViewSet.as_view({'post': 'edit_user_level'}), name='edit user level permission'),
    path('del-user-level',UserViewSet.as_view({'delete': 'del_user_level'}), name='delete user level'),
   

    path('login', LoginViewSet.as_view({'post': 'auth'}), name='auth_login'),
    path('menu-bar', MenuViewSet.as_view({'get': 'get_menubar'}), name='get menu-bar'),
    path('get-menu',MenuViewSet.as_view({'get': 'get_list_menu'}), name='get menu'),
    path('checkpoints', CheckpointViewSet.as_view({'get': 'get_all_active'}), name='get all active checkpoint'),
    path('checkpoints/detail', CheckpointViewSet.as_view({'get': 'get_all_detail'}), name='get all active checkpoint'),
    path('list-checkpoints',CheckpointViewSet.as_view({'get': 'list_checkpoints'}), name='get list checkpoints'),
    path('get-district',CheckpointViewSet.as_view({'get': 'get_district'}), name='get district'),
    path('get-road',CheckpointViewSet.as_view({'get': 'get_road'}), name='get road'),
    path('add-checkpoint',CheckpointViewSet.as_view({'post': 'add_checkpoint'}), name='add checkpoints'),
    path('edit-checkpoint',CheckpointViewSet.as_view({'post': 'edit_checkpoint'}), name='edit checkpoints'),
    path('list-road',CheckpointViewSet.as_view({'get': 'list_road'}),name='list road'),
    path('add-road',CheckpointViewSet.as_view({'post': 'add_road'}), name='add road'),
    path('edit-road',CheckpointViewSet.as_view({'patch': 'edit_road'}), name='edit road'),
    path('list-lane',CheckpointViewSet.as_view({'get': 'list_lane'}),name='list lane'),
    path('add-lane',CheckpointViewSet.as_view({'post': 'add_lane'}), name='add lane'),
    path('edit-lane',CheckpointViewSet.as_view({'patch': 'edit_lane'}), name='edit lane'),

    path('list-cameras',CameraViewSet.as_view({'get': 'list_cameras'}), name='get list cameras'),
    path('get-checkpoints',CameraViewSet.as_view({'get': 'get_checkpoints'}), name='get all checkpoints'),
    path('add-camera',CameraViewSet.as_view({'post': 'add_camera'}), name='add camera'),
    path('edit-camera',CameraViewSet.as_view({'post': 'edit_camera'}), name='edit camera'),

    path('vehicles-color', VehicleColorViewSet.as_view({'get': 'get_all_name'}), name='get all name vehicle color'),
    path('vehicles-type', VehicleTypeViewSet.as_view({'get': 'get_all_name'}), name='get all name vehicle type'),
    path('provinces', ProvinceViewSet.as_view({'get': 'get_all_name'}), name='get all name provinces'),
    path('v2/vehicles-type', VehicleTypeViewSet.as_view({'get': 'get_all'}), name='get all name vehicle type'),
    path('v2/vehicles-color', VehicleColorViewSet.as_view({'get': 'get_all'}), name='get all name vehicle color'),
    path('v2/provinces', ProvinceViewSet.as_view({'get': 'get_all'}), name='get all name provinces'),

    path('user-level', userLevelViewSet.as_view({'get': 'get_all_name'}), name='get all name user level'),

    path('dashboard', RecordViewSet.as_view({'get': 'get_dashboard_data'}), name='get dashboard data'),
    path('dashboardTest', RecordViewSet.as_view({'get': 'get_dashboard_data_test'}), name='get dashboard data'),
    path('dashboard-scheduler', RecordViewSet.as_view({'get': 'get_dashboard_data_scheduler'}), name='get dashboard data'),
    path('checkpoint/<checkpoint_id>/<type>', RecordViewSet.as_view({'get': 'get_checkpoint_detail'}), name='get checkpoint detail'),
    path('traffic-detail/<record_type>', RecordViewSet.as_view({'get': 'get_traffic_detail'}), name='get traffic detail'),

    path('blacklists', BlacklistViewSet.as_view({'get': 'get_all'}), name='get list blacklist'),
    path('blacklist', BlacklistViewSet.as_view({'post': 'create'}), name='get list blacklist'),
    path('blacklist/<blacklist_id>', BlacklistViewSet.as_view({'patch': 'update'}), name='get list blacklist'),
    path('blacklist/<blacklist_id>', BlacklistViewSet.as_view({'delete': 'delete'}), name='get list blacklist'),
    path('vehicle-search', VehiclePassViewSet.as_view({'get': 'get_search'}), name='get list vehicle'),
    path('v2/vehicle-search', VehiclePassViewSet.as_view({'get': 'get_filter'}), name='get list vehicle'),
    path('vehicle/<vehicle_passing_id>/report', VehiclePassViewSet.as_view({'get': 'get_one_report'}), name='get report vehicle'),
    path('vehicle-violation-search', VehiclePassViewSet.as_view({'get': 'get_violation_search'}), name='get list violation vehicle'),
    path('vehicle-violation/<vehicle_passing_id>/report', VehiclePassViewSet.as_view({'get': 'get_one_violation_report'}), name='get report violation vehicle'),
    path('violation-playback/<passing_id>', violationPayback.camerafeed),

    # v2 vehicle
    path('v2/vehicle-filter', VehiclePassViewSet.as_view({'get': 'filter'}), name='get filter vehicle'),
    path('v3/vehicle-search', VehiclePassViewSet.as_view({'get': 'search'}), name='get list vehicle'),
    path('vehicle-report', VehiclePassViewSet.as_view({'post': 'get_report'}), name='get list vehicle report'),
    path('vehicle-report-detail', VehiclePassViewSet.as_view({'post': 'get_report_detail'}), name='get detail vehicle report'),

    path('vehicle-destination-times', VehiclePassViewSet.as_view({'get': 'search_origin_destination_time'}), name='get time vehicle origin and destination'),
    path('vehicle-destination-list/<type>', VehiclePassViewSet.as_view({'get': 'get_search_origin_destination'}), name='get list vehicle origin and destination'),
    # path('vehicle-destination/<vehicle_passing_id>/report', VehiclePassViewSet.as_view({'get': 'get_origin_destination_report'}), name='get list vehicle origin and destination'),

    path('blacklist-search', BlacklistPassViewSet.as_view({'get': 'get_search'}), name='get list vehicle'),
    path('blacklist/<blacklist_passing_id>/passing', BlacklistPassViewSet.as_view({'get': 'get_one'}), name='get blacklist passing'),
    path('blacklist/<blacklist_passing_id>/report', BlacklistPassViewSet.as_view({'get': 'get_one_report'}), name='get report blacklist'),
    path('blacklist-playback', blacklistPlayback.camerafeed),
    path('blacklist-check', BlacklistPassViewSet.as_view({'get': 'check_blacklist'}), name='count blacklist'),
    path('blacklist-status/<id>', BlacklistPassViewSet.as_view({'get': 'update_status'}), name='update status blacklist'),

    path('truck-search', TruckPassViewSet.as_view({'get': 'get_search'}), name='get list vehicle'),
    path('truck/<truck_passing_id>/passing', TruckPassViewSet.as_view({'get': 'get_one'}), name='get blacklist passing'),
    path('truck/<truck_passing_id>/report', TruckPassViewSet.as_view({'get': 'get_one_report'}), name='get report blacklist'),

    path('traffic-view/live-sample', TrafficViewViewSet.as_view({'get': 'get_live_view_sample'}), name='testing'),
    path('traffic-view/checkpoint-camera', TrafficViewViewSet.as_view({'get': 'get_checkpoint_cameras'}), name='testing'),
    path('traffic-view/live', TrafficViewViewSet.as_view({'get': 'get_live_view'}), name='testing'),
    path('traffic-view/playback', playback.camerafeed),

    path('devices-status', DeviceStatusViewSet.as_view({'get': 'get_dashboard'}), name='get device status dashboard'),
    path('devices-status/all-sensors', DeviceStatusViewSet.as_view({'get': 'get_all_sensor'}), name='test'),
    path('devices-status/current-alarm', DeviceStatusViewSet.as_view({'get': 'get_current_alarm'}), name='test'),
    path('device-check', DeviceStatusViewSet.as_view({'get': 'check_device'}), name='count device status down'),
    path('camera-status', DeviceStatusViewSet.as_view({'get': 'get_camera_status'}), name='get camera all status'),

    path('device-status/<checkpoint_id>', DeviceStatusViewSet.as_view({'get': 'get_checkpoint_status'}), name='get device status dashboard'),
    path('device-status/all-sensors/<checkpoint_id>', DeviceStatusViewSet.as_view({'get': 'get_all_sensor_by_checkpoint'}), name='get device status dashboard'),
    path('device-status/current-alarm/<checkpoint_id>', DeviceStatusViewSet.as_view({'get': 'get_current_alarm_by_checkpoint'}), name='get device status dashboard'),

    path('report-bkk', BkkReportViewSet.as_view({'get': 'get_report'}), name='get report superuser'),

    path('date-record-insert',ManualViewSet.as_view({'post': 'record_insert'}), name='insert daily record'),
    path('date-violation-insert',ManualViewSet.as_view({'post': 'violation_insert'}), name='insert daily violation'),

    # report bkk v2
    path('report-bkk-2/daily', BkkReport2ViewSet.as_view({'get': 'daily'}), name='get report daily'),
    path('report-bkk-2/weekly', BkkReport2ViewSet.as_view({'get': 'weekly'}), name='get report weekly'),
    path('report-bkk-2/monthly', BkkReport2ViewSet.as_view({'get': 'monthly'}), name='get report monthly'),
    path('report-bkk-2/yearly', BkkReport2ViewSet.as_view({'get': 'yearly'}), name='get report yearly'),

    path('record-url', RecordViewSet.as_view({'get': 'get_record_url'}), name='get record url'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
