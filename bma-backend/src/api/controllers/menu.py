from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from api.repositories.menu import MenuRepository
from api.repositories.user import UserRepository

from api.validators.session import SessionValidator
from api.validators.userPermission import UserPermissionValidator
from api.logics.menuBar import MenuBarLogic

from api.serializers.menu import MenuSerializer
from rest_framework.exceptions import ParseError, PermissionDenied

class MenuViewSet(viewsets.ViewSet):

    def __init__(self):
        self.menu_repo = MenuRepository()
        self.menu_serializer = MenuSerializer
        self.menu_bar_interface = MenuBarLogic()
        self.user_repo = UserRepository()
        
        self.session_validator = SessionValidator()
        self.user_permission_validator = UserPermissionValidator()

        self.get_success_msg = 'request get data success'


    def get_menubar(self, request):
        ## validate
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

        menu_ids = self.user_permission_validator.list_accessible_menu(
            user_id=payloads['user_id']
        )

        user = self.user_repo.get_by_id(id=payloads['user_id'])
        
        group_id = user["group_id"]
        is_super_user = user["is_super_user"]

        ## query & format
        menus = self.menu_repo.get_by_list_id(ids=menu_ids)
        # serializer = self.menu_serializer(menus, many=True)
        # data = self.menu_bar_interface.formatting(menus=serializer.data)
        data = self.menu_bar_interface.formatting(menus=menus)

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)

        if (group_id == 1) and (is_super_user == True ):
            super_user_menu = self.menu_repo.get_super_user_menu()
            super_user_menu_srz = self.menu_serializer(super_user_menu)
            super_user_menu_data = super_user_menu_srz.data

            data.append(super_user_menu_data)

        ## make response
        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)

    def get_list_menu(self, request):
        ## validate
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

        user = self.user_repo.get_by_id(id=payloads['user_id'])
        
        is_super_user = user["is_super_user"]
        
        if not is_super_user:
            response = {
                'status_code': 403,
                'message': 'permission denied'
            }

            raise PermissionDenied(response)

        data = self.menu_repo.get_all_menu()

        response = {
            'status_code': 200,
            'message': self.get_success_msg,
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)
