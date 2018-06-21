import uuid
import os
import json
from jinja2 import Template
from jinja2 import Environment, PackageLoader, select_autoescape
import pdfkit



from image_generators import renderers

def main():
    dirname = str(uuid.uuid4())
    os.mkdir(dirname)
    env = Environment(
        loader=PackageLoader('report_gen', 'templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    
    with open("config.json") as config_file:
        with open("index.html","w") as output:
            
            data = json.load(config_file)['report']
            write_header(data,output,env)
            for item in data['items']:
                if item['type'] == "image":
                    try:
                        a = renderers[item['sourceType']](item,dirname,env)
                        a.generate()
                        output.write(a.render())
                    except:
                        pass
            write_footer(data['footer'],output,env)
            pdfkit.from_file("./index.html", 'webpage.pdf')


    # with open('wms_test.json') as json_data_file:
    #     data = json.load(json_data_file)
    #     #print(data)
    #     a = wmsImage(data,dirname,env)
    #     imgpath = a.generate()
    # #print("generated image @ %s" % imgpath)
    #     print(a.render())


def write_header(data,output,env):
    output.write(env.get_template('header.html').render(data=data))


def write_footer(data,output,env):
    output.write(env.get_template('footer.html').render(data=data))


if __name__ == '__main__':
    main()