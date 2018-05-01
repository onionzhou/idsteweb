import os
from utils.fileRead import YamlRead

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH,'config','config.yaml')
DATA_PATH = os.path.join(BASE_PATH,'data')
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')

class config():
    def __init__(self,config=CONFIG_FILE):
        self.config = YamlRead(config).data()

    def get (self,element,index = 0):
        return self.config[index].get(element)

if __name__ == '__main__':
    print(DATA_PATH)
    url = config().get('TEST4')
    print(url)
    print(DRIVER_PATH +'\cc')

