import uuid
import os

class fileImage(object):
    
    def __init__(self, config,dirname,template_env):
        print('*'*80)
        data = config
        self.template_env = template_env
        self.position = data['position']
        self.dirname = dirname
       
        self.caption = self.conditionalAdd(data['caption'])
        self.text = self.conditionalAdd(data['text'])
        self.size = data['size']
        if self.size == "custom":
            self.height = data['height']
            self.width = data['width']
        elif self.size == "small":
            self.width = 300
        elif self.size == "medium":
            self.width = 450
        elif self.size == "large":
            self.width = 600
        self.source = data['source']
        self.fullPath = self.source['filepath']
    def generate(self):
        pass
    
    def render(self):
        return self.template_env.get_template('image.html').render(data=self)
    
    def conditionalAdd(self,item):
        if item is "null":
            return None
        return item

