import re
import argparse

# 所有设定错误的集合
errors = {
    '101': 'error:101: Word must be completely letters.',
}

# define new exception
class UnSupport(Exception):
    pass

class InputError(Exception):
    pass

# Input check


def Input_check(word):

    error_code = None

    # 判断错误类型
    if re.search(r'\d|\W', word)!=None:
        error_code = '101'
    
    # 打印错误信息
    if error_code != None:
        raise InputError(errors[error_code])

if __name__ == '__main__':
    word = input(':')
    Input_check(word)
