from api.validators.userPermission import UserPermissionValidator


class FeatureValidator:

    def __init__(self):
        self.menu_ids= {
            'dashboard': 1,
            'checkpoint': 2,
            'traffic_detail': 3,
            'blacklist-search':4,
            'vehicle-search': 5,
            'vehicle-origin-destination': 6,
            'traffic_view': 7,
            'device_status': 8,
            'report-bkk': 9,
            'system-config':10
        }

        self.user_permission_validator = UserPermissionValidator()
    

    def validate_dashboard(self, user_id):
        self.user_permission_validator.validate_user_permission(
            user_id=user_id, menu_id=self.menu_ids['dashboard']
        )


    def validate_checkpoint(self, user_id):
        self.user_permission_validator.validate_user_permission(
            user_id=user_id, menu_id=self.menu_ids['checkpoint']
        )


    def validate_traffic_detail(self, user_id):
        self.user_permission_validator.validate_user_permission(
            user_id=user_id, menu_id=self.menu_ids['traffic_detail']
        )


    def validate_vehicle_search(self, user_id):
        self.user_permission_validator.validate_user_permission(
            user_id=user_id, menu_id=self.menu_ids['vehicle-search']
        )

    def validate_vehicle_destination_search(self, user_id):
        self.user_permission_validator.validate_user_permission(
            user_id=user_id, menu_id=self.menu_ids['vehicle-origin-destination']
        )


    def validate_traffic_view(self, user_id):
        self.user_permission_validator.validate_user_permission(
            user_id=user_id, menu_id=self.menu_ids['traffic_view']
        )

    def validate_device_status(self, user_id):
        self.user_permission_validator.validate_user_permission(
            user_id=user_id, menu_id=self.menu_ids['device_status']
        )
