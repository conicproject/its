from rest_framework.exceptions import ParseError
from api.repositories.oracleCheckpoint import OracleCheckpointRepository

class TrafficViewValidator:
    def __init__(self):
        self.checkpoint_repo = OracleCheckpointRepository()
        self.time_string = '.000+07:00'
    

    def validate_value(self, checkpoint_id):
        try:
            checkpoint_id = int(checkpoint_id)
        except:
            response = {
                'status_code': 400,
                'message': 'incorrected value'
            }

            raise ParseError(response)
        
        return checkpoint_id
    

    def validate_checkpoint_field(self, params):
        if 'checkpoint' not in params:
            response = {
                'status_code': 400,
                'message': 'checkpoint field required'
            }

            raise ParseError(response)
        
        checkpoint = params.get('checkpoint')

        return checkpoint


    def validate_camera_field(self, params):
        if 'camera' not in params:
            response = {
                'status_code': 400,
                'message': 'camera field required'
            }

            raise ParseError(response)
        
        camera = params.get('camera')

        return camera


    def validate_start_time_field(self, params):
        if 'start_time' not in params:
            response = {
                'status_code': 400,
                'message': 'start time field required'
            }

            raise ParseError(response)
        
        start_time = params.get('start_time')

        return start_time


    def validate_end_time_field(self, params):
        if 'end_time' not in params:
            response = {
                'status_code': 400,
                'message': 'end time field required'
            }

            raise ParseError(response)
        
        end_time = params.get('end_time')

        return end_time


    def validate_request_sample(self, params):
        checkpoint = self.validate_checkpoint_field(params=params)
        checkpoint_id = self.validate_value(
            checkpoint_id=checkpoint
        )
        self.checkpoint_repo.get_by_id(id=checkpoint_id)

        return checkpoint_id


    def validate_request(self, params):
        checkpoint = self.validate_checkpoint_field(params=params)
        camera_code = self.validate_camera_field(params=params)
        checkpoint_id = self.validate_value(
            checkpoint_id=checkpoint
        )
        self.checkpoint_repo.get_by_id(id=checkpoint_id)

        return checkpoint_id, camera_code



    def validate_checkpoint_field_playback(self, params):
        if 'checkpoint' not in params:
            response = {
                'status_code': 400,
                'message': 'checkpoint field required'
            }

            raise ParseError(response)
        
        checkpoint = params['checkpoint']

        return checkpoint


    def validate_camera_field_playback(self, params):
        if 'camera' not in params:
            response = {
                'status_code': 400,
                'message': 'camera field required'
            }

            raise ParseError(response)
        
        camera = params['camera']

        return camera


    def validate_start_time_field_playback(self, params):
        if 'start_time' not in params:
            response = {
                'status_code': 400,
                'message': 'start time field required'
            }

            raise ParseError(response)
        
        start_time = params['start_time']

        return start_time


    def validate_end_time_field_playback(self, params):
        if 'end_time' not in params:
            response = {
                'status_code': 400,
                'message': 'end time field required'
            }

            raise ParseError(response)
        
        end_time = params['end_time']

        return end_time


    def validate_request_playback(self, params):
        checkpoint = self.validate_checkpoint_field_playback(params=params)
        camera_code = self.validate_camera_field_playback(params=params)
        start_time = self.validate_start_time_field_playback(params=params)
        end_time = self.validate_end_time_field_playback(params=params)

        checkpoint_id = self.validate_value(
            checkpoint_id=checkpoint
        )
        self.checkpoint_repo.get_by_id(id=checkpoint_id)

        start_time = start_time + self.time_string
        end_time = end_time + self.time_string

        return checkpoint_id, camera_code, start_time, end_time