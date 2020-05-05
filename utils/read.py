import configparser
import os

class Read(object):
    def __init__(self, file_name=None, part=None):
        self.file_name = file_name
        self.part = part
        # 设置默认值
        if file_name == None:
            file_name = os.path.dirname(os.path.abspath(os.getcwd())) + '/config/' + 'elements.txt'
        if  part == None:
            self.part = 'elements'
        self.cf = self.load(file_name)

    # 加载文件
    def load(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf
    # 获取文件里面的值
    def get_value(self, key):
        data = self.cf.get(self.part, key)
        return data

# if __name__ == '__main__':
#     read = Read()
#     print(read.get_value('tel'))
