import yaml
import os

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