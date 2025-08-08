from rest_framework import viewsets
from rest_framework.response import Response

from api.logics.timePayloads import TimePayloadsLogic
from api.repositories.record import RecordRepository
from api.logics.dashboard import DashboardLogic

from api.validators.trafficDetail import TrafficDetailValidator

from api.logics.trafficDetail import TrafficDetailLogic
from api.validators.vehicle import VehicleValidator
from api.repositories.record import RecordRepository
from api.repositories.oracleVehicleType import OracleVehicleTypeRepository
from api.repositories.timeRange import TimeRangeRepository

from api.logics.trafficDetail import TrafficDetailLogic
from api.repositories.record import RecordRepository
from api.logics.bkkReport import BkkReportLogic

import json


from rest_framework.exceptions import ParseError


import datetime
import pandas as pd

class TestViewSet(viewsets.ViewSet):

    def __init__(self):

        self.record_repository = RecordRepository()
        self.hour_range = 12

        self.traffic_detail_validator = TrafficDetailValidator()
        self.traffic_detail_logic = TrafficDetailLogic()

        self.vehicle_type_repo = OracleVehicleTypeRepository()
        self.bkk_report_logic = BkkReportLogic()