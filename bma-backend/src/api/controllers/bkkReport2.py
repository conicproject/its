from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed

from api.validators.session import SessionValidator
from api.validators.trafficDetail import TrafficDetailValidator

from api.repositories.user import UserRepository
from api.repositories.oracleCheckpoint import OracleCheckpointRepository

from api.logics.bkkReport import BkkReportLogic
import pandas as pd

import json
from dateutil.relativedelta import relativedelta
# import datetime

from datetime import datetime, timedelta

class BkkReport2ViewSet(viewsets.ViewSet):

    def __init__(self):
        self.user_repo = UserRepository()
        self.checkpoint_repo = OracleCheckpointRepository()

        self.session_validator = SessionValidator()
        self.traffic_detail_validator = TrafficDetailValidator()
        self.bkk_report_logic = BkkReportLogic()

    def daily(self, request):

        now = datetime.now()
        yesterday = now - timedelta(days=1)
        now_date = yesterday.strftime('%Y-%m-%d')

        type = 'day'
        datetime_value = now_date
        report_data = []

        checkpoints = self.checkpoint_repo.get_all_active_report()

        for checkpoint in checkpoints:
            response = self.bkk_report_logic.get_data(
                type=type, datetime_value=datetime_value, checkpoint_id=checkpoint['id']
            )
            response['checkpoint'] = checkpoint
           
            report_data.append(response)


        response_ = {
            'status_code': 200,
            'message': 'request success',
            'data': report_data
        }

        with open('../json-folder/daily_json.json', 'w', encoding='utf-8') as outfile:
            outfile.write(json.dumps(response_, default=str, ensure_ascii=False, indent=2))

        response = {
            'status_code': 200,
            'message': 'request success'
        }

        return Response(response, status=status.HTTP_200_OK)

    def weekly(self, request):

        now = datetime.now()

        if(now.strftime('%A') != 'Monday'):
            response = {
                'status_code': 200,
                'message': 'date is valid',
                'data': now.strftime('%A')
            }

            return Response(response, status=status.HTTP_200_OK)

        previous_monday = now - timedelta(days=7)
        date = previous_monday.strftime('%Y-%m-%d')
        # date = '2023-02-06'

        type = 'week'
        datetime_value = date
        report_data = []

        checkpoints = self.checkpoint_repo.get_all_active_report()

        for checkpoint in checkpoints:
            response = self.bkk_report_logic.get_data(
                type=type, datetime_value=datetime_value, checkpoint_id=checkpoint['id']
            )
            response['checkpoint'] = checkpoint
           
            report_data.append(response)

        # response_ = {
        #     'status_code': 200,
        #     'message': 'request success',
        #     'data': report_data
        # }

        # with open('../json-folder/weekly_json.json', 'w', encoding='utf-8') as outfile:
        #     outfile.write(json.dumps(response_, default=str, ensure_ascii=False, indent=2))

        response = {
            'status_code': 200,
            'message': 'request success'
        }

        return Response(response, status=status.HTTP_200_OK)

    def monthly(self, request):
        now = datetime.now()
        fistDayOfMonth = now.replace(day=1)

        if(now.date() != fistDayOfMonth.date()):
        # if(now.date() == fistDayOfMonth.date()):
            response = {
                'status_code': 200,
                'message': 'not first day of monthly'
            }

            return Response(response, status=status.HTTP_200_OK)

        previous_month_first_day = fistDayOfMonth - relativedelta(months=+1)

        type = 'month'
        datetime_value = previous_month_first_day.strftime('%Y-%m')
        report_data = []

        checkpoints = self.checkpoint_repo.get_all_active_report()

        for checkpoint in checkpoints:
            response = self.bkk_report_logic.get_data(
                type=type, datetime_value=datetime_value, checkpoint_id=checkpoint['id']
            )
            response['checkpoint'] = checkpoint
           
            report_data.append(response)

        # response_ = {
        #     'status_code': 200,
        #     'message': 'request success',
        #     'data': report_data
        # }

        # with open('../json-folder/monthly_json.json', 'w', encoding='utf-8') as outfile:
        #     outfile.write(json.dumps(response_, default=str, ensure_ascii=False, indent=2))

        response = {
            'status_code': 200,
            'message': 'request success',
            'data': report_data
        }

        return Response(response, status=status.HTTP_200_OK)

    def yearly(self, request):
        now = datetime.now()
        current_year = now.strftime('%Y')

        previous_year = now - relativedelta(years=+1)

        type = 'year'
        datetime_value = previous_year.strftime('%Y')
        report_data = []

        checkpoints = self.checkpoint_repo.get_all_active_report()
        for checkpoint in checkpoints:
            response = self.bkk_report_logic.get_data(
                type=type, datetime_value=datetime_value, checkpoint_id=checkpoint['id']
            )
            response['checkpoint'] = checkpoint
           
            report_data.append(response)

        response_ = {
            'status_code': 200,
            'message': 'request success',
            'data': report_data
        }

        with open('../json-folder/yearly_json.json', 'w', encoding='utf-8') as outfile:
            outfile.write(json.dumps(response_, default=str, ensure_ascii=False, indent=2))

        response = {
            'status_code': 200,
            'message': 'request success'
        }

        return Response(response, status=status.HTTP_200_OK)


