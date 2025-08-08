from api.repositories.user import UserRepository
from api.repositories.group import GroupRepository
from api.repositories.permission import PermissionRepository
import datetime
from rest_framework.exceptions import NotFound,ParseError
from argon2 import PasswordHasher

class SystemConfigValidator:

    def __init__(self):
        self.user_repo = UserRepository()
        self.group_repo = GroupRepository()
        self.permission_repo = PermissionRepository()

        self.not_have_permission_msg = 'not have permission'

    def validate_user_id(self, params):
        if 'id' not in params:
            response = {
                'status_code': 400,
                'message': 'id required'
            }

            raise ParseError(response)

        id = params.get('id')

        return id

    def validate_user_level_id(self, params):
        if 'id' not in params:
            response = {
                'status_code': 400,
                'message': 'user level id required'
            }

            raise ParseError(response)

        id = params.get('id')

        return id


    def validate_user_name(self, params):
        if 'name' not in params:
            name = ''
        else:
            name = params.get('name')
        
        return name

    def validate_user_password(self, params):
        if 'password' not in params:
            password = ''
        else:
            ph = PasswordHasher()
            password = params.get('password')
            password = ph.hash(password)
        
        return password

    def validate_user_email(self, params):
        if 'email' not in params:
            email = ''
        else:
            email = params.get('email')
        
        return email
    
    def validate_user_phone(self, params):
        if 'phone' not in params:
            phone = ''
        else:
            phone = params.get('phone')
        
        return phone

    def validate_user_address(self, params):
        if 'address' not in params:
            address = ''
        else:
            address = params.get('address')
        
        return address

    def validate_user_group(self, params):
        if 'group' not in params:
            group = ''
        else:
            group = params.get('group')
        
        return group

    def validate_user_super_user(self, params):
        if 'is_super_user' not in params:
            superuser = ''
        else:
            superuser = params.get('is_super_user')
        
        return superuser

    def validate_add_group_name(self, params):
        if 'name' not in params:
            response = {
                'status_code': 400,
                'message': 'name required'
            }

            raise ParseError(response)
        else:
            name = params.get('name')
        
        return name
        

    def validate_add_group_level(self, params):
        if 'user_level_id' not in params:
            response = {
                'status_code': 400,
                'message': 'user level required'
            }

            raise ParseError(response)
        else:
            grouplevel = params.get('user_level_id')
        
        return grouplevel

    def validate_edit_group_level(self, params):
        if 'user_level_id' not in params:
            grouplevel = ''
        else:
            grouplevel = params.get('user_level_id')
        
        return grouplevel
    
    def validate_add_department_id(self, params):
        if 'department_id' not in params:
            response = {
                'status_code': 400,
                'message': 'department id required'
            }

            raise ParseError(response)
        else:
            department_id = params.get('department_id')
        
        return department_id

    def validate_edit_user_level_name(self, params):
        if 'name' not in params:
            name = ''
        else:
            name = params.get('name')
        
        return name

    def validate_menu(self,params):
        if 'menu' not in params:
            menu = ''
        else:
            menu = params.get('menu')
        return menu

    def validate_edit_menu(self,params):
        if 'menu' not in params:
            menu = []
        else:
            menu = params.get('menu')
        return menu

    def validate_requirment(self,params,name):
        if name not in params:
            response = {
                'status_code': 400,
                'message': '{} required'.format(name)
            }

            raise ParseError(response)
        else:
            result = params.get(name)
        return result

    def validate_non_requirment(self,params,name):
        if name not in params:
            result = ''
        else:
            result = params.get(name)
        return result
    
    def validate_request_edit_user(self,params):
        id = self.validate_user_id(params=params)
        name = self.validate_user_name(params=params)
        password = self.validate_user_password(params=params)
        email = self.validate_user_email(params=params)
        phone = self.validate_user_phone(params=params)
        address = self.validate_user_address(params=params)
        group = self.validate_user_group(params=params)
        is_super_user = self.validate_user_super_user(params=params)
        
            
        payloads = {
            'id': id,
            'name': name,
            'password': password,
            'email': email,
            "phone": phone,
            "home_address": address,
            "group_id": group,
            "is_super_user" :is_super_user
        }


        return payloads

    def validate_request_add_group_user(self,params):
        name = self.validate_add_group_name(params=params)
        department_id = self.validate_add_department_id(params=params)
        group_level_id = self.validate_add_group_level(params=params)
            
        payloads = {
            'name': name,
            'department_id': department_id,
            'user_level_id': group_level_id
        }


        return payloads

    def validate_request_edit_group_user(self,params):
        id = self.validate_user_id(params=params)
        name = self.validate_user_name(params=params)
        grouplevel = self.validate_edit_group_level(params=params)
        
            
        payloads = {
            'id': id,
            'name': name,
            'user_level_id': grouplevel
        }


        return payloads

    
    def validate_request_del_user(self,params):
        
        id = self.validate_user_id(params=params)
        if id == 1:
            response = {
                'status_code': 400,
                'message': 'cannot delete super admin'
            }

            raise ParseError(response)
            
        payloads = {
            'id': id
        }


        return payloads

    def validate_request_add_user_level(self,params):
        level_name = self.validate_add_group_name(params=params)
        menu = self.validate_menu(params=params)
        
            
        payloads = {
            'name': level_name,
            'menu':menu
        }


        return payloads

    def validate_request_edit_user_level(self,params):
        id = self.validate_user_level_id(params=params)
        level_name = self.validate_edit_user_level_name(params=params)
        menu = self.validate_edit_menu(params=params)
        
            
        payloads = {
            'id': id,
            'name':level_name,
            'menu':menu
        }


        return payloads

    def validate_request_add_checkpoint(self,params):
        checkpoint_id = self.validate_requirment(params=params,name='checkpoint_id')
        checkpoint_code = self.validate_requirment(params=params,name='checkpoint_code')
        checkpoint_name = self.validate_requirment(params=params,name='checkpoint_name')
        speedlimit = self.validate_requirment(params=params,name='speedlimit')
        latitude = self.validate_requirment(params=params,name='latitude')
        longtitude = self.validate_requirment(params=params,name='longtitude')
        road_id = self.validate_requirment(params=params,name='road_id')
        district_id = self.validate_requirment(params=params,name='district_id')
        road_condition_id = self.validate_non_requirment(params=params,name='road_condition_id')
        checkpoint_nameth = self.validate_requirment(params=params,name='checkpoint_nameth')
        checkpoint_nickname = self.validate_requirment(params=params,name='checkpoint_nickname')
        area_code = self.validate_requirment(params=params,name='area_code')
        project_id = self.validate_requirment(params=params,name='project_id')
        
        payloads = {
            'checkpoint_id': checkpoint_id,
            'checkpoint_code':checkpoint_code,
            'checkpoint_name':checkpoint_name,
            'speedlimit':speedlimit,
            'latitude':latitude,
            'longtitude':longtitude,
            'road_id':road_id,
            'district_id':district_id,
            'road_condition_id':road_condition_id,
            'checkpoint_nameth':checkpoint_nameth,
            'checkpoint_nickname':checkpoint_nickname,
            'area_code':area_code,
            'project_id':project_id,
        }


        return payloads

    
    def validate_request_edit_checkpoint(self,params):
        checkpoint_id = self.validate_requirment(params=params,name='checkpoint_id')
        checkpoint_code = self.validate_non_requirment(params=params,name='checkpoint_code')
        checkpoint_name = self.validate_non_requirment(params=params,name='checkpoint_name')
        speedlimit = self.validate_non_requirment(params=params,name='speedlimit')
        latitude = self.validate_non_requirment(params=params,name='latitude')
        longtitude = self.validate_non_requirment(params=params,name='longtitude')
        road_id = self.validate_non_requirment(params=params,name='road_id')
        district_id = self.validate_non_requirment(params=params,name='district_id')
        road_condition_id = self.validate_non_requirment(params=params,name='road_condition_id')
        checkpoint_nameth = self.validate_non_requirment(params=params,name='checkpoint_nameth')
        checkpoint_nickname = self.validate_non_requirment(params=params,name='checkpoint_nickname')
        area_code = self.validate_non_requirment(params=params,name='area_code')
        project_id = self.validate_non_requirment(params=params,name='project_id')
        
        payloads = {
            'checkpoint_id': checkpoint_id,
            'checkpoint_code':checkpoint_code,
            'checkpoint_name':checkpoint_name,
            'speedlimit':speedlimit,
            'latitude':latitude,
            'longtitude':longtitude,
            'road_id':road_id,
            'district_id':district_id,
            'road_condition_id':road_condition_id,
            'checkpoint_nameth':checkpoint_nameth,
            'checkpoint_nickname':checkpoint_nickname,
            'area_code':area_code,
            'project_id':project_id,
        }


        return payloads

    def validate_request_add_camera(self,params):
        camera_id = self.validate_requirment(params=params,name='camera_id')
        camera_name = self.validate_requirment(params=params,name='camera_name')
        camera_code = self.validate_requirment(params=params,name='camera_code')
        model = self.validate_non_requirment(params=params,name='model')
        ip = self.validate_requirment(params=params,name='ip')
        checkpoint_id = self.validate_requirment(params=params,name='checkpoint_id')
        serial = self.validate_non_requirment(params=params,name='serial')
        brand = self.validate_requirment(params=params,name='brand')
        bma_code = self.validate_requirment(params=params,name='bma_code')
        is_sample = self.validate_requirment(params=params,name='is_sample')
        hls = self.validate_requirment(params=params,name='hls')
        type = self.validate_requirment(params=params,name='type')
        
        payloads = {
            'camera_id': camera_id,
            'camera_name':camera_name,
            'camera_code':camera_code,
            'model':model,
            'ip':ip,
            'checkpoint_id':checkpoint_id,
            'serial':serial,
            'brand':brand,
            'bma_code':bma_code,
            'is_sample':is_sample,
            'hls':hls,
            'type':type
        }


        return payloads
        
    def validate_request_edit_camera(self,params):
        camera_id = self.validate_requirment(params=params,name='camera_id')
        camera_name = self.validate_non_requirment(params=params,name='camera_name')
        camera_code = self.validate_non_requirment(params=params,name='camera_code')
        model = self.validate_non_requirment(params=params,name='model')
        ip = self.validate_non_requirment(params=params,name='ip')
        checkpoint_id = self.validate_non_requirment(params=params,name='checkpoint_id')
        serial = self.validate_non_requirment(params=params,name='serial')
        brand = self.validate_non_requirment(params=params,name='brand')
        bma_code = self.validate_non_requirment(params=params,name='bma_code')
        is_sample = self.validate_non_requirment(params=params,name='is_sample')
        hls = self.validate_non_requirment(params=params,name='hls')
        type = self.validate_non_requirment(params=params,name='type')
        
        payloads = {
            'camera_id': camera_id,
            'camera_name':camera_name,
            'camera_code':camera_code,
            'model':model,
            'ip':ip,
            'checkpoint_id':checkpoint_id,
            'serial':serial,
            'brand':brand,
            'bma_code':bma_code,
            'is_sample':is_sample,
            'hls':hls,
            'type':type
        }


        return payloads

    def validate_request_add_road(self,params):
        road_id = self.validate_requirment(params=params,name='road_id')
        road_code = self.validate_requirment(params=params,name='road_code')
        from_section = self.validate_requirment(params=params,name='from_section')
        to_section = self.validate_requirment(params=params,name='to_section')
        road_name = self.validate_requirment(params=params,name='road_name')
       
        payloads = {
            'road_id': road_id,
            'road_code':road_code,
            'from_section':from_section,
            'to_section':to_section,
            'road_name':road_name
        }


        return payloads

    def validate_request_edit_road(self,params):
        road_id = self.validate_requirment(params=params,name='road_id')
        road_code = self.validate_non_requirment(params=params,name='road_code')
        from_section = self.validate_non_requirment(params=params,name='from_section')
        to_section = self.validate_non_requirment(params=params,name='to_section')
        road_name = self.validate_non_requirment(params=params,name='road_name')
       
        payloads = {
            'road_id': road_id,
            'road_code':road_code,
            'from_section':from_section,
            'to_section':to_section,
            'road_name':road_name
        }


        return payloads

    
    def validate_request_add_lane(self,params):
        lane_id = self.validate_requirment(params=params,name='lane_id')
        lane_code = self.validate_requirment(params=params,name='lane_code')
        lane_name = self.validate_requirment(params=params,name='lane_name')
        road_direction = self.validate_requirment(params=params,name='road_direction')
        road_id = self.validate_requirment(params=params,name='road_id')
        camera_id = self.validate_requirment(params=params,name='camera_id')
        checkpoint_id = self.validate_requirment(params=params,name='checkpoint_id')
        payloads = {
            'lane_id': lane_id,
            'lane_code':lane_code,
            'lane_name':lane_name,
            'road_direction':road_direction,
            'road_id':road_id,
            'camera_id':camera_id,
            'checkpoint_id':checkpoint_id
        }


        return payloads

    def validate_request_edit_lane(self,params):
        lane_id = self.validate_requirment(params=params,name='lane_id')
        lane_code = self.validate_non_requirment(params=params,name='lane_code')
        lane_name = self.validate_non_requirment(params=params,name='lane_name')
        road_direction = self.validate_non_requirment(params=params,name='road_direction')
        road_id = self.validate_non_requirment(params=params,name='road_id')
        camera_id = self.validate_non_requirment(params=params,name='camera_id')
        checkpoint_id = self.validate_non_requirment(params=params,name='checkpoint_id')
        payloads = {
            'lane_id': lane_id,
            'lane_code':lane_code,
            'lane_name':lane_name,
            'road_direction':road_direction,
            'road_id':road_id,
            'camera_id':camera_id,
            'checkpoint_id':checkpoint_id
        }


        return payloads

    def validate_time_format(self,params):
        starttime = self.validate_requirment(params=params,name='starttime')
        endtime = self.validate_requirment(params=params,name='endtime')
        payloads = {
            'starttime':starttime,
            'endtime':endtime
        }
        return payloads

        