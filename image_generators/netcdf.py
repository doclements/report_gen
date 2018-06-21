import json


class netcdfImage(object):
    
    def __init__(self, config):
        data = json.load(config)
        self.title = data.title
        self.subtitle = self.conditionalAdd(data.subtitle)

    
    def conditionalAdd(self,item):
        if item is "null":
            return None
        return item


