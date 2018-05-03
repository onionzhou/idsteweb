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
class SheetTypeError():
    pass
class ExcelRead():
    '''read excel file
        return list
        | A| B| C|
        |a1|b1|c1|
        |a2|b2|c2|

     print(ExcelReader(excel, title_line=True).data) output:
    [{A: A1, B: B1, C:C1}, {A:A2, B:B2, C:C2}]
    print(ExcelReader(excel, title_line=False).data) output
    [[A,B,C], [A1,B1,C1], [A2,B2,C2]]
     sheet  Specify search by index or name
        '''
    def __init__(self,execlfile,sheet=0,title_line=False):
        if os.path.exists(execlfile):
            self.execl =execlfile
        else:
            raise FileNotFoundError('file is not exist')
        self.sheet =sheet
        self.title_line = title_line
        self._data = list()
    def data(self):
        if not self._data:
            file = xlrd.open_workbook(self.execl)
            if type(self.sheet) not in [int,str]:
                raise SheetTypeError('sheet only support type(int) or type(str)')
            elif type(self.sheet) == int:
                sheetfile = file.sheet_by_index(self.sheet)
            else:
                sheetfile = file.sheet_by_name(self.sheet)
        if self.title_line:
            title = sheetfile.row_values(0) #title  return list
            for i in range(1,sheetfile.nrows):
                self._data.append(dict(zip(title,sheetfile.row_values(i))))
        else:
            for i in range(1,sheetfile.nrows):
                self._data.append(sheetfile.row_values(i))
        return self._data

class CsvRead():
    pass

def test():
    e= 'F:\python\idsteweb\data\\testdata.xlsx'
    file = xlrd.open_workbook(e)
    #file.sheet_by_index()
    sheetfile = file.sheet_by_name('Sheet1')
    title = sheetfile.row_values(0)
    data =[]
    for i in range(1,sheetfile.nrows):
        file =dict(zip(title,sheetfile.row_values(i)))
        data.append(file)
    print(data)

    '''for sheet in file.sheets():
        print(sheet.name)
    for i in range(sheetfile.nrows): #所有行 sheetfile.nrows
        row = sheetfile.row_values(i) # 打印每行的值
        print(row)
        for cell in row:
            print(cell) #打印每个表格的值
    print(sheetfile.row_values(0))
    '''
if __name__ == '__main__':
    e = 'F:\python\idsteweb\data\\testdata.xlsx'
    file =ExcelRead(e,title_line=True).data()
    print(file)
    print(int(file[0]['phone']))



