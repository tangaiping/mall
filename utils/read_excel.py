import os
import xlrd
from xlutils.copy import copy

class Excel(object):
    def __init__(self, excel_path=None, index=None):
        # 设置默认值
        if excel_path == None:
            self.excel_path = os.path.dirname(os.path.abspath(os.getcwd())) + '/config/' + 'keywords.xls'
            print(excel_path)
        else:
            self.excel_path = excel_path
        if index == None:
           self.index = 0
        else:
            self.index = index
        self.data = xlrd.open_workbook(self.excel_path)        # 打开Excel
        self.table = self.data.sheets()[self.index]            # 获取工作列表中所有行的所有字段列表

    # 获取行数
    def get_lines(self):
        rows = self.table.nrows        # 获取行数
        if rows >= 1:
            return rows
        return None

    # 获取单元格数据
    def get_col_value(self, row, col):
        if self.get_lines() > row:
            data = self.table.cell(row, col).value   # 获取单元格的值
            return data

    # 获取整行的值并写进result列表
    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows != None:
            for i in range(rows):
                data = self.table.row_values(i)
                result.append(data)
            return result
        return None

    # 写入数据
    def write_value(self, row, value):
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row, 9, value)
        write_data.save(self.excel_path)

if __name__ == '__main__':
    ex = Excel()
    print(ex.get_col_value(3, 4))
    print(ex.get_data())