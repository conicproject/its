from api.repositories.user import UserRepository
from api.repositories.group import GroupRepository
from api.repositories.permission import PermissionRepository

from rest_framework.exceptions import NotFound

class UserPermissionValidator:

    def __init__(self):
        self.user_repo = UserRepository()
        self.group_repo = GroupRepository()
        self.permission_repo = PermissionRepository()

        self.not_have_permission_msg = 'not have permission'
    

    def __validate_permission_menus(self, list_menu):
        if not list_menu:
            response = {
                'status_code': 404,
                'message': self.not_have_permission_msg
            }

            raise NotFound(response)


    def list_accessible_menu(self, user_id):
        user = self.user_repo.get_by_id(id=user_id)
        group = self.group_repo.get_by_id(id=user["group_id"])
        
        
        list_menu = self.permission_repo.get_menulist_by_group(user_level_id=group["user_level_id"])

        self.__validate_permission_menus(list_menu=list_menu)

        return list_menu


    def validate_user_permission(self, user_id, menu_id):
        user = self.user_repo.get_by_id(id=user_id)
        group = self.group_repo.get_by_id(id=user["group_id"])
        self.permission_repo.validate_permission(user_level_id=group["user_level_id"], menu_id=menu_id)