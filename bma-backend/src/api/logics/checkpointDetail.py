from api.logics.timePayloads import TimePayloadsLogic
from api.repositories.record import RecordRepository
from api.repositories.violation import ViolationRepository
from api.repositories.timeRange import TimeRangeRepository

from api.repositories.oracleCheckpoint import OracleCheckpointRepository
from api.repositories.oracleVehicleType import OracleVehicleTypeRepository
from api.repositories.hikCamera import HikCameraRepository

import pandas as pd

class CheckpointDetailLogic:

    def __init__(self):
        self.time_range_graph = {
            'days': 0,
            'hours': 6
        }
        self.reduce_length = 3
        self.hour_range = 6
        self.vehicle_type_repo = OracleVehicleTypeRepository()

        self.time_payloads_logic = TimePayloadsLogic()
        self.record_repo = RecordRepository()
        self.violation_repo = ViolationRepository()
        self.time_range_repo = TimeRangeRepository()
        self.checkpoint_repo = OracleCheckpointRepository()
        self.hik_camera_repo = HikCameraRepository()


    def get_checkpoint_detail(self, checkpoint_id):
        checkpoint_detail = self.checkpoint_repo.get_by_id(id=checkpoint_id)

        return checkpoint_detail


    def get_total_cameras_status(self, checkpoint_id):
        area_code = self.checkpoint_repo.get_area_code_by_id(
            id=checkpoint_id
        )
        total_status = self.hik_camera_repo.get_total_camera_status(
            area_code=area_code
        )

        return total_status


    def get_total(self, checkpoint_id,type):
        total = 0
        total_record = 0
        time_payloads = self.time_payloads_logic.get_query_time_payloads(
            time_config=self.time_range_graph
        )
        if(type == '0'):
            for payload in time_payloads:
                total_ = self.record_repo.get_total_by_checkpoint(
                    payload=payload, checkpoint_id=checkpoint_id
                )
                total += total_
        elif(type == '1'):
            for payload in time_payloads:
                total_ = self.violation_repo.get_total_by_checkpoint(
                    payload=payload, checkpoint_id=checkpoint_id
                )
                total += total_
            for payload in time_payloads:
                total_ = self.record_repo.get_total_by_checkpoint(
                    payload=payload, checkpoint_id=checkpoint_id
                )
                total_record += total_
                
        return total,total_record
    
            

    def get_direction_volume(self, checkpoint_id,type):
        direction_total = {
            'inbound': 0,
            'outbound': 0
        }

        time_payloads = self.time_payloads_logic.get_query_time_payloads(
            time_config=self.time_range_graph
        )
        if(type == '0'):
            for payload in time_payloads:
                direction_total_ = self.record_repo.get_sum_group_by_dir_checkpoint(
                    payload=payload, checkpoint_id=checkpoint_id
                )
                direction_total['inbound'] += direction_total_[0]['volume']
                direction_total['outbound'] += direction_total_[1]['volume']
        elif(type == '1'):
            for payload in time_payloads:
                direction_total_ = self.violation_repo.get_sum_group_by_dir_checkpoint(
                    payload=payload, checkpoint_id=checkpoint_id
                )
                direction_total['inbound'] += direction_total_[0]['volume']
                direction_total['outbound'] += direction_total_[1]['volume']
            
        return direction_total


    def get_list_df(self, list_df, time_payloads, checkpoint_id,type):
        for payload in time_payloads:
            total = self.record_repo.get_sum_group_by_car_type(
                payload=payload, checkpoint_id=checkpoint_id
            )

            df = pd.DataFrame(total)
            list_df.append(df)
    
    def get_violation_list_df(self, list_df, time_payloads, checkpoint_id):
        for payload in time_payloads:
            total = self.violation_repo.get_sum_group_by_car_type(
                payload=payload, checkpoint_id=checkpoint_id
            )

            df = pd.DataFrame(total)
            list_df.append(df)


    def get_summing_df(self, list_df):
        df = pd.DataFrame()
        df['car_type'] = list_df[0]['car_type_id']

        for index, df_ in enumerate(list_df):
            if index == 0:
                df['volume'] = df_['volume']
            else:
                df['volume'] += df_['volume']
        
        ids = self.vehicle_type_repo.get_list_id()
        names = self.vehicle_type_repo.get_list_name()
        df[['car_type']] = df[['car_type']].replace(ids, names)

        return df

    def get_cartype_all_data(self):
        dfs = []
        time_payloads = self.time_payloads_logic.get_query_time_payloads(time_config=self.time_range_graph)
        self.get_list_all_df(
            list_df=dfs, time_payloads=time_payloads,type=type
        )
        df_sum = self.get_summing_df(list_df=dfs)
        df_sum = df_sum.groupby(by='car_type').sum()
        df_sum = df_sum.reset_index()
        zero_value = len(df_sum[df_sum['volume'].isin([0])].index)

        if zero_value != len(df_sum.index):
            df_sum['percent'] = (df_sum['volume'] / df_sum['volume'].sum()) * 100

            df_volume = df_sum[['car_type', 'volume']]
            df_percentage = df_sum[['car_type', 'percent']]

            data = {
                'volume': df_volume.to_dict('records'),
                'percent': df_percentage.to_dict('records')
            }
        else:
            data = {
                'volume': [],
                'percent': []
            }

            car_type_list = list(df_sum['car_type'])

            for car_type in car_type_list:
                volume_data = {
                    'car_type': car_type,
                    'volume': 0
                }
                percent_data = {
                    'car_type': car_type,
                    'volume': 0
                }

                data['volume'].append(volume_data)
                data['percent'].append(percent_data)

        return data

    def get_list_all_df(self, list_df, time_payloads,type):
        for payload in time_payloads:
            total = self.record_repo.get_all_car_type(payload=payload)
            df = pd.DataFrame(total)
            list_df.append(df)

    def get_cartype_data(self, checkpoint_id,type):
        if(type == '0'):
            dfs = []
            time_payloads = self.time_payloads_logic.get_query_time_payloads(
                time_config=self.time_range_graph
            )
            self.get_list_df(
                    list_df=dfs, time_payloads=time_payloads, checkpoint_id=checkpoint_id,type=type
            )
            df_sum = self.get_summing_df(list_df=dfs)
            df_sum = df_sum.groupby(by='car_type').sum()
            df_sum = df_sum.reset_index()
            zero_value = len(df_sum[df_sum['volume'].isin([0])].index)

            if zero_value != len(df_sum.index):
                df_sum['percent'] = (df_sum['volume'] / df_sum['volume'].sum()) * 100

                df_volume = df_sum[['car_type', 'volume']]
                df_percentage = df_sum[['car_type', 'percent']]

                data = {
                    'volume': df_volume.to_dict('records'),
                    'percent': df_percentage.to_dict('records')
                }
            else:
                data = {
                    'volume': [],
                    'percent': []
                }

                car_type_list = list(df_sum['car_type'])

                for car_type in car_type_list:
                    volume_data = {
                        'car_type': car_type,
                        'volume': 0
                    }
                    percent_data = {
                        'car_type': car_type,
                        'volume': 0
                    }

                    data['volume'].append(volume_data)
                    data['percent'].append(percent_data)

            return data
        elif(type == '1'):
            dfs = []
            time_payloads = self.time_payloads_logic.get_query_time_payloads(
                time_config=self.time_range_graph
            )
            self.get_violation_list_df(
                    list_df=dfs, time_payloads=time_payloads, checkpoint_id=checkpoint_id
                )
          
            df_sum = self.get_summing_df(list_df=dfs)
            df_sum = df_sum.groupby(by='car_type').sum()
            df_sum = df_sum.reset_index()

            zero_value = len(df_sum[df_sum['volume'].isin([0])].index)

            if zero_value != len(df_sum.index):
                df_sum['percent'] = (df_sum['volume'] / df_sum['volume'].sum()) * 100

                df_volume = df_sum[['car_type', 'volume']]
                df_percentage = df_sum[['car_type', 'percent']]

                data = {
                    'volume': df_volume.to_dict('records'),
                    'percent': df_percentage.to_dict('records')
                }
            else:
                data = {
                    'volume': [],
                    'percent': []
                }

                car_type_list = list(df_sum['car_type'])

                for car_type in car_type_list:
                    volume_data = {
                        'car_type': car_type,
                        'volume': 0
                    }
                    percent_data = {
                        'car_type': car_type,
                        'volume': 0
                    }

                    data['volume'].append(volume_data)
                    data['percent'].append(percent_data)

            return data


    def get_list_data(self, checkpoint_id):
        inbounds = []
        outbounds = []

        time_payloads = self.time_payloads_logic.get_query_time_payloads(
            time_config=self.time_range_graph
        )
        for payload in time_payloads:
            inbound_data = self.record_repo.get_inbound_checkpoint_time_range(
                payload=payload, checkpoint_id=checkpoint_id
            )
            outbound_data = self.record_repo.get_outbound_checkpoint_time_range(
                payload=payload, checkpoint_id=checkpoint_id
            )

            inbounds.extend(inbound_data)
            outbounds.extend(outbound_data)
        
        return inbounds, outbounds

    def get_violation_list_data(self, checkpoint_id):
        inbounds = []
        outbounds = []

        time_payloads = self.time_payloads_logic.get_query_time_payloads(
            time_config=self.time_range_graph
        )
        for payload in time_payloads:
            inbound_data = self.violation_repo.get_inbound_checkpoint_time_range(
                payload=payload, checkpoint_id=checkpoint_id
            )
            outbound_data = self.violation_repo.get_outbound_checkpoint_time_range(
                payload=payload, checkpoint_id=checkpoint_id
            )

            inbounds.extend(inbound_data)
            outbounds.extend(outbound_data)
        
        return inbounds, outbounds

    def aggregate_data(self, data: list):
        df = pd.DataFrame(data)
        df = df.rename(columns={
            'time_range_id': 'time'
        })

        time_ranges_data = self.time_range_repo.get_all()
        time_range_ids = [ time_range['id'] for time_range in time_ranges_data ]
        time_range_end_times = [ time_range['end_time'] for time_range in time_ranges_data ]

        volume = df[['volume']].groupby(df.index // self.hour_range).sum()
        df = df[df.index % self.hour_range == (self.hour_range - 1)]

        config_datetime = df[['time', 'date']]
        zero_value = len(df[df['volume'].isin([0])].index)

        if zero_value != len(df.index):
            df['volume'] = volume['volume'].to_list()
            df[['time']] = df[['time']].replace(
                time_range_ids, time_range_end_times
            )
            df[['time']] = df[['time']].replace('00:00', '24:00')

            records = df.to_dict('records')

        else:
            records = []
            config_datetime[['time']] = config_datetime[['time']].replace(
                time_range_ids, time_range_end_times
            )

            for i in range(len(config_datetime)):
                time = list(config_datetime['time'])[i]
                date = list(config_datetime['date'])[i]
                data = {
                    'time': time,
                    'date': date,
                    'volume': 0
                }

                records.append(data)

        return records


    def get_graph_data(self, checkpoint_id,type):
        inbounds_data = []
        outbounds_data = []
        if(type == '0'):
            inbounds, outbounds = self.get_list_data(checkpoint_id=checkpoint_id)
            inbounds_data = self.aggregate_data(data=inbounds)
            outbounds_data = self.aggregate_data(data=outbounds)
        elif(type == '1'):
            inbounds, outbounds = self.get_violation_list_data(checkpoint_id=checkpoint_id)
            inbounds_data = self.aggregate_data(data=inbounds)
            outbounds_data = self.aggregate_data(data=outbounds)
        

        data = {
            'inbound': inbounds_data,
            'outbound': outbounds_data
        }

        return data