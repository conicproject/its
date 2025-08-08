from rest_framework.exceptions import ParseError

import datetime

class BlacklistValidator:
    def __init__(self):
        self.format = '%Y-%m-%d'

        self.incorrect_time_format = 'incorrect format'
        self.incorrect_time_value = 'incorrect value'


    def validate_license_plate_field(self, params):
        if 'license_plate' not in params:
            response = {
                'status_code': 400,
                'message': 'license plate field required'
            }

            raise ParseError(response)
        
        license_plate = params.get('license_plate')

        return license_plate


    def validate_request(self, params):
        license_plate = self.validate_license_plate_field(params=params)
        now = datetime.datetime.now()
        today = now.strftime(self.format)

        payloads = {
            'license_plate': license_plate,
            'province': params.get('province'),
            'color': params.get('color'),
            'type': params.get('type'),
            'note': params.get('note'),
            'date': today
        }

        return payloads


    def validate_blacklist_id(self, id):
        try:
            blacklist_id = int(id)

        except:
            response = {
                'status_code': 400,
                'message': 'invalid value'
            }

            raise ParseError(response)
