#!/usr/bin/env python3
file_string = '''python函数知识要点：

定义函数 def
文档字符串 docstring
    - 模块开始处
    - 函数名之后
    - 可以给变量赋值
符号表：
    - 局部，外层，全局
    - nonlocal, global
    - vars(), locals(), globals()
参数：
    - 值传递，引用传递
概念：函数名、函数对象、函数变量
    f = fib
    f100 = fib(100)
返回值:
    - 无返回值时，为None
函数参数的使用：
    - 定义时、调用时
函数参数：
    - 型参 formal parameter / argument
    - 参数默认值
    - 默认值可以使用变量，但只求值一次
    - 关键字参数 keyword argument
        也叫做 named parameter
    - 位置参数 positional argument
    - 必选/可选参数：required / optional
    - 关键字参数必须在位置参数后面
    - 调用时：参数不能多于函数要求
    - 调用时：参数不能重复赋值
参数收集：*arg形参与**arg 形参
    - *arg 必须在 **name前
    - *arg 接收一个元组，包含形参列表之外的*位置*参数
    - **arg 接收一个字典，包含与函数中已定义形参对应之外的所有*关键字*参数
    - *arg 和 **arg 可一同时使用， * 在 ** 前
    - 关键字参数在输出结果中的顺序与调用函数时的顺序一致
    - 使用 * 处理任意多的参数：
       *arg后可以有关键字参数
       def concat(*args, sep="/"):
           return sep.join(args)
参数分隔 / 和 * 【特殊写法】
    - 格式：def foo(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    - 将参数类型分开：
      / 前为 仅限位置参数
      / * 之间为位置或关键字参数
      * 之后为关键字参数
    【错误写法】避免特征的情况发生：
        def foo(name, **kwds):
          return 'name' in kwds
        在这个函数被调用时，无法使用 foo('Alice', name='Kite')
        这样的形式，否则产生重复赋值的错误
        也无法使用 foo(1, **{'name': 2})，重复赋值
    【特殊写法】所以需要书写为：
        def foo(name, /, **kwds):
          return 'name' in kwds
    - 可以这样调用：foo(1, **{'name': 2})
        或这样调用 foo(a, name=2)
解包实参列表
    - 函数调用时
    - 使用 * 解包列表或元组
        args = [3, 6]
        list(range(*args)) 
    - 使用 ** 解包字典
lambda表达式
    - 普通写法：lambda a, b: a+b，返回两个数的和
    - 用于任何需要函数调用的地方
    - 只能是单个表达式
    - 语法糖
    - 可以引用包含在作用域中的变量
    【特殊写法】
      返回一个lambda函数
        def make_incrementor(n):
        return lambda x: x + n
      把匿名函数作为参数传递：
        pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
        pairs.sort(key=lambda pair: pair[1])
        pairs
        [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

'''
def increment(n):
    return lambda x: x + n

def test_increment():
    f = increment(10)
    print(f(1))
    print(f(2))

def small_talk(greet, name='', chat=''):
    '''首先打印greet, 循环打印name: , 逐条打印chat'''
    print(greet)
    #print('name:', name)
    #print('chat:', chat)
    #return
    n = len(name)
    m = 0
    c = chat
    for i in c:
        if m == n: m = 0
        print(name[m], ':', end = ' ')
        m += 1
        print(i)

def test_small_talk():
    greet = 'Time is 4pm'
    name = ['Me', 'Alice']
    chat = ['Can you tell me a story?',
            'OK',
            '',
            'Here is one',
            ]
    small_talk(greet, name, chat)

a_number = 10
def print_int(i = a_number):
    ''' 此处函数默认值等于一个全局变量，
    该默认值只赋值一次，当全局变量变化后，
    函数默认值仍保持不变'''
    print(i)
def test_print_int():
    print('function default argument value: 20')
    print_int()
    print('change default var: 20')
    a_number = 20
    print_int()

a_list = [1, 2]
def print_list(i = a_list):
    ''' 函数默认值为可变类型
    此处函数默认值等于一个全局变量，
    该全局变量为可变类型list,
    默认值赋值为该变量的引用，
    当全局变量变化后，函数默认值随之改变'''
    print(i)

def test_print_list():
    print('a_list = [1, 2]')
    print_list()
    print('append 100 to the list:')
    a_list.append(100)
    print_list()

def share_list_arg(i, arg=[]):
    '''特殊写法：
    函数参数默认值为空列表，
    当该列表的值改变后，所有函数调用，该参数默认值都改变。
    可理解为：编译器创建了一个匿名变量，将引用赋值给参数
    若避免该情况，需 arg=None
    然后在函数内部 arg=[]
    
    '''
    arg.append(i)
    return arg

def test_share_list_arg():
    print('Function share an argument:')
    print(share_list_arg(100))
    print(share_list_arg('share'))
    print(share_list_arg(222))
    print(share_list_arg(None))

def dont_share_list_arg(i, arg=None):
    '''特殊写法：
    避免函数参数共享可变类型：
    若避免该情况，需 arg=None
    然后在函数内部 arg=[]
    
    '''
    arg=[]
    arg.append(i)
    return arg
def test_dont_share_list_arg():
    print('Function dont share an argument:')
    print(dont_share_list_arg(100))
    print(dont_share_list_arg('share'))

def feb_prn(max):
    '''打印斐波那契数列'''
    a, b = 0, 1
    print('不大于', max, '的斐波那契数列:', sep='')
    while a <= max:
        print(a, end=', ')
        a, b = b, a+b
    print('')

def feb(count=0, limit=0, start=0):
    ''' 返回斐波那契数列, 列表。
        列表从0，1开始
        count: 数列元素个数
        limit: 不超过最大值
        start: 开始值
        无参数时返回空列表
    '''
    # print('count:', count, "limit:", limit)
    # 处理参数特殊情况
    if (count<=0 and limit<=0):
        return []
    a, b = start, start+1
    result = [start]
    i = 1       # 已经添加了一个值，计数从1开始
    while True:
        a, b = b, a + b
        if count!=0 and i>=count:
            break
        if limit!=0 and a>limit:
            break
        result.append(a)
        i += 1
    return result

def test_feb():
    print("feb(0):", feb(0))
    print("feb(1):", feb(1))
    print("feb(2):", feb(2))
    print("feb(5):", feb(5))
    print("feb(limit=30):", feb(limit=30))
    print("feb(count=3, limit=1000):", feb(count=3, limit=1000))
    print("feb(count=10, limit=30):", feb(count=10, limit=30))
    print("feb(count=5, start=1000):", feb(count=5, start=1000))

def test_feb_prn():
    feb_prn(1)
    feb_prn(20)

def test_ref_func():
    '''函数名和函数对象:
        * 定义一个变量，引用另一个函数对象
        * 定义一个变量，引用函数对象，附带变量列表
    '''
    f = feb_prn
    f(30)
    f50 = f(50)
    
def no_return(i):
    ''' 函数返回值默认返回None，即使没有return'''
    i += 1

def test_no_return():
    print(no_return(1))

if __name__ == '__main__':
    def demo():
        print(file_string)
        test_feb_prn()
        test_no_return()
        test_ref_func()
        test_print_int()
        test_feb()
        test_print_list()
        test_share_list_arg()
        test_dont_share_list_arg()
        test_small_talk()
        test_increment()
    print(file_string)
    demo()

    
