from rest_framework.exceptions import ParseError

from argon2 import PasswordHasher
import datetime
import jwt

class SessionLogic:

    def __init__(self):
        self.ph = PasswordHasher()

        self.__secret = 'testing@46890#Project!$'
        self.__format = '%Y-%m-%d %H:%M:%S'
        self.__session_config = {
            'hours': 12,
            'minutes': 0
        }

        self.validate_fail_msg = 'invalid session data'
        self.session_timeout = 'session timeout'


    def __encode_session(self, payloads):
        encoded = jwt.encode(payloads, self.__secret, algorithm="HS256")

        return encoded


    def __decode_session(self, session):
        decoded = jwt.decode(session, self.__secret, algorithms="HS256")

        return decoded
    

    def session_timestamp(self):
        time_now = datetime.datetime.now()
        time_delta = time_now + datetime.timedelta(
            hours=self.__session_config['hours'],
            minutes=self.__session_config['minutes']
        )

        created_at = time_now.strftime(self.__format)
        expired_at = time_delta.strftime(self.__format)

        return created_at, expired_at


    def get_session(self, payloads):
        encoded = self.__encode_session(payloads=payloads)
        data = {
            'session': encoded
        }

        return data


    def get_payloads(self, session):
        decoded = self.__decode_session(session=session)

        return decoded