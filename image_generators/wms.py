import json
import uuid
import os

from owslib.wms import WebMapService

class wmsImage(object):
    
    def __init__(self, config,dirname,template_env):
        data = config
        self.template_env = template_env
        self.position = data['position']
        self.dirname = dirname
        self.filename = '%s.png'%str(uuid.uuid4())
        self.fullPath = os.path.join(self.dirname,self.filename)
        self.template = "wms"
        self.caption = self.conditionalAdd(data['caption'])
        self.text = self.conditionalAdd(data['text'])
        self.size = data['size']
        if self.size == "custom":
            self.height = data['height']
            self.width = data['width']
        elif self.size == "small":
            self.height = 300
            self.width = 300
        elif self.size == "medium":
            self.height = 450
            self.width = 450
        elif self.size == "large":
            self.height = 600
            self.width = 600

        self.source = data['source']

    def generate(self):
        
        #self.source['lon'].extend(self.source['lat'])
        #print('-'*30)
        #print(self.source['lon'])
        wms = WebMapService(self.source['serverUrl'], version=self.source['serverVersion'])
        img = wms.getmap(   layers=[self.source['layer']],
                     styles=[self.source['palette']],
                     srs='EPSG:4326',
                     bbox = (self.source['lon'][0],self.source['lat'][0],self.source['lon'][1],self.source['lat'][1]),
                     size=(600, 600),
                     format='image/png',
                     transparent=False,
                     time = self.source['time'],
                     logscale = True
                     )
        out = open(self.fullPath, 'wb')
        out.write(img.read())
        out.close()
        #print(img.geturl())
        return self.fullPath

    def render(self):
        return self.template_env.get_template('image.html').render(data=self)
    
    def conditionalAdd(self,item):
        if item is "null":
            return None
        return item




    

if __name__ == '__main__':
    with open('wms_test.json') as json_data_file:
        data = json.load(json_data_file)
        print(data)
        a = wmsImage(data)
        a.generate()