import math
import datetime

from api.repositories.timeRange import TimeRangeRepository

class TimeRangeLogic:

    def __init__(self):
        self.process_minutes = 5
        self.time_range_repo = TimeRangeRepository()


    def get_time_range_id(self, datetime_):
        rd_minute = self.round_down_minutes(minute=datetime_.minute)
        tmp_datetime = datetime.datetime(
            year=datetime_.year,
            month=datetime_.month,
            day=datetime_.day,
            hour=datetime_.hour,
            minute=rd_minute
        )

        end_time = tmp_datetime.strftime('%H:%M')
        time_range = self.time_range_repo.get_by_endtime(end_time=end_time)
        time_range_id = time_range['id']

        return time_range_id


    def round_down_minutes(self, minute: int):
        float_ = minute / self.process_minutes
        round_down = math.trunc(float_) * self.process_minutes

        return round_down