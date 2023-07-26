#!/usr/bin/env python3
r'''打印表达式 / 值 / 值类型 / 备注信息
    此处：
    字段列表、宽度值 
    -> 使用‘推导’，生成格式化，列表
    -> 将列表join格式化字符串
    -> print(格式串.format(*字段列表))
'''

#import sys
#sys.path.append('./public')
#sys.path.append('../public') 

import math
from keyword import iskeyword

def prn_list(list_item, row = 4, width = 20):
    try:
        for i in range(0, len(list_item), row):
            for j in range(row):
                #print(f'{s:{w}}'.format(s=list_item[i+j], w=width), end='')
                print(f'{list_item[i+j]:{width}}', end='')
            print()
    except IndexError:
        return
    finally:
        print()

def test_prn_list():
    prn_title('test_prn_list()')
    t = dir(int)
    prn_list(t)
    prn_list(t, 3)
    prn_list(['aaa','bbb','ccc'])
    prn_list('uvwxyz')

def prn_title(s, width=40, frame=''):
    '''打印标题
    在标题外侧添加边框，并居中打印标题
        width: 整数。标题宽度，默认40字符
        frame: 字符串。标题边框
    frame字符串长度可以为1，2，3，或更长
        默认打印边框：'_||‾'
    '''    
    l = len(frame)
    if l == 0:
        frame = '_||‾'
    top = 0
    if l == 1:
        left = right = bottom = 0
    elif l == 2:
        left = right = 1
        bottom = 0
    elif l == 3:
        left = 1
        right = 2
        bottom = 0
    else:
        left = 1
        right = 2
        bottom = 3
    print(frame[top] * width)
    print(frame[left] + s.center(width - 2) + frame[right])
    print(frame[bottom] * width)

def test_prn_title():
    prn_title("test_prn_title()")
    prn_title("test_prn_title()", frame='*|-')
    prn_title("test_prn_title()", 10, frame='*|-')

def prn_express(exp, width=None, title=None):
    '''打印表达式
    格式：表达式，结果，结果类型，注释信息
    参数：
        exp: 列表。表达式列表，格式为:['表达式', '注释信息',...]
        width: 宽度。列表。包含4个宽度值
        title: 标题。列表。包含4个标题字符串

    '''
    if width == None:
        width=[20, 15, 20, 20]
    if title == None:
        title = ['express', 'result', 'result type', 'comment']
    #if exp == None:
    #    exp = []

    fmt_list = ['{:' + str(x) + '}' for x in width]
    fmt = ' ' + ' '.join(fmt_list)
    sep_list = ['|' + '-' * x for x in width]
    sep = ''.join(sep_list)
    print(sep)
    print(fmt.format(*title))
    print(sep)
    for i in range(0, len(exp), 2):
        v = eval(exp[i])
        print(fmt.format(exp[i], 
                         repr(v),
                         repr(type(v)),
                         exp[i + 1]))
# make an alias
print_exp = prn_express

def test_print_exp():
    exp_list = ['3 + 4 - 9 + 4*5', '整数运算结果类型为整数',
        '3.1 + 2 - 3.1' , '浮点数表达式结果为浮点数',
        '17 // 6' , '整数的下整除，结果为整数',
        '343.4 // 4.5' , '浮点数的下整除，结果为浮点数',
        '5.3 % 4.1' , '浮点数求余，结果为浮点数',
        '5 % 4' , '整数求余，结果为整数',
        '2 ** 3' , '整数的幂运算，结果为整数',
        '2 ** 3.0' , '浮点数的幂运算，结果为浮点数',
        '3E1', '科学计数法表示的数字都是浮点数',
        '(3 + 4j)','复数可以看作实部和虚部的加法运算',
        '"-------"' , '--------',
        '"abcde"[3]' , '字符串索引，下标不能超范围',
        '"abcdef"[::]' , '字符串切片',
        '"abcdef"[-12:21]' , '起始和终止位置任意',
        '"abcdef"[21:-42]' , '起始和终止位置任意',
    ]
    print_exp(exp_list)

if __name__ == '__main__':
    print(__doc__)
    def test():
        test_print_exp()
        test_prn_title()
        test_prn_list()
    test()
