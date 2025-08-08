from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError, PermissionDenied

from argon2 import PasswordHasher
import pandas as pd
from api.models.user import UserModel
from api.validators.session import SessionValidator
from api.repositories.user import UserRepository
from api.validators.systemConfig import SystemConfigValidator
from api.repositories.userLevel import userLevel
from api.repositories.permission import PermissionRepository

class UserViewSet(viewsets.ViewSet):

    def __init__(self):
        self.session_validator = SessionValidator()
        self.user_repo = UserRepository()
        self.system_config = SystemConfigValidator()
        self.userLevel_repo = userLevel()
        self.permission_repo = PermissionRepository()

    # def create(self, request):
    #     payloads = self.session_validator.validate_session(
    #         headers=request.headers
    #     )
    #     user = self.user_repo.get_by_id(id=payloads['user_id'])
    #     is_super_user = user.is_super_user

    #     if not is_super_user:
    #         response = {
    #             'status_code': 403,
    #             'message': 'permission denied'
    #         }

    #         raise PermissionDenied(response)

    #     ######## validate payload ##########
    #     if 'username' not in request.data:
    #         response = {
    #             'status_code': 400,
    #             'message': 'usernmae field required'
    #         }
            
    #         raise ParseError(response)

    #     if 'password' not in request.data:
    #         response = {
    #             'status_code': 400,
    #             'message': 'password field required'
    #         }
            
    #         raise ParseError(response)

    #     if 'group' not in request.data:
    #         response = {
    #             'status_code': 400,
    #             'message': 'group field required'
    #         }
            
    #         raise ParseError(response)

    #     username = request.data['username']
    #     password = request.data['password']

    #     ## 
    #     try:
    #         group_id = int(request.data['group'])

    #     except:
    #         response = {
    #             'status_code': 400,
    #             'message': 'group field invalid value'
    #         }

    #         raise ParseError(response)

    #     try:
    #         data = UserModel.objects.get(name=username)
    #         response = {
    #             'status_code': 400,
    #             'message': 'username have been used'
    #         }

    #         raise ParseError(response)

    #     except UserModel.DoesNotExist:
    #         pass
   
    #     ph = PasswordHasher()
    #     hash = ph.hash(password)

    #     user = UserModel(
    #         name=username,
    #         password=hash,
    #         group_id=group_id
    #     )

    #     user.save()

    #     response = {
    #         'status_code': 201,
    #         'message': 'create success'
    #     }

    #     return Response(response, status=status.HTTP_201_CREATED)

    def get_user(self, request):
        print("request", request.headers)
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

        user = self.user_repo.get_by_id(id=payloads['user_id'])
        is_super_user = user['is_super_user']

        if not is_super_user:
            response = {
                'status_code': 403,
                'message': 'permission denied'
            }

            raise PermissionDenied(response)
        
        dataUser = {
            'id': user['id'],
            'username': user['name'],
            'group_id': user['group_id'],
        }

        response = {
            'status_code': 200,
            'message': 'get success',
            'data': dataUser
        }

        return Response(response, status=status.HTTP_200_OK)

    def add_user(self, request):

        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

       
        user = self.user_repo.get_by_id(id=payloads['user_id'])
        
        is_super_user = user['is_super_user']
        
        if not is_super_user:
            response = {
                'status_code': 403,
                'message': 'permission denied'
            }

            raise PermissionDenied(response)

        input_user = request.data

        for k in input_user.keys():
            if input_user[k] == "":
                response = {
                'status_code': 400,
                'message': 'Bad Request',
                
                }

                raise PermissionDenied(response)

        print("---test---",request.data["name"])

        data = self.user_repo.insert(
            payloads=input_user
        )
        response = {
            'status_code': 200,
            'message': 'get success',
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)

    def edit_user(self, request):

        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

       
        check_user = self.user_repo.get_by_id(id=payloads['user_id'])
        
        is_super_user = check_user['is_super_user']
        
        if not is_super_user:
            response = {
                'status_code': 403,
                'message': 'permission denied'
            }

            raise PermissionDenied(response)
        
        user = self.system_config.validate_request_edit_user(
            params= request.data
        )
        except_key = 'id'
        query_string = ''
        for key in user:
            if user[key] != '' and key not in except_key:
                if type(user[key]) == str:
                    query_string = query_string + "{} = '{}',".format(key,user[key])
                else:
                    query_string = query_string + "{} = {},".format(key,user[key])
            

        query_string = query_string[:-1]
        
        data = self.user_repo.edit(
            payloads=user,
            query=query_string
        )

        response = {
            'status_code': 200,
            'message': 'get success',
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)

    def del_user(self, request):

        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

       
        check_user = self.user_repo.get_by_id(id=payloads['user_id'])
        
        is_super_user = check_user['is_super_user']
        
        if not is_super_user:
            response = {
                'status_code': 403,
                'message': 'permission denied'
            }

            raise PermissionDenied(response)
        
        user = self.system_config.validate_request_del_user(
            params= request.data
        )
        data = self.user_repo.delete(payloads=user)

        response = {
            'status_code': 200,
            'message': 'get success',
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)

    def list_user(self, request):

        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

       
        check_user = self.user_repo.get_by_id(id=payloads['user_id'])
        
        is_super_user = check_user['is_super_user']
        
        if not is_super_user:
            response = {
                'status_code': 403,
                'message': 'permission denied'
            }

            raise PermissionDenied(response)

        user = self.user_repo.get_all()

        response = {
            'status_code': 200,
            'message': 'get success',
            'data': user
        }

        return Response(response, status=status.HTTP_200_OK)

    def get_group_department(self, request):

        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

       
        check_user = self.user_repo.get_by_id(id=payloads['user_id'])
        
        is_super_user = check_user['is_super_user']
        
        if not is_super_user:
            response = {
                'status_code': 403,
                'message': 'permission denied'
            }

            raise PermissionDenied(response)

        data = self.user_repo.get_all_group_department()
        df = pd.DataFrame(data)
        result = df.groupby("department_name").apply(lambda x: x.set_index("group_name")['group_id'].to_dict()).to_dict()
        
        
        response = {
            'status_code': 200,
            'message': 'get success',
            'data': result
        }

        return Response(response, status=status.HTTP_200_OK)

    def get_department(self,request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

        check_user = self.user_repo.get_by_id(id=payloads['user_id'])
        
        is_super_user = check_user['is_super_user']
        
        if not is_super_user:
            response = {
                'status_code': 403,
                'message': 'permission denied'
            }

            raise PermissionDenied(response)

        data = self.user_repo.get_department()
        
        response = {
                'status_code': 200,
                'message': 'get success',
                'data': data
            }

        return Response(response, status=status.HTTP_200_OK)

    def get_user_level(self,request):
        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

        check_user = self.user_repo.get_by_id(id=payloads['user_id'])
        
        is_super_user = check_user['is_super_user']
        
        if not is_super_user:
            response = {
                'status_code': 403,
                'message': 'permission denied'
            }

            raise PermissionDenied(response)

        data = self.user_repo.get_user_level()
        
        response = {
                'status_code': 200,
                'message': 'get success',
                'data': data
            }

        return Response(response, status=status.HTTP_200_OK)

    def list_group_user(self, request):

        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

       
        check_user = self.user_repo.get_by_id(id=payloads['user_id'])
        
        is_super_user = check_user['is_super_user']
        
        if not is_super_user:
            response = {
                'status_code': 403,
                'message': 'permission denied'
            }

            raise PermissionDenied(response)

        user = self.user_repo.get_group_user()

        response = {
            'status_code': 200,
            'message': 'get success',
            'data': user
        }

        return Response(response, status=status.HTTP_200_OK)

    def add_user_group(self, request):

        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

       
        user = self.user_repo.get_by_id(id=payloads['user_id'])
        
        is_super_user = user['is_super_user']
        
        if not is_super_user:
            response = {
                'status_code': 403,
                'message': 'permission denied'
            }

            raise PermissionDenied(response)

        user = self.system_config.validate_request_add_group_user(
            params= request.data
        )

        data = self.user_repo.insert_group(
            payloads=user
        )
        response = {
            'status_code': 200,
            'message': 'get success',
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)

    def edit_user_group(self, request):

        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

       
        check_user = self.user_repo.get_by_id(id=payloads['user_id'])
        
        is_super_user = check_user['is_super_user']
        
        if not is_super_user:
            response = {
                'status_code': 403,
                'message': 'permission denied'
            }

            raise PermissionDenied(response)
        
        user = self.system_config.validate_request_edit_group_user(
            params= request.data
        )
        except_key = 'id'
        query_string = ''
        for key in user:
            if user[key] != '' and key not in except_key:
                if type(user[key]) == str:
                    query_string = query_string + "{} = '{}',".format(key,user[key])
                else:
                    query_string = query_string + "{} = {},".format(key,user[key])
            

        query_string = query_string[:-1]
        
        data = self.user_repo.edit_group(
            payloads=user,
            query=query_string
        )

        response = {
            'status_code': 200,
            'message': 'get success',
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)

    def del_user_group(self, request):

        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

       
        check_user = self.user_repo.get_by_id(id=payloads['user_id'])
        
        is_super_user = check_user['is_super_user']
        
        if not is_super_user:
            response = {
                'status_code': 403,
                'message': 'permission denied'
            }

            raise PermissionDenied(response)
        data = 'status'
        user = self.user_repo.check_exist_group(
            payloads= request.data
        )
        if user != 0:
            response = {
                'status_code': 400,
                'message': 'this group have been used'
            }

            raise ParseError(response)
        elif user == 0:
            data = self.user_repo.delete_group(id=request.data['id'])

        response = {
            'status_code': 200,
            'message': 'get success',
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)


    def list_user_permission(self, request):

        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

       
        check_user = self.user_repo.get_by_id(id=payloads['user_id'])
        
        is_super_user = check_user['is_super_user']
        
        if not is_super_user:
            response = {
                'status_code': 403,
                'message': 'permission denied'
            }

            raise PermissionDenied(response)

        user = self.userLevel_repo.get_list_user_level()
        user_level = self.userLevel_repo.get_user_level_permission()
        df = pd.DataFrame(user)
        df2 = pd.DataFrame(user_level)
        df2['menu_id'] = df2['menu_id'].astype(str)
        df2 = df2.groupby('id')['menu_id'].apply(','.join).reset_index()
        data = pd.merge(df,df2,on='id',how='left')
        data = data.fillna('')
        for i in range(len(data['menu_id'])):
            if(data['menu_id'][i] != ''):
                arr = data['menu_id'][i].split(',')
                arr = sorted(arr,key=int)
                data['menu_id'][i] = ','.join(arr)
        result = data.to_dict('records')
        response = {
            'status_code': 200,
            'message': 'get success',
            'data': result
        }

        return Response(response, status=status.HTTP_200_OK)

    def add_user_level(self, request):

        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

       
        user = self.user_repo.get_by_id(id=payloads['user_id'])
        
        is_super_user = user['is_super_user']
        
        if not is_super_user:
            response = {
                'status_code': 403,
                'message': 'permission denied'
            }

            raise PermissionDenied(response)

        user = self.system_config.validate_request_add_user_level(
            params= request.data
        )
        data = 'success but menu permission is none'
        try:
            insert_data = self.user_repo.insert_user_level(
                payloads=user
            )
            user_id = self.user_repo.get_user_level_id_by_name(
                payloads=user
            )
            query_string = self.userLevel_repo.query_string_user_level_permission(
                id=user_id,
                payloads=user
            )
            if query_string != '':
                data = self.userLevel_repo.insert_user_level_permission(
                    query=query_string
                )
            response = {
                'status_code': 200,
                'message': 'get success',
                'data': data
            }

        except:
            response = {
                'status_code': 400,
                'message': 'duplicate user name'
            }

            raise ParseError(response)

        

        return Response(response, status=status.HTTP_200_OK)

    
    def edit_user_level(self, request):

        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

       
        user = self.user_repo.get_by_id(id=payloads['user_id'])
        
        is_super_user = user['is_super_user']
        
        if not is_super_user:
            response = {
                'status_code': 403,
                'message': 'permission denied'
            }

            raise PermissionDenied(response)

        user = self.system_config.validate_request_edit_user_level(
            params= request.data
        )
        validate_menu_idx = list(range(1,11))
        if(user['menu'] != []):
            for i in user['menu']:
                if i not in validate_menu_idx:
                    response = {
                        'status_code': 400,
                        'message': 'given menu idx not existing'
                    }

                    raise ParseError(response)
        if(user['name'] != ''):
            data = self.userLevel_repo.edit_user_level_name(
                payloads=user
            )
        data = self.userLevel_repo.update_user_level_permission(
            payloads=user
        )
        response = {
            'status_code': 200,
            'message': 'get success',
            'data': data
        }

        

        return Response(response, status=status.HTTP_200_OK)

    def del_user_level(self, request):

        payloads = self.session_validator.validate_session(
            headers=request.headers
        )

       
        check_user = self.user_repo.get_by_id(id=payloads['user_id'])
        
        is_super_user = check_user['is_super_user']
        
        if not is_super_user:
            response = {
                'status_code': 403,
                'message': 'permission denied'
            }

            raise PermissionDenied(response)
        data = 'status'
        # n_permission_exist = self.userLevel_repo.exist_user_level_permission(
        #     payloads= request.data
        # )
        n_group_exist = self.userLevel_repo.exist_user_level_group(
            payloads= request.data
        )
        if n_group_exist != 0:
            response = {
                'status_code': 406,
                'message': 'level user used in group'
            }

            raise ParseError(response)
        elif n_group_exist == 0:
            data = self.userLevel_repo.delete_user_level(id=request.data['id'])

        response = {
            'status_code': 200,
            'message': 'get success',
            'data': data
        }

        return Response(response, status=status.HTTP_200_OK)

    