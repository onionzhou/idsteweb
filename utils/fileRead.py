import yaml
import os
import xlrd
class YamlRead():
    def __init__(self,yaml_file):
        if os.path.exists(yaml_file):
            self.yaml_file= yaml_file
        else:
            raise FileNotFoundError('file is not exist')
        self._data =None

    def data(self):
        if not self._data:
            with open(self.yaml_file,'rb') as f:
               self._data = list(yaml.safe_load_all(f))
        return  self._data

class ExcelRead():
    '''read excel file
        return list
        | A| B| C|
        |a1|b1|c1|
        |a2|b2|c2|
        '''
    def __init__(self,execlfile,sheet,title_line):
        if os.path.exists(execlfile):
            self.execl =execlfile
        else:
            raise FileNotFoundError('file is not exist')
        self.sheet =sheet
        self.title_line = title_line
        self._data = list()


