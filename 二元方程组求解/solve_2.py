from sympy import *
import re
#coding=utf-8



import ctypes,sys
 
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12
 
# 字体颜色定义 ,关键在于颜色编码，由2位十六进制组成，分别取0~f，前一位指的是背景色，后一位指的是字体色
#由于该函数的限制，应该是只有这16种，可以前景色与背景色组合。也可以几种颜色通过或运算组合，组合后还是在这16种颜色中
 
# Windows CMD命令行 字体颜色定义 text colors
FOREGROUND_BLACK = 0x00 # black.
FOREGROUND_DARKBLUE = 0x01 # dark blue.
FOREGROUND_DARKGREEN = 0x02 # dark green.
FOREGROUND_DARKSKYBLUE = 0x03 # dark skyblue.
FOREGROUND_DARKRED = 0x04 # dark red.
FOREGROUND_DARKPINK = 0x05 # dark pink.
FOREGROUND_DARKYELLOW = 0x06 # dark yellow.
FOREGROUND_DARKWHITE = 0x07 # dark white.
FOREGROUND_DARKGRAY = 0x08 # dark gray.
FOREGROUND_BLUE = 0x09 # blue.
FOREGROUND_GREEN = 0x0a # green.
FOREGROUND_SKYBLUE = 0x0b # skyblue.
FOREGROUND_RED = 0x0c # red.
FOREGROUND_PINK = 0x0d # pink.
FOREGROUND_YELLOW = 0x0e # yellow.
FOREGROUND_WHITE = 0x0f # white.
 
 
# Windows CMD命令行 背景颜色定义 background colors
BACKGROUND_BLUE = 0x10 # dark blue.
BACKGROUND_GREEN = 0x20 # dark green.
BACKGROUND_DARKSKYBLUE = 0x30 # dark skyblue.
BACKGROUND_DARKRED = 0x40 # dark red.
BACKGROUND_DARKPINK = 0x50 # dark pink.
BACKGROUND_DARKYELLOW = 0x60 # dark yellow.
BACKGROUND_DARKWHITE = 0x70 # dark white.
BACKGROUND_DARKGRAY = 0x80 # dark gray.
BACKGROUND_BLUE = 0x90 # blue.
BACKGROUND_GREEN = 0xa0 # green.
BACKGROUND_SKYBLUE = 0xb0 # skyblue.
BACKGROUND_RED = 0xc0 # red.
BACKGROUND_PINK = 0xd0 # pink.
BACKGROUND_YELLOW = 0xe0 # yellow.
BACKGROUND_WHITE = 0xf0 # white.
 
 
 
# get handle
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
 
def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool
 
#reset white
def resetColor():
    set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)

def printYellow(mess):
    set_cmd_text_color(FOREGROUND_YELLOW)
    sys.stdout.write(mess)
    resetColor()
def printYellowRed(mess):
    set_cmd_text_color(BACKGROUND_GREEN | FOREGROUND_YELLOW)
    sys.stdout.write(mess)
    resetColor()

def subZ(z):
    z=z.replace("X", "x")
    z=z.replace("Y", "y")
    z=z.replace("[","(")
    z=z.replace("]",")")
    z = re.sub(r'([\d\.]+)([xy(])', r'\1*\2', z)
    return z.replace("=", "-(" ) + ")"
printYellowRed("本程序由"+"邬乐"+"出品，用于方程验算 #2406Workshop@2018.12.16\r\n")

while 1:
    j=input("一元一次方程还是二元一次方程？输入1或者2并回车，输入其他退出程序：")
    if j == "1" :
        print("请输入一个含有未知数x的一元一次方程：(例如2x+1/3=1 返回结果为[1/3])")
        print("如果需要计算小数结果，请在数值后面输入.0，(例如2x+1/3=1.0 返回结果为[0.333333333333333])")
        z=input("请输入一个等式：")
        zz=subZ(z)
        x=Symbol('x')
        print(solve(zz,x))
    elif j == "2" :
        print("请输入一个含有未知数x,y的二元一次方程组（例如 x+2y=5  x-2y=1 返回结果{x: 3, y: 1}")
        print("如果需要计算小数结果，请在数值后面输入.0，(例如2x+1/3=1.0 返回结果为[0.333333333333333])")
        z1=input("请输入第一个等式：")        
        zz1=subZ(z1)
        z2=input("请输入第二个等式：")
        zz2=subZ(z2)
        x=Symbol('x')
        y=Symbol('y')
        print(solve([zz1,zz2],[x,y]))
    else :
        break