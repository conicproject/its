from api.logics.timeRange import TimeRangeLogic
from api.repositories.timeRange import TimeRangeRepository
import datetime

class TimePayloadsLogic:

    def __init__(self):
        self.time_range_logic = TimeRangeLogic()
        self.time_range_repo = TimeRangeRepository()


    def get_query_time_payloads(self, time_config: dict):
        now = datetime.datetime.now()
        past = now - datetime.timedelta(
            days=time_config['days'],
            hours=time_config['hours']
        )
        time_payloads = self.list_payloads(now=now, past=past)

        return time_payloads


    def onday_time_range(self, now, past, end_date):
        date = end_date
        start_time_id = self.time_range_logic.get_time_range_id(past)
        end_time_id = self.time_range_logic.get_time_range_id(now)

        payloads = [
            {
                'date': date,
                'start_time_id': start_time_id,
                'end_time_id': end_time_id
            }
        ]

        return payloads


    def between_time_range(self, now, past, start_date, end_date):

        past_stime_id = self.time_range_logic.get_time_range_id(past)
        past_etime_id = 288

        onday_stime_id = 0
        onday_etime_id = self.time_range_logic.get_time_range_id(now)

        payloads = [
            {
                'date': start_date,
                'start_time_id': past_stime_id,
                'end_time_id': past_etime_id
            },
            {
                'date': end_date,
                'start_time_id': onday_stime_id,
                'end_time_id': onday_etime_id
            }
        ]

        return payloads


    def list_payloads(self, now, past):
        start_date = past.date()
        end_date = now.date()

        if start_date == end_date:
            payloads = self.onday_time_range(
                now=now, past=past, end_date=end_date
            )
        else:
            payloads = self.between_time_range(
                now=now, past=past, start_date=start_date, end_date=end_date
            )
        
        return payloads


