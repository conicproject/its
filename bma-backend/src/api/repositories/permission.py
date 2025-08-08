from api.models.permission import PermissionModel
from api.connections.oracle import OracleConnection
from rest_framework.exceptions import PermissionDenied

import pandas as pd

from rest_framework.exceptions import NotFound

class PermissionRepository:

    def __init__(self):
        self.oracle_connection = OracleConnection().get_connection()
        self.not_have_permission = 'not have permission'


    def get_menulist_by_group(self, user_level_id):
        sql_command = """
            SELECT MENU_ID  FROM BMA_PHASE_II.PERMISSIONS
            WHERE USER_LEVEL_ID = '{}'
        """.format(user_level_id)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'MENU_ID': 'name'
        })

        result = df['name'].to_list()

        return result

    
    def validate_permission(self, user_level_id, menu_id):
        try:
            sql_command = """
            SELECT *  FROM BMA_PHASE_II.PERMISSIONS
            WHERE USER_LEVEL_ID = '{}' AND MENU_ID = '{}'
            """.format(user_level_id,menu_id)
            cursor = self.oracle_connection.cursor()
            cursor.execute(sql_command)
            data = cursor.fetchall()
            # data = PermissionModel.objects.get(group=group_id, menu=menu_id)
        except PermissionModel.DoesNotExist:
            response = {
                'status_code': 403,
                'message': self.not_have_permission
            }

            raise PermissionDenied(response)
