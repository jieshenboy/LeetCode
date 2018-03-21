#-*- coding: utf-8 -*-

def print99():
    """
    打印99乘法口诀表
    :return:
    """
    for i in range(1,10):
        for j in range(1, i+1):
            print('%dX%d=%2s  ' %(j,i,i*j))
        print('\n')
print99()
