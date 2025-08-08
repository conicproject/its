from rest_framework.exceptions import ParseError

import datetime
from dateutil.relativedelta import relativedelta

class TrafficDetailValidator:

    def __init__(self):
        self.date_format = "%Y-%m-%d"
        self.month_format = "%Y-%m"
        self.year_format = "%Y"
        self.type = ['day', 'week', 'month', 'year', 'range']
        self.max_days_range = 14
        self.min_days_range = 1

        self.missing_date_field = 'date field required'
        self.missing_type_field = 'type field required'
        self.missing_checkpoint_field = 'checkpoint field required'

        self.incorrect_time_format = 'incorrect format'
        self.incorrect_time_value = 'incorrect value'
        self.incorrect_type_value = 'incorrect value'
        self.start_date_not_monday = 'start date should be monday'

        self.start_date_gte_end_date = "start date can't greater than or equal end date"
        self.out_of_max_range = 'date range allow only 7 days'


    def __validate_date_format(self, date):
        try:
            datetime_ = datetime.datetime.strptime(date, self.date_format)
            date_ = datetime_.date()
        except:
            response = {
                'status_code': 400,
                'message': self.incorrect_time_format
            }

            raise ParseError(response)

        return date_


    def __validate_date_value(self, date):
        today = datetime.datetime.now().date()
        
        if date >= today:
            response = {
                'status_code': 400,
                'message': self.incorrect_time_value
            }

            raise ParseError(response)


    def __validate_week_format(self, start_date):
        try:
            start_datetime = datetime.datetime.strptime(
                start_date, self.date_format
            )
        except:
            response = {
                'status_code': 400,
                'message': self.incorrect_time_format
            }

            raise ParseError(response)

        return start_datetime


    def __validate_is_monday(self, datetime_):
        day_index = datetime_.weekday()

        if day_index != 0:
            response = {
                'status_code': 400,
                'message': self.start_date_not_monday
            }

            raise ParseError(response)


    def __validate_week_value(self, datetime_):
        end_datetime = datetime_ + datetime.timedelta(days=7)
        now = datetime.datetime.now()

        if (end_datetime >= now):
            response = {
                'status_code': 400,
                'message': self.incorrect_time_value
            }

            raise ParseError(response)
        
        return end_datetime


    def __validate_month_format(self, month_value):
        try:
            datetime_ = datetime.datetime.strptime(
                month_value, self.month_format
            )
            month = datetime_.month
            year = datetime_.year
        except:
            response = {
                'status_code': 400,
                'message': self.incorrect_time_format
            }

            raise ParseError(response)
        
        return datetime_, month, year


    def __validate_month_value(self, month, year):
        now = datetime.datetime.now()
        now_month = now.month
        now_year = now.year

        if (month >= now_month) and (year > now_year):
            response = {
                'status_code': 400,
                'message': self.incorrect_time_value
            }

            raise ParseError(response)


    def __validate_year_format(self, year_value):
        try:
            year_value = int(year_value)
        except:
            response = {
                'status_code': 400,
                'message': self.incorrect_time_format
            }

            raise ParseError(response)
        
        return year_value


    def __validate_year_value(self, year_value):
        now = datetime.datetime.now()
        now_year = now.year

        if year_value > now_year:
            response = {
                'status_code': 400,
                'message': self.incorrect_time_value
            }

            raise ParseError(response)


    def __validate_len_range(self, list_raw_payloads):
        if len(list_raw_payloads) != 2:
            response = {
                'status_code': 400,
                'message': self.incorrect_time_value
            }

            raise ParseError(response)


    def __validate_range_format(self, range_value):
        try:
            list_raw_payloads = range_value.split(',')
            self.__validate_len_range(
                list_raw_payloads=list_raw_payloads
            )

            start_date = datetime.datetime.strptime(
                list_raw_payloads[0], self.date_format
            ).date()
            end_date = datetime.datetime.strptime(
                list_raw_payloads[1], self.date_format
            ).date()

        except:
            response = {
                'status_code': 400,
                'message': self.incorrect_time_format
            }

            raise ParseError(response)
        
        return start_date, end_date


    def __validate_range_limitation(self, start_date, end_date):
        range_ = end_date - start_date
        days_range = range_.days


        if not (self.min_days_range <= days_range <= self.max_days_range):
            response = {
                'status_code': 400,
                'message': self.out_of_max_range
            }

            raise ParseError(response)


    def __validate_startdate_enddate(self, start_date, end_date):
        if start_date >= end_date:
            response = {
                'status_code': 400,
                'message': self.start_date_gte_end_date
            }

            raise ParseError(response)


    def __validate_enddate_value(self, end_date):
        today = datetime.datetime.now().date()

        if end_date >= today:
            response = {
                'status_code': 400,
                'message': self.incorrect_time_value
            }

            raise ParseError(response)


    def __validate_date_field(self, params):
        if 'date' not in params:
            response = {
                'status_code': 400,
                'message': self.missing_date_field
            }

            raise ParseError(response)

        date = params.get('date')

        return date


    def __validate_type_field(self, params):
        if 'type' not in params:
            response = {
                'status_code': 400,
                'message': self.missing_type_field
            }

            raise ParseError(response)
        
        type = params.get('type')

        return type


    def __validate_type_value(self, type):
        if type not in self.type:
            response = {
                'status_code': 400,
                'message': self.incorrect_type_value
            }

            raise ParseError(response)


    def __validate_checkpoint_field(self, params):
        if 'checkpoint' not in params:
            response = {
                'status_code': 400,
                'message': self.missing_checkpoint_field
            }

            raise ParseError(response)
        
        checkpoint = params.get('checkpoint')

        return checkpoint


    def __validate_checkpoint_id(self, checkpoint_id):
        try:
            checkpoint_id = int(checkpoint_id)
        except:
            response = {
                'status_code': 400,
                'message': self.incorrect_time_format
            }

            raise ParseError(response)

        return checkpoint_id


    def validate_type_day(self, datetime_value):
        date = self.__validate_date_format(date=datetime_value)
        self.__validate_date_value(date=date)

        return date


    def validate_type_week(self, datetime_value):
        start_datetime = self.__validate_week_format(start_date=datetime_value)
        self.__validate_is_monday(datetime_=start_datetime)
        end_datetime = self.__validate_week_value(datetime_=start_datetime)

        start_date = start_datetime.date()
        end_date = end_datetime.date()

        return start_date, end_date


    def validate_type_month(self, datetime_value):
        datetime_, month, year = self.__validate_month_format(month_value=datetime_value)
        self.__validate_month_value(month=month, year=year)

        start_date = datetime_.date()
        end_date = start_date + relativedelta(months=1)

        return start_date, end_date


    def validate_type_year(self, datetime_value):
        year_value = self.__validate_year_format(year_value=datetime_value)
        self.__validate_year_value(year_value=year_value)

        return year_value


    def validate_type_range(self, datetime_value):
        start_date, end_date = self.__validate_range_format(
            range_value=datetime_value
        )
        self.__validate_startdate_enddate(
            start_date=start_date, end_date=end_date
        )
        self.__validate_enddate_value(end_date=end_date)
        self.__validate_range_limitation(
            start_date=start_date, end_date=end_date
        )
        end_date = end_date + datetime.timedelta(days=1)

        return start_date, end_date


    def validate_report_request(self, params):
        type = self.__validate_type_field(params=params)
        datetime_value = self.__validate_date_field(params=params)

        self.__validate_type_value(type=type)

        return type, datetime_value


    def validate_request(self, params):
        type = self.__validate_type_field(params=params)
        datetime_value = self.__validate_date_field(params=params)
        checkpoint = self.__validate_checkpoint_field(params=params)

        self.__validate_type_value(type=type)
        checkpoint_id = self.__validate_checkpoint_id(checkpoint_id=checkpoint)

        return type, datetime_value, checkpoint_id