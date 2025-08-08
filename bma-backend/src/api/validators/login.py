from rest_framework.exceptions import ParseError, AuthenticationFailed

from api.repositories.user import UserRepository
from api.logics.session import SessionLogic

from argon2 import PasswordHasher

class LoginValidator:

    def __init__(self):
        self.user_repo = UserRepository()
        self.session_logic = SessionLogic()

        self.ph = PasswordHasher()

        self.__missing_field_payloads_msg = 'invalid payloads format'
        self.password_fail_msg = 'incorrected password'


    def __validate_payloads(self, payloads):
        if 'name' not in payloads:
            response = {
                'status_code': 400,
                'message': self.__missing_field_payloads_msg
            }

            raise ParseError(response)
        
        if 'password' not in payloads:
            response = {
                'status_code': 400,
                'message': self.__missing_field_payloads_msg
            }

            raise ParseError(response)


    def __validate_password(self, hash, password):
        try:
            self.ph.verify(hash, password)
        except:
            response = {
                'status_code': 403,
                'message': self.password_fail_msg
            }

            raise AuthenticationFailed(response)


    def validate(self, payloads):
        self.__validate_payloads(payloads=payloads)

        name = payloads['name']
        password = payloads['password']

        user = self.user_repo.get_by_name(name=name)
        hash = user['password']
        self.__validate_password(hash=hash, password=password)
        
        return user