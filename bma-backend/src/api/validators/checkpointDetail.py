from rest_framework.exceptions import ParseError
from api.repositories.oracleCheckpoint import OracleCheckpointRepository

class CheckpointDetailValidator:
    def __init__(self):
        self.checkpoint_repo = OracleCheckpointRepository()
    

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


    def validate_checkpoint_id(self, checkpoint_id):
        checkpoint_id = self.validate_value(
            checkpoint_id=checkpoint_id
        )
        self.checkpoint_repo.get_by_id(id=checkpoint_id)

        return checkpoint_id 