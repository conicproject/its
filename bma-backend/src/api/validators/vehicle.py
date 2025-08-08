from rest_framework.exceptions import ParseError
import math
import json
import datetime

class VehicleValidator:

    def __init__(self):
        self.date_format = '%Y-%m-%d'
        self.format = '%Y-%m-%d %H:%M:%S'
        self.range_day = 7
        self.max_record = 10000

        self.incorrect_time_format = 'incorrect format'
        self.incorrect_time_value = 'incorrect value'


    def validate_date_field(self, params):
        if 'date' not in params:
            response = {
                'status_code': 400,
                'message': 'date field required'
            }

            raise ParseError(response)

        date = params.get('date')

        return date
    
    def validate_start_date_field(self, params):
        if 'startdate' not in params:
            response = {
                'status_code': 400,
                'message': 'date field required'
            }

            raise ParseError(response)

        date = params.get('startdate')

        return date

    def validate_end_date_field(self, params):
        if 'enddate' not in params:
            response = {
                'status_code': 400,
                'message': 'date field required'
            }

            raise ParseError(response)

        date = params.get('enddate')

        return date

    def validate_date_format(self, date_value):
        try:
            datetime_ = datetime.datetime.strptime(date_value, self.date_format)
            date_ = datetime_.date()

        except:
            response = {
                'status_code': 400,
                'message': self.incorrect_time_format
            }

            raise ParseError(response)
        
        return date_


    def validate_date_value(self, date_value):
        today = datetime.datetime.now().date()

        if date_value > today:
            response = {
                'status_code': 400,
                'message': self.incorrect_time_value
            }

            raise ParseError(response)

        end_date = date_value + datetime.timedelta(days=1)
        start_date = end_date - datetime.timedelta(days=self.range_day)

        start_date_str = start_date.strftime(self.date_format)
        end_date_str = end_date.strftime(self.date_format)

        return start_date_str, end_date_str


    def validate_date_value_blacklist(self, date_value):
        today = datetime.datetime.now().date()

        if date_value > today:
            response = {
                'status_code': 400,
                'message': self.incorrect_time_value
            }

            raise ParseError(response)

        end_date = date_value + datetime.timedelta(days=1)
        start_date = end_date - datetime.timedelta(days=30)

        start_date_str = start_date.strftime(self.format)
        end_date_str = end_date.strftime(self.format)

        return start_date_str, end_date_str


    def validate_date_value_truck(self, date_value):
        today = datetime.datetime.now().date()

        if date_value > today:
            response = {
                'status_code': 400,
                'message': self.incorrect_time_value
            }

            raise ParseError(response)

        end_date = date_value + datetime.timedelta(days=1)
        start_date = date_value

        start_date_str = start_date.strftime(self.format)
        end_date_str = end_date.strftime(self.format)

        return start_date_str, end_date_str
    
    def validate_date_value_destination(self, date_value):
        today = datetime.datetime.now().date()

        if date_value > today:
            response = {
                'status_code': 400,
                'message': self.incorrect_time_value
            }

            raise ParseError(response)

        end_date = date_value + datetime.timedelta(days=1)
        start_date = date_value

        start_date_str = start_date.strftime(self.date_format)
        end_date_str = end_date.strftime(self.date_format)

        return start_date_str, end_date_str



    def validate_date(self, params):
        # date = self.validate_date_field(params=params)
        # date = self.validate_date_format(date_value=date)
        # start_date, end_date = self.validate_date_value(date_value=date)
        start = self.validate_start_date_field(params=params)
        end = self.validate_end_date_field(params=params)
        start_date = self.validate_date_format(date_value=start)
        end_date = self.validate_date_format(date_value=end)
        end_date = end_date + datetime.timedelta(days=1)
        start_date = start_date.strftime(self.date_format)
        end_date = end_date.strftime(self.date_format)

        return start_date, end_date


    def validate_date_blacklist(self, params):
        # date = self.validate_date_field(params=params)
        # date = self.validate_date_format(date_value=date)
        # start_date, end_date = self.validate_date_value_blacklist(date_value=date)
        start = self.validate_start_date_field(params=params)
        end = self.validate_end_date_field(params=params)
        start_date = self.validate_date_format(date_value=start)
        end_date = self.validate_date_format(date_value=end)
        end_date = end_date + datetime.timedelta(days=1)
        start_date = start_date.strftime(self.date_format)
        end_date = end_date.strftime(self.date_format)

        return start_date, end_date


    def validate_date_truck(self, params):
        # date = self.validate_date_field(params=params)
        # date = self.validate_date_format(date_value=date)
        # start_date, end_date = self.validate_date_value_truck(date_value=date)
        start = self.validate_start_date_field(params=params)
        end = self.validate_end_date_field(params=params)
        start_date = self.validate_date_format(date_value=start)
        end_date = self.validate_date_format(date_value=end)
        end_date = end_date + datetime.timedelta(days=1)
        start_date = start_date.strftime(self.format)
        end_date = end_date.strftime(self.format)


        return start_date, end_date

    def validate_date_destination(self, params):
        date = self.validate_date_field(params=params)
        date = self.validate_date_format(date_value=date)
        start_date, end_date = self.validate_date_value_destination(date_value=date)

        return start_date, end_date
    

    def validate_plate_no_field(self, params):
        if 'plate_no' not in params:
            plate_no = ''
        else:
            plate_no = params.get('plate_no')
        
        return plate_no

    
    def validate_plate_no_field_destination(self, params):
        if 'plate_no' not in params:
            response = {
                'status_code': 400,
                'message': 'plate no required'
            }
            raise ParseError(response)
        else:
            plate_no = params.get('plate_no')
        
        return plate_no
    
    def validate_province_field_destination(self, params):
        if 'province' not in params:
            response = {
                'status_code': 400,
                'message': 'province required'
            }
            raise ParseError(response)
        else:
            province = params.get('province')
        
        return province

    def validate_vehicle_type_field_destination(self, params):
        if 'vehicle_type' not in params:
            response = {
                'status_code': 400,
                'message': 'vehicle type required'
            }
            raise ParseError(response)
        else:
            vehicle_type = params.get('vehicle_type')
        
        return vehicle_type


    def validate_vehicle_color_field_destination(self, params):
        if 'vehicle_color' not in params:
            response = {
                'status_code': 400,
                'message': 'vehicle color required'
            }
            raise ParseError(response)
        else:
            vehicle_color = params.get('vehicle_color')
        
        return vehicle_color

    def validate_province_field(self, params):
        if 'province' not in params:
            province = ''
        else:
            province = params.get('province')
        
        return province


    def validate_checkpoint_field(self, params):
        if 'checkpoint' not in params:
            checkpoint = ''
        else:
            checkpoint = params.get('checkpoint')
        
        return checkpoint


    def validate_direction_field(self, params):
        if 'direction' not in params:
            direction = ''
        else:
            direction = params.get('direction')
        
        return direction

    def validate_timerange_field(self, params):
        if 'timerange' not in params:
            response = {
                'status_code': 400,
                'message': 'timerange field required'
            }
            raise ParseError(response)
        timerange = params.get('timerange')
        timerange = json.loads(timerange)
        
        return timerange


    def validate_vehicle_type_field(self, params):
        if 'vehicle_type' not in params:
            vehicle_type = ''
        else:
            vehicle_type = params.get('vehicle_type')
        
        return vehicle_type


    def validate_vehicle_color_field(self, params):
        if 'vehicle_color' not in params:
            vehicle_color = ''
        else:
            vehicle_color = params.get('vehicle_color')
        
        return vehicle_color


    def validate_page_field(self, params):
        if 'page' not in params:
            response = {
                'status_code': 400,
                'message': 'page field required'
            }

            raise ParseError(response)

        page = params.get('page')

        return page


    def validate_page_value(self, page):
        try:
            page_value = int(page)
        except:
            response = {
                'status_code': 400,
                'message': self.incorrect_time_value
            }

            raise ParseError(response)

        return page_value


    def validate_max_page(self, page, max_page):
        if page > max_page:
            response = {
                'status_code': 400,
                'message': 'over limitation'
            }

            raise ParseError(response)


    def validate_request(self, params):
        start_date, end_date = self.validate_date(params=params)
        plate_no = self.validate_plate_no_field(params=params)
        province = self.validate_province_field(params=params)
        checkpoint = self.validate_checkpoint_field(params=params)
        direction = self.validate_direction_field(params=params)
        vehicle_type = self.validate_vehicle_type_field(params=params)
        vehicle_color = self.validate_vehicle_color_field(params=params)

        payloads = {
            'start_date': start_date,
            'end_date': end_date,
            'plate_no': plate_no,
            'province': province,
            'checkpoint': checkpoint,
            'direction': direction,
            'vehicle_type': vehicle_type,
            'vehicle_color': vehicle_color,
            'type': params.get('type'),
        }

        return payloads


    def validate_request_blacklist(self, params):
        start_date, end_date = self.validate_date_blacklist(params=params)
        plate_no = self.validate_plate_no_field(params=params)
        province = self.validate_province_field(params=params)
        checkpoint = self.validate_checkpoint_field(params=params)
        direction = self.validate_direction_field(params=params)
        vehicle_type = self.validate_vehicle_type_field(params=params)
        vehicle_color = self.validate_vehicle_color_field(params=params)

        payloads = {
            'start_date': start_date,
            'end_date': end_date,
            'plate_no': plate_no,
            'province': province,
            'checkpoint': checkpoint,
            'direction': direction,
            'vehicle_type': vehicle_type,
            'vehicle_color': vehicle_color
        }

        return payloads
        

    def validate_request_truck(self, params):
        start_date, end_date = self.validate_date_truck(params=params)
        checkpoint = self.validate_checkpoint_field(params=params)
        direction = self.validate_direction_field(params=params)
        timerange = self.validate_timerange_field(params=params)
        payloads = {
            'start_date': start_date,
            'end_date': end_date,
            'checkpoint': checkpoint,
            'direction': direction,
            'starttime': timerange[0],
            'endtime': timerange[1]
        }

        return payloads
    
    def validate_request_destination(self, params):
        start_date, end_date = self.validate_date_destination(params=params)
        province = self.validate_province_field(params=params)
        vehicle_type = self.validate_vehicle_type_field(params=params)
        vehicle_color = self.validate_vehicle_color_field(params=params)
        payloads = {
            'start_date': start_date,
            'end_date': end_date,
            'province': province,
            'vehicle_type': vehicle_type,
            'vehicle_color': vehicle_color
        }

        return payloads

    
    def validate_request_destination_vehicle(self, params):
        start_date, end_date = self.validate_date_destination(params=params)
        province = self.validate_province_field_destination(params=params)
        plate_no = self.validate_plate_no_field_destination(params=params)
        vehicle_type = self.validate_vehicle_type_field_destination(params=params)
        vehicle_color = self.validate_vehicle_color_field_destination(params=params)
        payloads = {
            'start_date': start_date,
            'end_date': end_date,
            'plate_no': plate_no,
            'province': province,
            'vehicle_type': vehicle_type,
            'vehicle_color': vehicle_color
        }

        return payloads


    def validate_paginate(self, params):
        page_size = 20

        page = self.validate_page_field(params=params)
        page = self.validate_page_value(page=page)
        max_page = math.ceil(self.max_record/page_size)
        self.validate_max_page(page=page, max_page=max_page)

        offset = (page - 1) * page_size

        page_data = {
            'page': page,
            'page_size': page_size,
            'offset': offset
        }

        return page_data

    def validate_paginate_over_10k(self, params):
        page_size = 20

        page = self.validate_page_field(params=params)
        page = self.validate_page_value(page=page)
        # max_page = math.ceil(self.max_record/page_size)
        # self.validate_max_page(page=page, max_page=max_page)

        offset = (page - 1) * page_size

        page_data = {
            'page': page,
            'page_size': page_size,
            'offset': offset
        }

        return page_data