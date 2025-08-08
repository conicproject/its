from api.models.menu import MenuModel
from api.connections.oracle import OracleConnection
from rest_framework.exceptions import NotFound
import pandas as pd

class MenuRepository:

    def __init__(self):
        self.oracle_connection = OracleConnection().get_connection()

    def get_all(self):
        data = MenuModel.objects.all()

        return data

    def get_all_menu(self):
        sql_command = """
            SELECT ID,NAME  FROM BMA_PHASE_II.MENUS m  
        """

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        try:
            columes = [row[0] for row in cursor.description]
            df = pd.DataFrame(data=data, columns=columes)
            df = df.rename(columns={
                'ID': 'id',
                'NAME': 'name'
            })

            result = df.to_dict('records')
            data = result

        except:
            response = {
                'status_code': 404,
                'message': self.not_found_msg
            }

            raise NotFound(response)
        
        return data


    def get_by_list_id(self, ids):
        # concentrate string
        query = "("
        for item in ids[:-1]:
            query = query + str(item)+","

        query = query + str(ids[-1])
        query += ")"

        sql_command = """
            SELECT * FROM BMA_PHASE_II.MENUS
            WHERE ID IN {}
        """.format(query)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        columns = cursor.description 
        result = [{columns[index][0].lower():column for index, column in enumerate(value)} for value in cursor.fetchall()]

        # data = MenuModel.objects.filter(id__in=ids)

        return result


    def get_super_user_menu(self):
        data = MenuModel.objects.get(for_super_user=True)

        return data