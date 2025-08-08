from api.repositories.oracleCheckpoint import OracleCheckpointRepository
import json


class MenuBarLogic:

    def __init__(self):
        self.checkpoint_repo = OracleCheckpointRepository()


    def add_checkpoint_sub_layer(self, child, menus, index):
        try:
            checkpoints = self.checkpoint_repo.get_all()
            child[0]['checkpoints_data']
            sub_layer_path = child[0]['path']
            sub_layer_checkpoint = []

            for checkpoint in checkpoints:
                checkpoint_data = {
                    'id': checkpoint['id'],
                    'name': checkpoint['name'],
                    'short_name': checkpoint['short_name'],
                    'is_active': checkpoint['is_active'],
                    'path': sub_layer_path + '/' + str(checkpoint['id']),
                    'is_checkpoint': True,
                    'child_obj': []
                }

                sub_layer_checkpoint.append(checkpoint_data)

            menus[index]['child_obj'] = sub_layer_checkpoint

        except:
            pass
    

    def add_checkpoint_semi_sub_layer(self, child, menus, index):
        try:
            checkpoints = self.checkpoint_repo.get_all()

            for child_index, child_obj in enumerate(child):
                child_obj["child_obj"][0]["checkpoints_data"]
                semi_sub_layer_path = child_obj["child_obj"][0]["path"]
                semi_sub_layer_checkpoint = []

                for checkpoint in checkpoints:
                    checkpoint_data = {
                        'id': checkpoint['id'],
                        'name': checkpoint['name'],
                        'short_name': checkpoint['short_name'],
                        'is_active': checkpoint['is_active'],
                        'path': semi_sub_layer_path + '/' + str(checkpoint['id']),
                        'is_checkpoint': True,
                        'child_obj': []
                    }

                    semi_sub_layer_checkpoint.append(checkpoint_data)
                
                menus[index]['child_obj'][child_index]['child_obj'] = semi_sub_layer_checkpoint

        except:
            pass


    def formatting(self, menus):
        test = 1
        for index, menu in enumerate(menus):
            test = index
            child = menu['child_obj']
            decode = json.loads(child)
            menu['child_obj'] = decode
            if decode:
                self.add_checkpoint_sub_layer(
                    child=decode,
                    menus=menus,
                    index=index
                )

                self.add_checkpoint_semi_sub_layer(
                    child=decode,
                    menus=menus,
                    index=index
                )
            
        
        return menus