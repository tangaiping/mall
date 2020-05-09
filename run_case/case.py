from utils.read_excel import Excel
from key_word.action_method import ActionMethod
import HTMLTestRunner
from log.log import Log
import os

logger = Log()
log = logger.get_log()


class KeywordCase(object):
    def __init__(self):
        self.action_method = ActionMethod()

    def run_case(self):
        file_path = os.path.dirname(os.path.abspath(os.getcwd())) + '/config/' + 'keywords.xls'
        handle_excel = Excel(file_path)
        case_lines = handle_excel.get_lines()
        log.info('读取case文件成功！')
        logger.close_hadle()

        if case_lines:
            for i in range(1, case_lines):
                is_run = handle_excel.get_col_value(i, 3)
                if is_run == 'yes':                                            # 判断case是否执行
                    get_method = handle_excel.get_col_value(i, 4)              # 拿到执行方法
                    send_value = handle_excel.get_col_value(i, 5)              # 拿到输入的数据
                    handle_value = handle_excel.get_col_value(i, 6)            # 拿到要处理的操作元素
                    except_result_method = handle_excel.get_col_value(i, 7)    # 拿到预期结果的方法
                    except_result = handle_excel.get_col_value(i, 8)           # 拿到预期结果值
                    self.run_method(get_method, send_value, handle_value)
                    if except_result != '':
                        except_value = self.get_except_result_value(except_result)
                        if except_value[0] == 'text':
                            result = self.run_method(except_result_method)
                            if except_value[1] in result:
                                handle_excel.write_value(i, 'pass')
                            else:
                                handle_excel.write_value(i, 'fail')
                        elif except_value[0] == 'element':
                            result = self.run_method(except_result_method, except_value[1] )
                            if result:
                                handle_excel.write_value(i, 'pass')
                            else:
                                handle_excel.write_value(i, 'fail')
                        else:
                            print('其他预期结果值')
                    else:
                        print('预期结果为空')

    # 把预期结果值以=切分
    def get_except_result_value(self, data):
        return data.split('=')

    def run_method(self, get_method, send_value='', handle_value=''):
        # 选择函数 + 选择参数
        method_value = getattr(self.action_method, get_method)    # 选择函数
        if send_value == '' and handle_value != '':                # 选择传参
            result = method_value(handle_value)
        elif send_value == '' and handle_value == '':
            result = method_value()
        elif send_value != '' and handle_value == '':
            result = method_value(send_value)
        else:
            result = method_value(send_value, handle_value)
        return result

if __name__ == '__main__':
    case = KeywordCase()
    # HTMLTestRunner好像只适用于unittest框架？？？
    # file_path = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())) + '/report/' + 'result.html')
    # report = open(file_path, 'w', encoding='utf-8')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=report, title='第1份报告', description='登录模块', verbosity=2)
    # runner.run()
    case.run_case()