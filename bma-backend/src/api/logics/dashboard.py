from api.logics.timePayloads import TimePayloadsLogic
from api.repositories.record import RecordRepository
from api.repositories.violation import ViolationRepository
from api.repositories.oracleCheckpoint import OracleCheckpointRepository

import pandas as pd

class DashboardLogic:

    def __init__(self):
        self.time_range_graph = {
            'days': 0,
            'hours': 6
        }
        self.top_rank = 3
        self.checkpoint_repo = OracleCheckpointRepository()

        self.time_payloads_logic = TimePayloadsLogic()
        self.record_repo = RecordRepository()
        self.violation_repo = ViolationRepository()


    def to_dataframe(self, data):
        df = pd.DataFrame(data)
        df = df.sort_values(by=['checkpoint_id'])
        df = df.rename(columns={"checkpoint_id": "checkpoint"})

        return df


    def get_list_df_inbound(self, payload, inbounds: list):
        inbound_df = self.record_repo.get_inbound_dashboard(
            payload=payload
        )
        # df = self.to_dataframe(data=inbound_data)
        inbounds.append(inbound_df)


    def get_list_df_outbound(self, payload, outbounds: list):
        outbound_df = self.record_repo.get_outbound_dashboard(
            payload=payload
        )
        # df = self.to_dataframe(data=inbound_data)
        outbounds.append(outbound_df)

    def get_list_violation_df_inbound(self, payload, inbounds: list):
        inbound_df = self.violation_repo.get_inbound_dashboard(
            payload=payload
        )
        inbounds.append(inbound_df)


    def get_list_violation_df_outbound(self, payload, outbounds: list):
        outbound_df = self.violation_repo.get_outbound_dashboard(
            payload=payload
        )
        outbounds.append(outbound_df)


    def summing_df(self, list_df: list):
        df_sum = pd.DataFrame()
        df_sum['direction'] = list_df[0]['direction']
        df_sum['checkpoint'] = list_df[0]['checkpoint']

        for index, df in enumerate(list_df):
            if index == 0:
                df_sum['volume'] = df['volume']
            else:
                df_sum['volume'] += df['volume']
        
        return df_sum


    def add_checkpoint_detail(self, list_data: list):
        ## get checkpoint api from oracle
        checkpoints = self.checkpoint_repo.get_all()

        for index, data in enumerate(list_data):
            index_ = data['checkpoint'] - 28
            list_data[index]['checkpoint'] = checkpoints[index_]
        return list_data


    def get_total(self):
        total = 0
        time_payloads = self.time_payloads_logic.get_query_time_payloads(
            time_config=self.time_range_graph
        )

        for payload in time_payloads: 
            total_ = self.record_repo.get_total(payload=payload)

            try:
                total += total_
            except:
                pass

        return total

    def get_violation_total(self):
        total = 0
        time_payloads = self.time_payloads_logic.get_query_time_payloads(
            time_config=self.time_range_graph
        )

        for payload in time_payloads: 
            total_ = self.violation_repo.get_total(payload=payload)

            try:
                total += total_
            except:
                pass

        return total


    def get_direction_volume(self):
        direction_total = {
            'inbound': 0,
            'outbound': 0
        }

        time_payloads = self.time_payloads_logic.get_query_time_payloads(
            time_config=self.time_range_graph
        )

        for payload in time_payloads:
            direction_total_ = self.record_repo.get_sum_group_by_dir(payload=payload)

            try:
                direction_total['inbound'] += direction_total_[0]['volume']
                direction_total['outbound'] += direction_total_[1]['volume']
            except:
                pass

        return direction_total
    
    def get_direction_violation_volume(self):
        direction_total = {
            'inbound': 0,
            'outbound': 0
        }

        time_payloads = self.time_payloads_logic.get_query_time_payloads(
            time_config=self.time_range_graph
        )

        for payload in time_payloads:
            direction_total_ = self.violation_repo.get_sum_group_by_dir(payload=payload)

            try:
                direction_total['inbound'] += direction_total_[0]['volume']
                direction_total['outbound'] += direction_total_[1]['volume']
            except:
                pass

        return direction_total


    def get_summing_df(self):
        inbounds = []
        outbounds = []

        time_payloads = self.time_payloads_logic.get_query_time_payloads(
            time_config=self.time_range_graph
        )

        for payload in time_payloads:
            self.get_list_df_inbound(payload=payload, inbounds=inbounds)
            self.get_list_df_outbound(payload=payload, outbounds=outbounds)

        df_inbounds = self.summing_df(list_df=inbounds)
        df_outbounds = self.summing_df(list_df=outbounds)
    
        return df_inbounds, df_outbounds

    def get_summing_violation_df(self):
        inbounds = []
        outbounds = []

        time_payloads = self.time_payloads_logic.get_query_time_payloads(
            time_config=self.time_range_graph
        )

        for payload in time_payloads:
            self.get_list_violation_df_inbound(payload=payload, inbounds=inbounds)
            self.get_list_violation_df_outbound(payload=payload, outbounds=outbounds)

        df_inbounds = self.summing_df(list_df=inbounds)
        df_outbounds = self.summing_df(list_df=outbounds)
    
        return df_inbounds, df_outbounds


    def get_top_rank(self):
        df_inbounds, df_outbounds = self.get_summing_df()
        df_sort_volume_inbound = df_inbounds.sort_values(by=['volume'], ascending=False)
        df_sort_volume_outbound = df_outbounds.sort_values(by=['volume'], ascending=False)

        df_sort_volume_inbound = df_sort_volume_inbound.drop(columns=['direction'])
        df_sort_volume_outbound = df_sort_volume_outbound.drop(columns=['direction'])

        top_rank_inbound_ = df_sort_volume_inbound[:self.top_rank].to_dict('records')
        top_rank_outbound_ = df_sort_volume_outbound[:self.top_rank].to_dict('records')

        top_rank_inbound = self.add_checkpoint_detail(list_data=top_rank_inbound_)
        top_rank_outbound = self.add_checkpoint_detail(list_data=top_rank_outbound_)

        data = {
            'inbound': top_rank_inbound,
            'outbound': top_rank_outbound
        }

        return data

    def get_top_violation_rank(self):
        df_inbounds, df_outbounds = self.get_summing_violation_df()
        df_sort_volume_inbound = df_inbounds.sort_values(by=['volume'], ascending=False)
        df_sort_volume_outbound = df_outbounds.sort_values(by=['volume'], ascending=False)

        df_sort_volume_inbound = df_sort_volume_inbound.drop(columns=['direction'])
        df_sort_volume_outbound = df_sort_volume_outbound.drop(columns=['direction'])

        top_rank_inbound_ = df_sort_volume_inbound[:self.top_rank].to_dict('records')
        top_rank_outbound_ = df_sort_volume_outbound[:self.top_rank].to_dict('records')

        top_rank_inbound = self.add_checkpoint_detail(list_data=top_rank_inbound_)
        top_rank_outbound = self.add_checkpoint_detail(list_data=top_rank_outbound_)

        data = {
            'inbound': top_rank_inbound,
            'outbound': top_rank_outbound
        }

        return data


    def get_graph_data(self):
        df_inbounds, df_outbounds = self.get_summing_df()

        summing_inbound = df_inbounds.to_dict('records')
        summing_outbound = df_outbounds.to_dict('records')

        inbound_data = self.add_checkpoint_detail(list_data=summing_inbound)
        outbound_data = self.add_checkpoint_detail(list_data=summing_outbound)

        data = {
            'inbound': inbound_data,
            'outbound': outbound_data
        }

        return data

    def get_violation_graph_data(self):
        df_inbounds, df_outbounds = self.get_summing_violation_df()

        summing_inbound = df_inbounds.to_dict('records')
        summing_outbound = df_outbounds.to_dict('records')

        inbound_data = self.add_checkpoint_detail(list_data=summing_inbound)
        outbound_data = self.add_checkpoint_detail(list_data=summing_outbound)

        data = {
            'inbound': inbound_data,
            'outbound': outbound_data
        }

        return data