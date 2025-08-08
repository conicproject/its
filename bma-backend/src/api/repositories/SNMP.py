import requests
import xmltodict

class SNMPRepository:

    def __init__(self):
        self.url = 'http://10.151.32.116:8080/api/getsensordetails.json'
        self.params = {
            'show': 'text',
            'username': 'prtgadmin',
            'passhash': '2109973814'
            # 'password':'Abc@1234#'
        }
        self.url_all = 'http://10.151.32.116:8080/api/table.xml'
        self.params_all = {
            'content': 'sensors',
            'username': 'prtgadmin',
            'passhash': '2109973814',
            'columns': 'objid,status',
        }


    def get_all_status(self, list_id):
        status_data = []

        for id in list_id:
            self.params['id'] = id
            response = requests.get(self.url, params=self.params)
            response = response.json()
            status = response['sensordata']['statustext']
            status_data.append(status)
        
        return status_data


    def get_all_sensor_report(self, list_id):
        status_data = []
        name_data = []

        for id in list_id:
            self.params['id'] = id
            response = requests.get(self.url, params=self.params)
            response = response.json()
            status = response['sensordata']['statustext']
            name = response['sensordata']['parentdevicename']

            status_data.append(status)
            name_data.append(name)
        
        return status_data, name_data

    def get_all_sensor_status(self):
        response = requests.get(self.url_all, params=self.params_all)
        xpars = xmltodict.parse(response.text)
        item = xpars['sensors']['item']
        return item