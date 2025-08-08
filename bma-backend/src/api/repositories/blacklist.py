from api.models.blacklist import BlacklistModel
from api.connections.oracle import OracleConnection
from rest_framework.exceptions import NotFound

import cx_Oracle
import pandas as pd
import math

class BlacklistRepository:

    def __init__(self):
        self.oracle_connection = OracleConnection().get_connection()


    def is_exist(self, id):
        sql_command = '''
            SELECT * FROM BMA_PHASE_II.BLACKLISTS
            WHERE ID = {}
        '''.format(id)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        try:
            columes = [row[0] for row in cursor.description]
            df = pd.DataFrame(data=data, columns=columes)
            df = df.rename(columns={
                'ID': 'id',
                'DEPARTMENT_ID': 'department_id',
                'LICENSE_PLATE': 'license_plate',
                'COLOR': 'color',
                'TYPE': 'type',
                'NOTE': 'note',
                'CREATED_DATE': 'date'
            })

            df = df.replace('None', None)
            result = df.to_dict('records')
            data = result[0]

        except:
            response = {
                'status_code': 404,
                'message': 'Blacklist Not Found'
            }

            raise NotFound(response)
        
        return data

    def get_total(self):
        sql_command = '''
            SELECT COUNT(ID) FROM BMA_PHASE_II.BLACKLISTS
        '''

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        return data

    def get_all(self):
        sql_command = '''
            SELECT ID, DEPARTMENT_ID, LICENSE_PLATE, COLOR, TYPE, NOTE FROM BMA_PHASE_II.BLACKLISTS
            ORDER BY ID
        '''

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
    
        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'ID': 'id',
            'DEPARTMENT_ID': 'department_id',
            'LICENSE_PLATE': 'license_plate',
            'COLOR': 'color',
            'TYPE': 'type',
            'NOTE': 'note'
        })
        df = df.replace('None', None)
        data = df.to_dict('records')

        return data

    def get_all_config(self,page_data,total):
        sql_command = '''
            SELECT ID, DEPARTMENT_ID, PLATE_PROVINCE, CREATED_DATE, LICENSE_PLATE, COLOR, TYPE, NOTE FROM BMA_PHASE_II.BLACKLISTS
            ORDER BY ID OFFSET {} ROWS FETCH NEXT {} ROWS ONLY
        '''.format(page_data['offset'], page_data['page_size'])

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()
    
        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'ID': 'id',
            'DEPARTMENT_ID': 'department_id',
            'LICENSE_PLATE': 'license_plate',
            'PLATE_PROVINCE': 'province',
            'COLOR': 'color',
            'TYPE': 'type',
            'NOTE': 'note',
            'CREATED_DATE': 'date'
        })
        df = df.replace('None', None)
        data = df.to_dict('records')

        page_total = math.ceil(total / page_data['page_size'])
        paginate_data = {
            'page': page_data['page'],
            'page_size': page_data['page_size'],
            'page_total': page_total
        }

        return data,paginate_data

    def get_all_by_department(self, department_id):
        sql_command = '''
            SELECT ID, DEPARTMENT_ID, PLATE_PROVINCE, CREATED_DATE,LICENSE_PLATE, COLOR, TYPE, NOTE FROM BMA_PHASE_II.BLACKLISTS
            WHERE DEPARTMENT_ID = {}
            ORDER BY ID
        '''.format(department_id)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'ID': 'id',
            'DEPARTMENT_ID': 'department_id',
            'LICENSE_PLATE': 'license_plate',
            'PLATE_PROVINCE': 'province',
            'COLOR': 'color',
            'TYPE': 'type',
            'NOTE': 'note',
            'CREATED_DATE': 'date'
        })
        df = df.replace('None', None)
        data = df.to_dict('records')

        return data

    def get_all_by_department_config(self, department_id,page_data,total):
        sql_command = '''
            SELECT ID, DEPARTMENT_ID, LICENSE_PLATE, COLOR, TYPE, NOTE FROM BMA_PHASE_II.BLACKLISTS
            WHERE DEPARTMENT_ID = {}
            ORDER BY ID OFFSET {} ROWS FETCH NEXT {} ROWS ONLY
        '''.format(department_id,page_data['offset'], page_data['page_size'])

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'ID': 'id',
            'DEPARTMENT_ID': 'department_id',
            'LICENSE_PLATE': 'license_plate',
            'COLOR': 'color',
            'TYPE': 'type',
            'NOTE': 'note'
        })
        df = df.replace('None', None)
        data = df.to_dict('records')

        page_total = math.ceil(total / page_data['page_size'])
        paginate_data = {
            'page': page_data['page'],
            'page_size': page_data['page_size'],
            'page_total': page_total
        }

        return data,paginate_data


    def insert(self, payloads, department_id):
        cursor = self.oracle_connection.cursor()
        new_id = cursor.var(cx_Oracle.NUMBER)

        sql_command = """
            INSERT INTO BMA_PHASE_II.BLACKLISTS (DEPARTMENT_ID, LICENSE_PLATE, PLATE_PROVINCE, COLOR, "TYPE", NOTE, CREATED_DATE)
            VALUES ({}, '{}', '{}', '{}', '{}', '{}', TO_DATE('{}', 'YYYY-MM-DD'))
            returning ID into :python_var
        """.format(
            department_id, payloads['license_plate'], payloads['province'],
            payloads['color'], payloads['type'], payloads['note'], payloads['date']
        )

        cursor.execute(sql_command, [new_id])
        blacklist_id = new_id.getvalue()
        blacklist_id = int(blacklist_id[0])
        self.oracle_connection.commit()

        get_sql_command = '''
            SELECT LICENSE_PLATE, PLATE_PROVINCE, COLOR, "TYPE", NOTE FROM BMA_PHASE_II.BLACKLISTS
            WHERE ID = {}
        '''.format(blacklist_id)

        cursor.execute(get_sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'LICENSE_PLATE': 'licence_plate',
            'PLATE_PROVINCE': 'plate_province',
            'COLOR': 'color',
            'TYPE': 'type',
            'NOTE': 'note',
        })

        df = df.replace('None', None)
        result = df.to_dict('records')
        blacklist = result[0]

        return blacklist


    def update(self, id, payloads):
        sql_command = '''
            UPDATE BMA_PHASE_II.BLACKLISTS 
            SET LICENSE_PLATE = '{}',
                PLATE_PROVINCE = '{}',
                COLOR = '{}',
                "TYPE" = '{}',
                NOTE = '{}'
            WHERE ID = {}
        '''.format(
            payloads['license_plate'], payloads['province'],
            payloads['color'], payloads['type'], payloads['note'],
            id
        )

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        self.oracle_connection.commit()

        get_sql_command = '''
            SELECT LICENSE_PLATE, PLATE_PROVINCE, COLOR, "TYPE", NOTE FROM BMA_PHASE_II.BLACKLISTS
            WHERE ID = {}
        '''.format(id)

        cursor.execute(get_sql_command)
        data = cursor.fetchall()

        columes = [row[0] for row in cursor.description]
        df = pd.DataFrame(data=data, columns=columes)
        df = df.rename(columns={
            'LICENSE_PLATE': 'licence_plate',
            'PLATE_PROVINCE': 'plate_province',
            'COLOR': 'color',
            'TYPE': 'type',
            'NOTE': 'note',
        })

        df = df.replace('None', None)
        result = df.to_dict('records')
        blacklist = result[0]

        return blacklist


    def delete(self, id):
        sql_command = '''
            DELETE
            FROM BMA_PHASE_II.BLACKLISTS
            WHERE ID = {}
        '''.format(id)

        cursor = self.oracle_connection.cursor()
        cursor.execute(sql_command)
        self.oracle_connection.commit()