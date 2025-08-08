import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
import pandas as pd
from dateutil.relativedelta import relativedelta

from api.validators.trafficDetail import TrafficDetailValidator
from api.repositories.timeRange import TimeRangeRepository
from api.repositories.record import RecordRepository
from api.repositories.violation import ViolationRepository
from api.repositories.oracleCheckpoint import OracleCheckpointRepository
from api.repositories.oracleVehicleType import OracleVehicleTypeRepository
import itertools

class BkkReportLogic:

    def __init__(self):
        self.date_format = "%Y-%m-%d"
        self.type = ['day', 'week', 'month', 'year', 'range']
        self.day_range = 288
        self.hour_range = 12
        self.last_time_range = 288

        self.rush_hour_config = [
            {
                'start': 1,
                'end': 84
            },
            {
                'start': 85,
                'end': 108
            },
            {
                'start': 109,
                'end': 144
            },
            {
                'start': 145,
                'end': 192
            },
            {
                'start': 193,
                'end': 228
            },
            {
                'start': 229,
                'end': 288               
            }
        ]

        self.record_repository = RecordRepository()
        self.violation_repository = ViolationRepository()
        self.time_range_repository = TimeRangeRepository()
        self.traffic_detail_validator = TrafficDetailValidator()

        self.vehicle_type_repo = OracleVehicleTypeRepository()


    def get_time_range_data(self):
        # time ranges: list[dict]
        time_ranges = self.time_range_repository.get_all()
        time_ranges_df = pd.DataFrame(time_ranges)
        time_range_ids = time_ranges_df['id'].values
        time_range_end_times = time_ranges_df['end_time'].values
        # return list[int], list[str]
        return time_range_ids, time_range_end_times
    

    def get_day_data(self, date, checkpoint_id,type):
        if(type == '0'):
            query_data = self.record_repository.get_by_date(
                date=date, checkpoint_id=checkpoint_id
            )
        elif(type == '1'):
            query_data = self.violation_repository.get_by_date(
                date=date, checkpoint_id=checkpoint_id
            )
        car_type_list_id = self.vehicle_type_repo.get_list_id()
        car_type_list_name = self.vehicle_type_repo.get_list_name()
        car_type_unique_name = self.vehicle_type_repo.get_list_active_name()
        
        df = pd.DataFrame(query_data)
        df = df.rename(
            columns={
                'time_range_id': 'time',
                'car_type_id': 'car_type'
            }
        )
        df['car_type'] = df['car_type'].replace(
            car_type_list_id, car_type_list_name
        )

        df = df[['direction', 'time', 'car_type', 'date', 'volume']].groupby(by=['direction', 'car_type', 'time', 'date']).sum()
        df = df.reset_index()

        df['pcu'] = 0
        name_pcu_list = self.vehicle_type_repo.get_list_active_name_pcu()
        df_pcu_config = pd.DataFrame(name_pcu_list)

        for item_data in name_pcu_list:
            df.loc[df['car_type'] == item_data['name'], 'pcu'] = item_data['pcu']

        time_range_ids, time_range_end_times = self.get_time_range_data()
        zero_value = len(df[df['volume'].isin([0])].index)

        if zero_value != len(df.index):

            df_car_type = df[['car_type', 'volume']].groupby(by='car_type').sum()
            df_car_type = df_car_type.reset_index()
            df_car_type['percent'] = 0
            if(df_car_type['volume'].sum() != 0):
                df_car_type['percent'] = (df_car_type['volume'] / df_car_type['volume'].sum()) * 100
            car_type_data = df_car_type[['car_type', 'volume']].to_dict('records')
            car_type_percent_data = df_car_type[['car_type', 'percent']].to_dict('records')

            # graph
            df_graph_ = df[['direction', 'time', 'date', 'volume']].groupby(by=['direction', 'time', 'date']).sum()
            df_graph_ = df_graph_.reset_index()

            df_volume = df_graph_[['volume']].groupby(df_graph_.index // self.hour_range).sum()
            df_graph = df_graph_[df_graph_.index % self.hour_range == (self.hour_range - 1)]

            df_graph['volume'] = df_volume['volume'].to_list()
            df_graph[['time']] = df_graph[['time']].replace(
                time_range_ids, time_range_end_times
            )


            df_graph[['time']] = df_graph[['time']].replace('00:00', '24:00')

            df_graph_inbound = df_graph[df_graph['direction'] == 'IN'][['time', 'date', 'volume']]
            graph_inbound_data = df_graph_inbound.to_dict('records')

            df_graph_outbound = df_graph[df_graph['direction'] == 'OUT'][['time', 'date', 'volume']]
            graph_outbound_data = df_graph_outbound.to_dict('records')


            report_quarter_hour = {
                'inbound': [],
                'outbound': []
            }

            df_time_inbound = df[df['direction'] == 'IN']
            df_time_inbound = df_time_inbound[['time', 'date', 'volume']].groupby(by=['time', 'date']).sum()
            df_time_inbound = df_time_inbound.reset_index()

            for i in range(24):
                quarter_hour_data = {}

                hour_range = [index_value for index_value in range((i * 12) + 1, (i * 12) + 13)]
                df_hour = df_time_inbound[df_time_inbound['time'].isin(hour_range)]

                df_hour_volume = df_hour[['volume']].groupby(df_hour.index // 3).sum()
                df_quarter = df_hour[df_hour.index % 3 == 2]
                df_quarter['volume'] = df_hour_volume['volume'].to_list()
                df_quarter[['time']] = df_quarter[['time']].replace(
                    time_range_ids, time_range_end_times
                )

                total = df_hour['volume'].sum()
                quarter_hour_data['data'] = df_quarter.to_dict('records')
                quarter_hour_data['total'] = total

                report_quarter_hour['inbound'].append(quarter_hour_data)



            df_time_outbound = df[df['direction'] == 'OUT']
            df_time_outbound = df_time_outbound[['time', 'date', 'volume']].groupby(by=['time', 'date']).sum()
            df_time_outbound = df_time_outbound.reset_index()

            for i in range(24):
                quarter_hour_data = {}

                hour_range = [index_value for index_value in range((i * 12) + 1, (i * 12) + 13)]
                df_hour = df_time_outbound[df_time_outbound['time'].isin(hour_range)]

                df_hour_volume = df_hour[['volume']].groupby(df_hour.index // 3).sum()
                df_quarter = df_hour[df_hour.index % 3 == 2]
                df_quarter['volume'] = df_hour_volume['volume'].to_list()
                df_quarter[['time']] = df_quarter[['time']].replace(
                    time_range_ids, time_range_end_times
                )

                total = df_hour['volume'].sum()
                quarter_hour_data['data'] = df_quarter.to_dict('records')
                quarter_hour_data['total'] = total

                report_quarter_hour['outbound'].append(quarter_hour_data)





            report_data = {
                'inbound': {},
                'outbound': {}
            }


            for car_type in car_type_unique_name:
                report_car_type = df[(df['car_type'] == car_type) & (df['direction'] == 'IN')].sort_values(by=['time'])
                report_car_type = report_car_type.reset_index(drop=True)
                report_car_type = report_car_type[['time', 'date', 'volume']]

                volume_car_type = report_car_type[['volume']].groupby(report_car_type.index // self.hour_range).sum()
                report_car_type = report_car_type[report_car_type.index % self.hour_range == (self.hour_range - 1)]
                report_car_type['volume'] = volume_car_type['volume'].to_list()
                report_car_type[['time']] = report_car_type[['time']].replace(
                    time_range_ids, time_range_end_times
                )

                report_car_type[['time']] = report_car_type[['time']].replace('00:00', '24:00')
                report_data['inbound'][car_type] = {}

                report_data['inbound'][car_type]['data'] = report_car_type.to_dict('records')
                report_data['inbound'][car_type]['total'] = report_car_type['volume'].sum()

                pcu_report_car_type = df_pcu_config[df_pcu_config['name'] == car_type].iloc[0]['pcu']
                report_data['inbound'][car_type]['pcu'] = report_car_type['volume'].sum() * pcu_report_car_type


            ## pcu inbound
            df_pcu = df[df['direction'] == 'IN']
            df_pcu = df_pcu[['time', 'date', 'car_type', 'volume', 'pcu']].groupby(by=['car_type', 'time', 'date','pcu']).sum()
            df_pcu = df_pcu.reset_index()

            pcu_value = df_pcu.volume * df_pcu.pcu
            df_pcu['pcu_value'] = pcu_value

            df_pcu = df_pcu[['time', 'date', 'pcu_value']].groupby(by=['time', 'date']).sum()
            df_pcu = df_pcu.reset_index()
            df_pcu = df_pcu.rename(columns={
                'pcu_value': 'volume'
            })

            volume_pcu = df_pcu[['volume']].groupby(df_pcu.index // self.hour_range).sum()
            df_pcu = df_pcu[df_pcu.index % self.hour_range == (self.hour_range - 1)]
            df_pcu['volume'] = volume_pcu['volume'].to_list()
            df_pcu[['time']] = df_pcu[['time']].replace(
                time_range_ids, time_range_end_times
            )
            df_pcu[['time']] = df_pcu[['time']].replace('00:00', '24:00')

            pcu = df_pcu.to_dict('records')
            report_data['inbound']['pcu'] = {}
            report_data['inbound']['pcu']['data'] = pcu
            report_data['inbound']['pcu']['total'] = df_pcu['volume'].sum()


            ## total group by time inbound
            df_total = df[df['direction'] == 'IN']
            df_total = df_total[['time', 'date', 'volume',]].groupby(by=['time', 'date']).sum()
            df_total = df_total.reset_index()

            volume_total = df_total[['volume']].groupby(df_total.index // self.hour_range).sum()
            df_total = df_total[df_total.index % self.hour_range == (self.hour_range - 1)]
            df_total['volume'] = volume_total['volume'].to_list()
            df_total[['time']] = df_total[['time']].replace(
                time_range_ids, time_range_end_times
            )
            df_total[['time']] = df_total[['time']].replace('00:00', '24:00')

            total_by_time = df_total.to_dict('records')
            report_data['inbound']['total'] = {}
            report_data['inbound']['total']['data'] = total_by_time
            report_data['inbound']['total']['total'] = df_total['volume'].sum()


            for car_type in car_type_unique_name:
                report_car_type = df[(df['car_type'] == car_type) & (df['direction'] == 'OUT')].sort_values(by=['time'])
                report_car_type = report_car_type.reset_index(drop=True)
                report_car_type = report_car_type[['time', 'date', 'volume']]

                volume_car_type = report_car_type[['volume']].groupby(report_car_type.index // self.hour_range).sum()
                report_car_type = report_car_type[report_car_type.index % self.hour_range == (self.hour_range - 1)]
                report_car_type['volume'] = volume_car_type['volume'].to_list()
                report_car_type[['time']] = report_car_type[['time']].replace(
                    time_range_ids, time_range_end_times
                )

                report_car_type[['time']] = report_car_type[['time']].replace('00:00', '24:00')
                report_data['outbound'][car_type] = {}

                report_data['outbound'][car_type]['data'] = report_car_type.to_dict('records')
                report_data['outbound'][car_type]['total'] = report_car_type['volume'].sum()

                pcu_report_car_type = df_pcu_config[df_pcu_config['name'] == car_type].iloc[0]['pcu']
                report_data['outbound'][car_type]['pcu'] = report_car_type['volume'].sum() * pcu_report_car_type


            ## pcu outbound
            df_pcu = df[df['direction'] == 'OUT']
            df_pcu = df_pcu[['time', 'date', 'car_type', 'volume', 'pcu']].groupby(by=['car_type', 'time', 'date','pcu']).sum()
            df_pcu = df_pcu.reset_index()

            pcu_value = df_pcu.volume * df_pcu.pcu
            df_pcu['pcu_value'] = pcu_value

            df_pcu = df_pcu[['time', 'date', 'pcu_value']].groupby(by=['time', 'date']).sum()
            df_pcu = df_pcu.reset_index()
            df_pcu = df_pcu.rename(columns={
                'pcu_value': 'volume'
            })

            volume_pcu = df_pcu[['volume']].groupby(df_pcu.index // self.hour_range).sum()
            df_pcu = df_pcu[df_pcu.index % self.hour_range == (self.hour_range - 1)]
            df_pcu['volume'] = volume_pcu['volume'].to_list()
            df_pcu[['time']] = df_pcu[['time']].replace(
                time_range_ids, time_range_end_times
            )
            df_pcu[['time']] = df_pcu[['time']].replace('00:00', '24:00')

            pcu = df_pcu.to_dict('records')
            report_data['outbound']['pcu'] = {}
            report_data['outbound']['pcu']['data'] = pcu
            report_data['outbound']['pcu']['total'] = df_pcu['volume'].sum()


            ## total group by time outbound
            df_total = df[df['direction'] == 'OUT']
            df_total = df_total[['time', 'date', 'volume',]].groupby(by=['time', 'date']).sum()
            df_total = df_total.reset_index()

            volume_total = df_total[['volume']].groupby(df_total.index // self.hour_range).sum()
            df_total = df_total[df_total.index % self.hour_range == (self.hour_range - 1)]
            df_total['volume'] = volume_total['volume'].to_list()
            df_total[['time']] = df_total[['time']].replace(
                time_range_ids, time_range_end_times
            )
            df_total[['time']] = df_total[['time']].replace('00:00', '24:00')

            total_by_time = df_total.to_dict('records')
            report_data['outbound']['total'] = {}
            report_data['outbound']['total']['data'] = total_by_time
            report_data['outbound']['total']['total'] = df_total['volume'].sum()


            data = {
                'car_type': {
                    'volume': car_type_data,
                    'percent': car_type_percent_data
                },
                'graph': {
                    'inbound': graph_inbound_data,
                    'outbound': graph_outbound_data
                },
                'report': report_data,
                'report_quarter_hour': report_quarter_hour
            }

        else:
            time_range_hours_list = [
                '01:00', '02:00', '03:00', '04:00', '05:00', '06:00',
                '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00',
                '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
                '21:00', '22:00', '23:00', '24:00'
            ]
            car_type_data = {
                'volume': [],
                'percent': []
            }

            for car_type in car_type_unique_name:
                volume_data = {
                    'car_type': car_type,
                    'volume': 0
                }
                percent_data = {
                    'car_type': car_type,
                    'percent': 0
                }

                car_type_data['volume'].append(volume_data)
                car_type_data['percent'].append(percent_data)
            
            graph = {
                'inbound': [],
                'outbound': []
            }

            report_quarter_hour = {
                'inbound': [],
                'outbound': []
            }

            str_time = '00:00'
            format_ = '%H:%M'
            datetime_ = datetime.datetime.strptime(str_time, format_)

            for hour in range(24):
                datetime_hour = datetime_ + datetime.timedelta(hours=hour)
                quarter_hour_data = {}
                quarter_hour_data['data'] = []
                quarter_hour_data['total'] = 0

                for quarter in range(4):
                    datetime_quarter = datetime_hour + datetime.timedelta(minutes=(quarter + 1) * 15)
                    data = {
                        'time': datetime_quarter.strftime(format_),
                        'date': date,
                        'volume': 0
                    }

                    quarter_hour_data['data'].append(data)
                
                report_quarter_hour['inbound'].append(quarter_hour_data)
                report_quarter_hour['outbound'].append(quarter_hour_data)
            
            report = {
                'inbound': {},
                'outbound': {}
            }

            car_type_unique_name.extend(['pcu', 'total'])
            report_config_list = car_type_unique_name
            
            for config in report_config_list:
                report['inbound'][config] = {
                    'data': [],
                    'total': 0
                }
                report['outbound'][config] = {
                    'data': [],
                    'total': 0
                }

                for hour in time_range_hours_list:
                    inbound_data = {
                        'time': hour,
                        'date': date,
                        'volume': 0
                    }
                    outbound_data = {
                        'time': hour,
                        'date': date,
                        'volume': 0
                    }

                    report['inbound'][config]['data'].append(inbound_data)
                    report['outbound'][config]['data'].append(outbound_data)
            
            data = {
                'car_type': car_type_data,
                'graph': graph,
                'report': report,
                'report_quarter_hour': report_quarter_hour
            }

        return data


    def get_day_range_time_type_dir_data(self, start_date, end_date, checkpoint_id,type):
        if(type == '0'):
            query_data = self.record_repository.get_time_type_direction_by_date_range(
                start_date=start_date, end_date=end_date, checkpoint_id=checkpoint_id
            )
        elif(type == '1'):
            query_data = self.violation_repository.get_time_type_direction_by_date_range(
                start_date=start_date, end_date=end_date, checkpoint_id=checkpoint_id
            )
        range_date = end_date - start_date
        range_date = range_date.days

        car_type_list_id = self.vehicle_type_repo.get_list_id()
        car_type_list_name = self.vehicle_type_repo.get_list_name()
        car_type_unique_name = self.vehicle_type_repo.get_list_active_name()

        ## to dataframe
        df = pd.DataFrame(query_data)
        df = df.rename(
            columns={
                'time_range_id': 'time',
                'car_type_id': 'car_type'
            }
        )
        df['car_type'] = df['car_type'].replace(
            car_type_list_id, car_type_list_name
        )
        df = df[['time', 'direction', 'car_type', 'volume']].groupby(by=['time', 'direction', 'car_type']).sum()
        df = df.reset_index()

        df['pcu'] = 0
        name_pcu_list = self.vehicle_type_repo.get_list_active_name_pcu()

        for item_data in name_pcu_list:
            df.loc[df['car_type'] == item_data['name'], 'pcu'] = item_data['pcu']

        time_range_ids, time_range_end_times = self.get_time_range_data()

        rush_hour_list = []

        for rush_hour_config in self.rush_hour_config:
            rush_hour_ids = [id for id in range(rush_hour_config['start'], rush_hour_config['end'] + 1)]
            rush_hour_list.append(rush_hour_ids)
        
        zero_value = len(df[df['volume'].isin([0])].index)

        report_direction_data = {
            'inbound': {},
            'outbound': {}
        }

        report_rush_hour_data = {
            'inbound': {},
            'outbound': {}
        }

        if zero_value != len(df.index):

            df_direction = df[['time', 'direction', 'volume']].groupby(by=['time', 'direction']).sum()
            df_direction = df_direction.reset_index()

            ## inbound direction
            df_direction_inbound = df_direction[df_direction['direction'] == 'IN'].sort_values(by=['time'])
            df_direction_inbound = df_direction_inbound.reset_index(drop=True)
            df_direction_inbound = df_direction_inbound[['time', 'volume']]

            volume_direction_inbound = df_direction_inbound[['volume']].groupby(df_direction_inbound.index // self.hour_range).sum()
            df_direction_inbound = df_direction_inbound[df_direction_inbound.index % self.hour_range == (self.hour_range - 1)]
            df_direction_inbound['volume'] = volume_direction_inbound['volume'].to_list()
            df_direction_inbound['volume_mean'] = df_direction_inbound['volume'] / range_date
            df_direction_inbound[['time']] = df_direction_inbound[['time']].replace(
                time_range_ids, time_range_end_times
            )
            df_direction_inbound[['time']] = df_direction_inbound[['time']].replace('00:00', '24:00')

            total_direction_inbound = df_direction_inbound['volume'].sum()
            mean_direction_inbound = total_direction_inbound / range_date
            total_direction_inbound_data = {
                'volume': total_direction_inbound,
                'volume_mean': mean_direction_inbound
            }

            report_direction_data['inbound']['data'] = df_direction_inbound.to_dict('records')
            report_direction_data['inbound']['total'] = total_direction_inbound_data


            ## outbound direction
            df_direction_outbound = df_direction[df_direction['direction'] == 'OUT'].sort_values(by=['time'])
            df_direction_outbound = df_direction_outbound.reset_index(drop=True)
            df_direction_outbound = df_direction_outbound[['time', 'volume']]

            volume_direction_outbound = df_direction_outbound[['volume']].groupby(df_direction_outbound.index // self.hour_range).sum()
            df_direction_outbound = df_direction_outbound[df_direction_outbound.index % self.hour_range == (self.hour_range - 1)]
            df_direction_outbound['volume'] = volume_direction_outbound['volume'].to_list()
            df_direction_outbound['volume_mean'] = df_direction_outbound['volume'] / range_date
            df_direction_outbound[['time']] = df_direction_outbound[['time']].replace(
                time_range_ids, time_range_end_times
            )
            df_direction_outbound[['time']] = df_direction_outbound[['time']].replace('00:00', '24:00')

            total_direction_outbound = df_direction_outbound['volume'].sum()
            mean_direction_outbound = total_direction_outbound / range_date
            total_direction_outbound_data = {
                'volume': total_direction_outbound,
                'volume_mean': mean_direction_outbound
            }

            report_direction_data['outbound']['data'] = df_direction_outbound.to_dict('records')
            report_direction_data['outbound']['total'] = total_direction_outbound_data


            for car_type in car_type_unique_name:

                report_rush_hour_data['inbound'][car_type] = {}
                report_rush_hour_data['inbound'][car_type]['data'] = []

                report_rush_hour_data['outbound'][car_type] = {}
                report_rush_hour_data['outbound'][car_type]['data'] = []

                for rush_hour in rush_hour_list:
                    report_car_type = df[
                        (df['car_type'] == car_type) &
                        (df['time'].isin(rush_hour))
                    ]

                    inbound_report_car_type = report_car_type[report_car_type['direction'] == 'IN']['volume'].sum()
                    outbound_report_car_type = report_car_type[report_car_type['direction'] == 'OUT']['volume'].sum()

                    report_rush_hour_data['inbound'][car_type]['data'].append(inbound_report_car_type)
                    report_rush_hour_data['outbound'][car_type]['data'].append(outbound_report_car_type)
                
                inbound_report_car_type_total = df[
                    (df['car_type'] == car_type) &
                    (df['direction'] == 'IN')
                ]['volume'].sum()

                report_rush_hour_data['inbound'][car_type]['total'] = inbound_report_car_type_total

                outbound_report_car_type_total = df[
                    (df['car_type'] == car_type) &
                    (df['direction'] == 'OUT')
                ]['volume'].sum()

                report_rush_hour_data['outbound'][car_type]['total'] = outbound_report_car_type_total
            

            report_rush_hour_data['inbound']['pcu'] = {}
            report_rush_hour_data['inbound']['total'] = {}
            report_rush_hour_data['inbound']['pcu']['data'] = []
            report_rush_hour_data['inbound']['total']['data'] = []

            report_rush_hour_data['outbound']['pcu'] = {}
            report_rush_hour_data['outbound']['total'] = {}
            report_rush_hour_data['outbound']['pcu']['data'] = []
            report_rush_hour_data['outbound']['total']['data'] = []

            df_pcu = df
            pcu_value = df_pcu.volume * df_pcu.pcu
            df_pcu['pcu_value'] = pcu_value

            for rush_hour in rush_hour_list:
                df_pcu_rush_hour = df_pcu[df_pcu['time'].isin(rush_hour)]

                inbound_pcu = df_pcu_rush_hour[df_pcu_rush_hour['direction'] == 'IN']['pcu_value'].sum()
                outbound_pcu = df_pcu_rush_hour[df_pcu_rush_hour['direction'] == 'OUT']['pcu_value'].sum()

                report_rush_hour_data['inbound']['pcu']['data'].append(inbound_pcu)
                report_rush_hour_data['outbound']['pcu']['data'].append(outbound_pcu)

                df_total_rush_hour = df[df['time'].isin(rush_hour)]
                inbound_total = df_total_rush_hour[df_total_rush_hour['direction'] == 'IN']['volume'].sum()
                outbound_total = df_total_rush_hour[df_total_rush_hour['direction'] == 'OUT']['volume'].sum()

                report_rush_hour_data['inbound']['total']['data'].append(inbound_total)
                report_rush_hour_data['outbound']['total']['data'].append(outbound_total)

            report_rush_hour_data['inbound']['pcu']['total'] = df_pcu[df_pcu['direction'] == 'IN']['pcu_value'].sum()
            report_rush_hour_data['outbound']['pcu']['total'] = df_pcu[df_pcu['direction'] == 'OUT']['pcu_value'].sum()

            report_rush_hour_data['inbound']['total']['total'] = df[df['direction'] == 'IN']['volume'].sum()
            report_rush_hour_data['outbound']['total']['total'] = df[df['direction'] == 'OUT']['volume'].sum()

        else:
            time_range_hours_list = [
                '01:00', '02:00', '03:00', '04:00', '05:00', '06:00',
                '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00',
                '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
                '21:00', '22:00', '23:00', '24:00'
            ]

            car_type_unique_name.extend(['pcu', 'total'])
            config_name = car_type_unique_name

            report_direction_data['inbound']['data'] = []
            report_direction_data['outbound']['data'] = []

            report_direction_data['inbound']['total'] = 0
            report_direction_data['outbound']['total'] = 0

            for time_range in time_range_hours_list:
                direction_data = {
                    'time': time_range,
                    'volume': 0,
                    'volume_mean': 0
                }

                report_direction_data['inbound']['data'].append(direction_data)
                report_direction_data['outbound']['data'].append(direction_data)
            
            for config in config_name:
                report_rush_hour_data['inbound'][config] = {}
                report_rush_hour_data['inbound'][config]['data'] = []
                report_rush_hour_data['inbound'][config]['total'] = 0

                report_rush_hour_data['outbound'][config] = {}
                report_rush_hour_data['outbound'][config]['data'] = []
                report_rush_hour_data['outbound'][config]['total'] = 0

                for rush_hour in range(len(self.rush_hour_config)):
                    report_rush_hour_data['inbound'][config]['data'].append(0)
                    report_rush_hour_data['outbound'][config]['data'].append(0)

        return report_direction_data, report_rush_hour_data


    def get_day_range_data(self, start_date, end_date, checkpoint_id,type):
        if(type == '0'):
            query_data = self.record_repository.get_by_date_range(
                start_date=start_date, end_date=end_date, checkpoint_id=checkpoint_id
            )
        elif(type == '1'):
            query_data = self.violation_repository.get_by_date_range(
                start_date=start_date, end_date=end_date, checkpoint_id=checkpoint_id
            )
        car_type_list_id = self.vehicle_type_repo.get_list_id()
        car_type_list_name = self.vehicle_type_repo.get_list_name()
        car_type_unique_name = self.vehicle_type_repo.get_list_active_name()
        
        ## to dataframe
        df = pd.DataFrame(query_data)
        df = df.rename(
            columns={
                'time_range_id': 'time',
                'car_type_id': 'car_type'
            }
        )
        df['car_type'] = df['car_type'].replace(
            car_type_list_id, car_type_list_name
        )
        df['days'] = [datetime.datetime.strftime(day,"%A") for day in df['date']]
        df = df[['direction', 'car_type', 'date','days', 'volume']].groupby(by=['direction', 'car_type', 'date','days']).sum()
        df = df.reset_index()

        df['pcu'] = 0
        name_pcu_list = self.vehicle_type_repo.get_list_active_name_pcu()
       
        for item_data in name_pcu_list:
            df.loc[df['car_type'] == item_data['name'], 'pcu'] = item_data['pcu']

        zero_value = len(df[df['volume'].isin([0])].index)

        if zero_value != len(df.index):
            df_car_type = df[['car_type', 'volume']].groupby(by='car_type').sum()
            df_car_type = df_car_type.reset_index()
            df_car_type['percent'] = 0
            if(df_car_type['volume'].sum() != 0):
                df_car_type['percent'] = (df_car_type['volume'] / df_car_type['volume'].sum()) * 100
                
            car_type_data = df_car_type[['car_type', 'volume']].to_dict('records')
            car_type_percent_data = df_car_type[['car_type', 'percent']].to_dict('records')

            ## graph
            df_graph = df[['direction', 'date', 'volume','days']].groupby(by=['direction', 'date','days']).sum()
            df_graph = df_graph.reset_index()

            df_graph_inbound = df_graph[df_graph['direction'] == 'IN'][['date', 'volume','days']]
            graph_inbound_data = df_graph_inbound.to_dict('records')

            df_graph_outbound = df_graph[df_graph['direction'] == 'OUT'][['date', 'volume','days']]
            graph_outbound_data = df_graph_outbound.to_dict('records')

            report_data = {
                'inbound': {},
                'outbound': {}
            }

            ####### INBOUND #########

            for car_type in car_type_unique_name:
                report_car_type = df[(df['car_type'] == car_type) & (df['direction'] == 'IN')]
                report_car_type = report_car_type[['date', 'volume','days']]

                report_data['inbound'][car_type] = {}
                report_data['inbound'][car_type]['data'] = report_car_type.to_dict('records')
                report_data['inbound'][car_type]['total'] = report_car_type['volume'].sum()


            ## pcu inbound
            df_pcu = df[df['direction'] == 'IN']
            df_pcu = df_pcu[['date', 'car_type', 'volume', 'pcu','days']].groupby(by=['car_type', 'date','pcu','days']).sum()
            df_pcu = df_pcu.reset_index()

            pcu_value = df_pcu.volume * df_pcu.pcu
            df_pcu['pcu_value'] = pcu_value

            df_pcu = df_pcu[['date', 'pcu_value','days']].groupby(by=['date','days']).sum()
            df_pcu = df_pcu.reset_index()
            df_pcu = df_pcu.rename(columns={
                'pcu_value': 'volume'
            })

            pcu = df_pcu.to_dict('records')
            report_data['inbound']['pcu'] = {}
            report_data['inbound']['pcu']['data'] = pcu
            report_data['inbound']['pcu']['total'] = df_pcu['volume'].sum()


            ## total group by time inbound
            df_total = df[df['direction'] == 'IN']
            df_total = df_total[['date', 'volume','days']].groupby(by=['date','days']).sum()
            df_total = df_total.reset_index()

            total_by_time = df_total.to_dict('records')
            report_data['inbound']['total'] = {}
            report_data['inbound']['total']['data'] = total_by_time
            report_data['inbound']['total']['total'] = df_total['volume'].sum()

            ####### OUTBOUND #########

            for car_type in car_type_unique_name:
                report_car_type = df[(df['car_type'] == car_type) & (df['direction'] == 'OUT')]
                report_car_type = report_car_type[['date', 'volume','days']]

                report_data['outbound'][car_type] = {}
                report_data['outbound'][car_type]['data'] = report_car_type.to_dict('records')
                report_data['outbound'][car_type]['total'] = report_car_type['volume'].sum()


            ## pcu outbound
            df_pcu = df[df['direction'] == 'OUT']
            df_pcu = df_pcu[['date', 'car_type', 'volume', 'pcu','days']].groupby(by=['car_type', 'date','pcu','days']).sum()
            df_pcu = df_pcu.reset_index()

            pcu_value = df_pcu.volume * df_pcu.pcu
            df_pcu['pcu_value'] = pcu_value

            df_pcu = df_pcu[['date', 'pcu_value','days']].groupby(by=['date','days']).sum()
            df_pcu = df_pcu.reset_index()
            df_pcu = df_pcu.rename(columns={
                'pcu_value': 'volume'
            })

            pcu = df_pcu.to_dict('records')
            report_data['outbound']['pcu'] = {}
            report_data['outbound']['pcu']['data'] = pcu
            report_data['outbound']['pcu']['total'] = df_pcu['volume'].sum()


            ## total group by time outbound
            df_total = df[df['direction'] == 'OUT']
            df_total = df_total[['date', 'volume','days']].groupby(by=['date','days']).sum()
            df_total = df_total.reset_index()

            total_by_time = df_total.to_dict('records')
            report_data['outbound']['total'] = {}
            report_data['outbound']['total']['data'] = total_by_time
            report_data['outbound']['total']['total'] = df_total['volume'].sum()
            
            data = {
                'car_type': {
                    'volume': car_type_data,
                    'percent': car_type_percent_data
                },
                'graph': {
                    'inbound': graph_inbound_data,
                    'outbound': graph_outbound_data
                },
                'report': report_data
            }
        else:
            date_list = df['date'].dt.strftime(self.date_format).unique()
            days_list = [datetime.datetime.strftime(day,"%A") for day in df['date']]

            car_type_data = {
                'volume': [],
                'percent': []
            }

            for car_type in car_type_unique_name:
                volume_data = {
                    'car_type': car_type,
                    'volume': 0
                }
                percent_data = {
                    'car_type': car_type,
                    'percent': 0
                }

                car_type_data['volume'].append(volume_data)
                car_type_data['percent'].append(percent_data)

            graph = {
                'inbound': [],
                'outbound': []
            }
            
            report = {
                'inbound': {},
                'outbound': {}
            }

            car_type_unique_name.extend(['pcu', 'total'])
            report_config_list = car_type_unique_name

            for config in report_config_list:
                report['inbound'][config] = {
                    'data': [],
                    'total': 0
                }
                report['outbound'][config] = {
                    'data': [],
                    'total': 0
                }

                for (date_,day_) in zip(date_list,days_list):
                    inbound_data = {
                        'date': date_,
                        'volume': 0,
                        'days':day_
                    }
                    outbound_data = {
                        'date': date_,
                        'volume': 0,
                        'days':day_
                    }

                    report['inbound'][config]['data'].append(inbound_data)
                    report['outbound'][config]['data'].append(outbound_data)
            
            data = {
                'car_type': car_type_data,
                'graph': graph,
                'report': report
            }

        return data


    def get_year_time_type_dir_data(self, year, checkpoint_id,type):
        if(type == '0'):
            query_data = self.record_repository.get_time_type_direction_by_year(
                year=year, checkpoint_id=checkpoint_id
            )
        elif(type == '1'):
            query_data = self.violation_repository.get_time_type_direction_by_year(
                year=year, checkpoint_id=checkpoint_id
            )    

        year_datetime = datetime.datetime.strptime(str(year), '%Y')
        plus_year = year_datetime + relativedelta(years=1)
        delta_year = plus_year - year_datetime

        range_date = delta_year.days

        car_type_list_id = self.vehicle_type_repo.get_list_id()
        car_type_list_name = self.vehicle_type_repo.get_list_name()
        car_type_unique_name = self.vehicle_type_repo.get_list_active_name()

        ## to dataframe
        df = pd.DataFrame(query_data)
        print("df cols", df.columns)
        df = df.rename(
            columns={
                'time_range_id': 'time',
                'car_type_id': 'car_type'
            }
        )
        df['car_type'] = df['car_type'].replace(
            car_type_list_id, car_type_list_name
        )
        df = df[['time', 'direction', 'car_type', 'volume']].groupby(by=['time', 'direction', 'car_type']).sum()
        df = df.reset_index()

        df['pcu'] = 0
        name_pcu_list = self.vehicle_type_repo.get_list_active_name_pcu()

        for item_data in name_pcu_list:
            df.loc[df['car_type'] == item_data['name'], 'pcu'] = item_data['pcu']

        time_range_ids, time_range_end_times = self.get_time_range_data()

        rush_hour_list = []

        for rush_hour_config in self.rush_hour_config:
            rush_hour_ids = [id for id in range(rush_hour_config['start'], rush_hour_config['end'] + 1)]
            rush_hour_list.append(rush_hour_ids)

        report_direction_data = {
            'inbound': {},
            'outbound': {}
        }

        report_rush_hour_data = {
            'inbound': {},
            'outbound': {}
        }

        df_direction = df[['time', 'direction', 'volume']].groupby(by=['time', 'direction']).sum()
        df_direction = df_direction.reset_index()

        ## inbound direction
        df_direction_inbound = df_direction[df_direction['direction'] == 'IN'].sort_values(by=['time'])
        df_direction_inbound = df_direction_inbound.reset_index(drop=True)
        df_direction_inbound = df_direction_inbound[['time', 'volume']]

        volume_direction_inbound = df_direction_inbound[['volume']].groupby(df_direction_inbound.index // self.hour_range).sum()
        df_direction_inbound = df_direction_inbound[df_direction_inbound.index % self.hour_range == (self.hour_range - 1)]
        df_direction_inbound['volume'] = volume_direction_inbound['volume'].to_list()
        df_direction_inbound['volume_mean'] = df_direction_inbound['volume'] / range_date
        df_direction_inbound[['time']] = df_direction_inbound[['time']].replace(
            time_range_ids, time_range_end_times
        )
        df_direction_inbound[['time']] = df_direction_inbound[['time']].replace('00:00', '24:00')

        total_direction_inbound = df_direction_inbound['volume'].sum()
        mean_direction_inbound = total_direction_inbound / range_date
        total_direction_inbound_data = {
            'volume': total_direction_inbound,
            'volume_mean': mean_direction_inbound
        }

        report_direction_data['inbound']['data'] = df_direction_inbound.to_dict('records')
        report_direction_data['inbound']['total'] = total_direction_inbound_data


        ## outbound direction
        df_direction_outbound = df_direction[df_direction['direction'] == 'OUT'].sort_values(by=['time'])
        df_direction_outbound = df_direction_outbound.reset_index(drop=True)
        df_direction_outbound = df_direction_outbound[['time', 'volume']]

        volume_direction_outbound = df_direction_outbound[['volume']].groupby(df_direction_outbound.index // self.hour_range).sum()
        df_direction_outbound = df_direction_outbound[df_direction_outbound.index % self.hour_range == (self.hour_range - 1)]
        df_direction_outbound['volume'] = volume_direction_outbound['volume'].to_list()
        df_direction_outbound['volume_mean'] = df_direction_outbound['volume'] / range_date
        df_direction_outbound[['time']] = df_direction_outbound[['time']].replace(
            time_range_ids, time_range_end_times
        )
        df_direction_outbound[['time']] = df_direction_outbound[['time']].replace('00:00', '24:00')

        total_direction_outbound = df_direction_outbound['volume'].sum()
        mean_direction_outbound = total_direction_outbound / range_date
        total_direction_outbound_data = {
            'volume': total_direction_outbound,
            'volume_mean': mean_direction_outbound
        }

        report_direction_data['outbound']['data'] = df_direction_outbound.to_dict('records')
        report_direction_data['outbound']['total'] = total_direction_outbound_data


        for car_type in car_type_unique_name:

            report_rush_hour_data['inbound'][car_type] = {}
            report_rush_hour_data['inbound'][car_type]['data'] = []

            report_rush_hour_data['outbound'][car_type] = {}
            report_rush_hour_data['outbound'][car_type]['data'] = []

            for rush_hour in rush_hour_list:
                report_car_type = df[
                    (df['car_type'] == car_type) &
                    (df['time'].isin(rush_hour))
                ]

                inbound_report_car_type = report_car_type[report_car_type['direction'] == 'IN']['volume'].sum()
                outbound_report_car_type = report_car_type[report_car_type['direction'] == 'OUT']['volume'].sum()

                report_rush_hour_data['inbound'][car_type]['data'].append(inbound_report_car_type)
                report_rush_hour_data['outbound'][car_type]['data'].append(outbound_report_car_type)
            
            inbound_report_car_type_total = df[
                (df['car_type'] == car_type) &
                (df['direction'] == 'IN')
            ]['volume'].sum()

            report_rush_hour_data['inbound'][car_type]['total'] = inbound_report_car_type_total

            outbound_report_car_type_total = df[
                (df['car_type'] == car_type) &
                (df['direction'] == 'OUT')
            ]['volume'].sum()

            report_rush_hour_data['outbound'][car_type]['total'] = outbound_report_car_type_total
        

        report_rush_hour_data['inbound']['pcu'] = {}
        report_rush_hour_data['inbound']['total'] = {}
        report_rush_hour_data['inbound']['pcu']['data'] = []
        report_rush_hour_data['inbound']['total']['data'] = []

        report_rush_hour_data['outbound']['pcu'] = {}
        report_rush_hour_data['outbound']['total'] = {}
        report_rush_hour_data['outbound']['pcu']['data'] = []
        report_rush_hour_data['outbound']['total']['data'] = []

        df_pcu = df
        pcu_value = df_pcu.volume * df_pcu.pcu
        df_pcu['pcu_value'] = pcu_value

        for rush_hour in rush_hour_list:
            df_pcu_rush_hour = df_pcu[df_pcu['time'].isin(rush_hour)]

            inbound_pcu = df_pcu_rush_hour[df_pcu_rush_hour['direction'] == 'IN']['pcu_value'].sum()
            outbound_pcu = df_pcu_rush_hour[df_pcu_rush_hour['direction'] == 'OUT']['pcu_value'].sum()

            report_rush_hour_data['inbound']['pcu']['data'].append(inbound_pcu)
            report_rush_hour_data['outbound']['pcu']['data'].append(outbound_pcu)

            df_total_rush_hour = df[df['time'].isin(rush_hour)]
            inbound_total = df_total_rush_hour[df_total_rush_hour['direction'] == 'IN']['volume'].sum()
            outbound_total = df_total_rush_hour[df_total_rush_hour['direction'] == 'OUT']['volume'].sum()

            report_rush_hour_data['inbound']['total']['data'].append(inbound_total)
            report_rush_hour_data['outbound']['total']['data'].append(outbound_total)

        report_rush_hour_data['inbound']['pcu']['total'] = df_pcu[df_pcu['direction'] == 'IN']['pcu_value'].sum()
        report_rush_hour_data['outbound']['pcu']['total'] = df_pcu[df_pcu['direction'] == 'OUT']['pcu_value'].sum()

        report_rush_hour_data['inbound']['total']['total'] = df[df['direction'] == 'IN']['volume'].sum()
        report_rush_hour_data['outbound']['total']['total'] = df[df['direction'] == 'OUT']['volume'].sum()


        return report_direction_data, report_rush_hour_data


    def get_year_data(self, year, checkpoint_id,type):
        if(type == '0'):
            query_data = self.record_repository.get_by_year(
                year=year, checkpoint_id=checkpoint_id
            )
        elif(type == '1'):
            query_data = self.violation_repository.get_by_year(
                year=year, checkpoint_id=checkpoint_id
            )
        car_type_list_id = self.vehicle_type_repo.get_list_id()
        car_type_list_name = self.vehicle_type_repo.get_list_name()
        car_type_unique_name = self.vehicle_type_repo.get_list_active_name()

        ## to dataframe
        df = pd.DataFrame(query_data)

        df = df.rename(
            columns={
                'date__month': 'month',
                'car_type_id': 'car_type'
            }
        )
        df['car_type'] = df['car_type'].replace(
            car_type_list_id, car_type_list_name
        )
        df['year'] = year
        df = df[['direction', 'car_type','year','month', 'volume']].groupby(by=['direction','year', 'car_type', 'month']).sum()
        df = df.reset_index()

        df['pcu'] = 0
        name_pcu_list = self.vehicle_type_repo.get_list_active_name_pcu()

        for item_data in name_pcu_list:
            df.loc[df['car_type'] == item_data['name'], 'pcu'] = item_data['pcu']

        df_car_type = df[['car_type', 'volume']].groupby(by='car_type').sum()
        df_car_type = df_car_type.reset_index()
        df_car_type['percent'] = 0
        if(df_car_type['volume'].sum() != 0):
            df_car_type['percent'] = (df_car_type['volume'] / df_car_type['volume'].sum()) * 100

        car_type_data = df_car_type[['car_type', 'volume']].to_dict('records')
        car_type_percent_data = df_car_type[['car_type', 'percent']].to_dict('records')

        ## graph
        df_graph = df[['direction', 'year','month', 'volume']].groupby(by=['direction', 'year','month']).sum()
        df_graph = df_graph.reset_index()

        df_graph_inbound = df_graph[df_graph['direction'] == 'IN'][['year','month', 'volume']]
        graph_inbound_data = df_graph_inbound.to_dict('records')

        df_graph_outbound = df_graph[df_graph['direction'] == 'OUT'][['year','month', 'volume']]
        graph_outbound_data = df_graph_outbound.to_dict('records')

        report_data = {
            'inbound': {},
            'outbound': {}
        }

        ####### INBOUND #########

        for car_type in car_type_unique_name:
            report_car_type = df[(df['car_type'] == car_type) & (df['direction'] == 'IN')]
            report_car_type = report_car_type[['year','month', 'volume']]

            report_data['inbound'][car_type] = {}
            report_data['inbound'][car_type]['data'] = report_car_type.to_dict('records')
            report_data['inbound'][car_type]['total'] = report_car_type['volume'].sum()


        ## pcu inbound
        df_pcu = df[df['direction'] == 'IN']
        df_pcu = df_pcu[['year','month', 'car_type', 'volume', 'pcu']].groupby(by=['car_type', 'year','month','pcu']).sum()
        df_pcu = df_pcu.reset_index()

        pcu_value = df_pcu.volume * df_pcu.pcu
        df_pcu['pcu_value'] = pcu_value

        df_pcu = df_pcu[['year','month', 'pcu_value']].groupby(by=['year','month']).sum()
        df_pcu = df_pcu.reset_index()
        df_pcu = df_pcu.rename(columns={
            'pcu_value': 'volume'
        })

        pcu = df_pcu.to_dict('records')
        report_data['inbound']['pcu'] = {}
        report_data['inbound']['pcu']['data'] = pcu
        report_data['inbound']['pcu']['total'] = df_pcu['volume'].sum()


        ## total group by time inbound
        df_total = df[df['direction'] == 'IN']
        df_total = df_total[['year','month', 'volume',]].groupby(by=['year','month']).sum()
        df_total = df_total.reset_index()

        total_by_time = df_total.to_dict('records')
        report_data['inbound']['total'] = {}
        report_data['inbound']['total']['data'] = total_by_time
        report_data['inbound']['total']['total'] = df_total['volume'].sum()

        ####### OUTBOUND #########

        for car_type in car_type_unique_name:
            report_car_type = df[(df['car_type'] == car_type) & (df['direction'] == 'OUT')]
            report_car_type = report_car_type[['year','month', 'volume']]

            report_data['outbound'][car_type] = {}
            report_data['outbound'][car_type]['data'] = report_car_type.to_dict('records')
            report_data['outbound'][car_type]['total'] = report_car_type['volume'].sum()


        ## pcu outbound
        df_pcu = df[df['direction'] == 'OUT']
        df_pcu = df_pcu[['year','month', 'car_type', 'volume', 'pcu']].groupby(by=['car_type','year', 'month','pcu']).sum()
        df_pcu = df_pcu.reset_index()

        pcu_value = df_pcu.volume * df_pcu.pcu
        df_pcu['pcu_value'] = pcu_value

        df_pcu = df_pcu[['year','month', 'pcu_value']].groupby(by=['year','month']).sum()
        df_pcu = df_pcu.reset_index()
        df_pcu = df_pcu.rename(columns={
            'pcu_value': 'volume'
        })

        pcu = df_pcu.to_dict('records')
        report_data['outbound']['pcu'] = {}
        report_data['outbound']['pcu']['data'] = pcu
        report_data['outbound']['pcu']['total'] = df_pcu['volume'].sum()


        ## total group by time outbound
        df_total = df[df['direction'] == 'OUT']
        df_total = df_total[['year','month', 'volume',]].groupby(by=['year','month']).sum()
        df_total = df_total.reset_index()

        total_by_time = df_total.to_dict('records')
        report_data['outbound']['total'] = {}
        report_data['outbound']['total']['data'] = total_by_time
        report_data['outbound']['total']['total'] = df_total['volume'].sum()

        data = {
            'car_type': {
                'volume': car_type_data,
                'percent': car_type_percent_data
            },
            'graph': {
                'inbound': graph_inbound_data,
                'outbound': graph_outbound_data
            },
            'report': report_data
        }

        return data


    def get_data(self, type, datetime_value, checkpoint_id):

        if type == 'day':
            date_query = self.traffic_detail_validator.validate_type_day(
                datetime_value=datetime_value
            )
            data = self.get_day_data(
                date=date_query, checkpoint_id=checkpoint_id,type = '0'
            )
            data['violation']= self.get_day_data(
                date=date_query, checkpoint_id=checkpoint_id,type = '1'
            )

        elif type == 'week':
            start_date, end_date = self.traffic_detail_validator.validate_type_week(
                datetime_value=datetime_value
            )
            data = self.get_day_range_data(
                start_date=start_date, end_date=end_date, checkpoint_id=checkpoint_id,type = '0'
            )
            time_type_dir_data, report_rush_hour_data = self.get_day_range_time_type_dir_data(
                start_date=start_date, end_date=end_date, checkpoint_id=checkpoint_id,type='0'
            )
            data['violation']= self.get_day_range_data(
                start_date=start_date, end_date=end_date, checkpoint_id=checkpoint_id,type = '1'
            )
            time_violation_type_dir_data, report_violation_rush_hour_data = self.get_day_range_time_type_dir_data(
                start_date=start_date, end_date=end_date, checkpoint_id=checkpoint_id,type='1'
            )

            data['report_direction'] = time_type_dir_data
            data['report_rush_hour'] = report_rush_hour_data
            data['violation_report_direction'] = time_violation_type_dir_data
            data['violation_report_rush_hour'] = report_violation_rush_hour_data

        elif type == 'month':
            start_date, end_date = self.traffic_detail_validator.validate_type_month(
                datetime_value=datetime_value
            )
            data = self.get_day_range_data(
                start_date=start_date, end_date=end_date, checkpoint_id=checkpoint_id,type = '0'
            )
            time_type_dir_data, report_rush_hour_data = self.get_day_range_time_type_dir_data(
                start_date=start_date, end_date=end_date, checkpoint_id=checkpoint_id,type = '0'
            )
            data['violation']= self.get_day_range_data(
                start_date=start_date, end_date=end_date, checkpoint_id=checkpoint_id,type = '1'
            )
            time_violation_type_dir_data, report_violation_rush_hour_data = self.get_day_range_time_type_dir_data(
                start_date=start_date, end_date=end_date, checkpoint_id=checkpoint_id,type='1'
            )

            data['report_direction'] = time_type_dir_data
            data['report_rush_hour'] = report_rush_hour_data
            data['violation_report_direction'] = time_violation_type_dir_data
            data['violation_report_rush_hour'] = report_violation_rush_hour_data

        elif type == 'year':
            year = self.traffic_detail_validator.validate_type_year(
                datetime_value=datetime_value
            )
            data = self.get_year_data(
                year=year, checkpoint_id=checkpoint_id,type = '0'
            )
            time_type_dir_data, report_rush_hour_data = self.get_year_time_type_dir_data(
                year=year, checkpoint_id=checkpoint_id,type = '0'
            )
            data['violation'] = self.get_year_data(
                year=year, checkpoint_id=checkpoint_id,type = '1'
            )
            time_violation_type_dir_data, report_violation_rush_hour_data = self.get_year_time_type_dir_data(
                year=year, checkpoint_id=checkpoint_id,type = '1'
            )

            data['report_direction'] = time_type_dir_data
            data['report_rush_hour'] = report_rush_hour_data
            data['violation_report_direction'] = time_violation_type_dir_data
            data['violation_report_rush_hour'] = report_violation_rush_hour_data

        # elif type == 'range':
        #     start_date, end_date = self.traffic_detail_validator.validate_type_range(
        #         datetime_value=datetime_value
        #     )

        #     data = self.get_day_range_data(
        #         start_date=start_date, end_date=end_date, checkpoint_id=checkpoint_id
        #     )
        
        return data


