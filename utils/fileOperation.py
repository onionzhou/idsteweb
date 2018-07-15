import yaml
import os
import xlrd,xlwt
from xlutils.copy import copy
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
                data_sheet = file.sheet_by_index(self.sheet)
            else:
                data_sheet = file.sheet_by_name(self.sheet)
        if self.title_line:
            title = data_sheet.row_values(0) #title  return list
            for row in range(1,data_sheet.nrows):
                templist =[]
                for col in range(data_sheet.ncols):
                    if data_sheet.cell_type(row,col) == 2:
                        templist.append(int(data_sheet.cell_value(row,col)))
                        #self._data.append(dict(zip(title, int(data_sheet.cell_type(row,col)))))
                    else:
                        templist.append(data_sheet.cell_value(row, col))
                self._data.append(dict(zip(title,templist)))
                #print(templist)
            #for col in range(1,data_sheet.nrows):
            #self._data.append(dict(zip(title, data_sheet.row_values(col))))
        else:
            for row in range(1,data_sheet.nrows):
                templist = []
                for col in range(data_sheet.ncols):
                    if data_sheet.cell_type(row,col) == 2 : # 2  is number
                        templist.append(int(data_sheet.cell_value(row,col)))
                    else:
                        templist.append(data_sheet.cell_value(row,col))
                self._data.append(templist)
                 #self._data.append(data_sheet.row_values(col))
        return self._data

row0 =['User_Desc','User_Sn','IcCard','User_Type','User_Expiry','Phone',
           'IC_Status','Dpm_Name','User_Name','New_Pass_Word','Priority',
           'privilege','usbkey',
           ]
class ExcelWriteError():
    pass
class ExcelWrite():
    '''
    write excel file (.xls)
    row0 title
    row1  data
    -----------------------------------------
    name     user_name  password   phone
     xiao    test1      test1       13982000043
     tesr2   est2       test2      13982000044
     -----------------------------------------
    '''
    def __init__(self,execlfile,sheet_name='sheet0'):

        if execlfile != None:
            self.excelfile = execlfile
        else:
            raise ExcelWriteError('execlfile is not name ')
        #if row_data != None:
        #    self._row_data = row_data
        #else:
        #    raise ExcelWriteError('row_data is null!')
        #if column_len != None:
        #    self._col_data_len =column_len
        #else:
        #    raise ExcelWriteError('colum_data is null!')

        if  os.path.exists(execlfile):
            self.file = copy(xlrd.open_workbook(execlfile))
            self.sheet=self.file.get_sheet(sheet_name)
        else:
            self.file = xlwt.Workbook(encoding='utf-8')
            self.sheet =self.file.add_sheet(sheet_name,cell_overwrite_ok=True)
    '''
    一行一行的插入数据
    :row_num  写几行
    :from_row_num 从第几行写
    '''
    def write(self,row,col,data):
        self.sheet.write(row,col,data)
            #print('c == '+ str(c) + 'r ==' +str(r) + 'row_data[r]' + str(row_data[r]))

    def save(self):
        self.file.save(self.excelfile)

class CsvRead():
    pass


if __name__ == '__main__':
    e = 'F:\my_work\idsteweb\data\\userdata.xlsx'

    file =ExcelRead(e,title_line=True).data()
    print(file)




