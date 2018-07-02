from bs4 import BeautifulSoup
import requests
import re
import argparse as ap
import argument
from error_handler import *

# 命令行输入
args = argument.get_argument()

# 检查异常
Input_check(args.word)

class youdao_dict(object):
    def __init__(self, word, deepth=5):
        self.deepth = deepth
        self.word = word
        url = requests.get(
            'http://www.youdao.com/w/eng/{}/#keyfrom=dict2.index'.format(word))
        self.soup = BeautifulSoup(url.text, 'lxml')

    def website_capture(self):
        self.translation = self.soup.find(
            name='div', attrs={'class': 'trans-container'})
        self.wordgroup = self.soup.find_all(
            name='p', attrs={'class': 'wordGroup'})
        self.example = self.soup.find(
            name='div', attrs={'id': 'examplesToggle'})

    def display(self):
        count = 0
        print('=============\n'+self.word+'\n=============')
        # 打印所有中文释义
        print('{}'.format(self.translation.ul.get_text()), end='\r')
        print('-----------------------------------------------')
        # 打印前n个词组
        print('词组:')
        for i in self.wordgroup:
            wordgroup = i.a.get_text()
            meaning = re.sub(r'[a-zA-Z]*(\s)', '', i.get_text())
            print('{0:25}'.format(wordgroup), '|', meaning)
            count += 1
            if count >= self.deepth:
                count = 0
                break
        print('-----------------------------------------------')
        # 打印前n个例句
        print('例句:')
        example_div = self.example.ul.find_all(name='li')
        for i in example_div:
            example = re.sub(
                r'[0-9a-z]*.[0-9a-z]*.com|《[\u4e00-\u9fa5]*》', '', i.get_text())
            example = re.sub(r'\n', '', example, 3)
            example = example.replace('\n', '/', 1)
            example = re.sub(r'\n', '', example)
            example = re.split('/', example)
            print('| ', example[0]+'\n'+example[1])

def main():
    a = youdao_dict((args.word),(args.deepth))
    a.website_capture()
    a.display()

if __name__ == '__main__':
    main()