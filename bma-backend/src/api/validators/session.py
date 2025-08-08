from api.repositories.login import LoginRepository
from api.repositories.user import UserRepository
from api.logics.session import SessionLogic

from rest_framework.exceptions import ParseError

import datetime

class SessionValidator:
    def __init__(self):
        self.login_repo = LoginRepository()
        self.user_repo = UserRepository()
        self.session_logic = SessionLogic()

        self.__format = '%Y-%m-%d %H:%M:%S'
        self.__payloads_format = [
            {
                'name': 'id',
                'type': int
            },
            {
                'name': 'user_id',
                'type': int
            },
            {
                'name': 'created_at',
                'type': str
            }
        ]

        self.session_invalid_msg = 'invalid session format'
        self.session_required_msg = 'session required'
        self.validate_fail_msg = 'invalid session data'
        self.session_timeout = 'session timeout'

    
    def __payload_key_error(self, payloads, key):
        if key not in payloads:
            response = {
                'status_code': 400,
                'message': self.session_invalid_msg
            }

            raise ParseError(response)


    def __payloads_type_error(self, value, type_):
        if type(value) != type_:
            response = {
                'status_code': 400,
                'message': self.session_invalid_msg
            }

            raise ParseError(response)


    def __validate_payloads_format(self, payloads):
        for item in self.__payloads_format:
            name = item['name']
            type_ = item['type']
            value = payloads[name]

            self.__payload_key_error(payloads=payloads, key=name)
            self.__payloads_type_error(value=value, type_=type_)


    def __validate_headers(self, headers):
        if 'session' not in headers:
            response = {
                'status_code': 400,
                'message': self.session_required_msg
            }

            raise ParseError(response)
        
        session = headers['session']
        
        return session


    def __validate_created_at_data(self, created_at, data):
        if created_at != data['created_at']:
            response = {
                'status_code': 400,
                'message': self.validate_fail_msg
            }

            raise ParseError(response)


    def __validate_is_expired(self, current, data):
        if current > data['expired_at']:
            response = {
                'status_code': 400,
                'message': self.session_timeout
            }
            
            raise ParseError(response)


    def __validate_payloads_data(self, payloads):
        login_id = payloads['id']
        user_id = payloads['user_id']

        created_at = datetime.datetime.strptime(payloads['created_at'], self.__format)
        current = datetime.datetime.now()

        data = self.login_repo.validate_session(id=login_id, msg=self.validate_fail_msg)
        self.user_repo.validate_session(id=user_id, msg=self.validate_fail_msg)
        self.__validate_created_at_data(created_at=created_at, data=data)
        self.__validate_is_expired(current=current, data=data)


    def validate_session(self, headers):
        session = self.__validate_headers(headers=headers)
        
        payloads = self.session_logic.get_payloads(session=session)

        self.__validate_payloads_format(payloads=payloads)
        self.__validate_payloads_data(payloads=payloads)

        return payloads