import logging
import os
import datetime

class Log(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # 动态文件名设置
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir, 'logs')
        log_file = datetime.datetime.now().strftime('%Y-%m-%d') + '.log'
        file_name = log_dir + '/' + log_file
        print(file_name)

        # 文件输出日志
        self.file_handle = logging.FileHandler(file_name)
        # 日志格式设置
        formatter = logging.Formatter('%(asctime)s  %(filename)s  %(funcName)s -----%(levelno)s  %(levelname)s -------> %(message)s ')
        self.file_handle.setFormatter(formatter)
        # 将格式赋给logger
        self.logger.addHandler(self.file_handle)
        # 设置日志级别
        self.logger.setLevel(logging.INFO)

    def get_log(self):
        return self.logger

    def close_hadle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()

if __name__ == '__main__':
    log =Log()
    log.get_log().debug('hello world !')
    log.close_hadle()
