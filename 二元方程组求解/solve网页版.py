#coding=utf-8
from sympy import *
import re
from bottle import *

def subZ(z):
    z=z.replace("X", "x")
    z=z.replace("Y", "y")
    z=z.replace("[","(")
    z=z.replace("]",")")
    z = re.sub(r'([\d\.]+)([xy(])', r'\1*\2', z)
    return z.replace("=", "-(" ) + ")"

def sol1(z):
    zz=subZ(z)
    x=Symbol('x')
    return solve(zz,x)

def sol2(z1,z2):
    zz1=subZ(z1)
    zz2=subZ(z2)
    x=Symbol('x')
    y=Symbol('y')
    return solve([zz1,zz2],[x,y])
#decorator
def allow_cross_domain(fn):
    def _enable_cors(*args, **kwargs):
        #set cross headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,OPTIONS'
        allow_headers = 'Referer, Accept, Origin, User-Agent'
        response.headers['Access-Control-Allow-Headers'] = allow_headers     
        if request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)    
    return _enable_cors

#@route('/solve')
@get('/solve')
@allow_cross_domain
def login_form():
    return '''please visit < a href=" ">http://m.wulehao.com</ a>'''
#@route('/login', method = 'POST')

@post('/solve')
@allow_cross_domain
def login():
    d1 = request.forms.get('d1')
    d2 = request.forms.get('d2')
    if d2:
        return "计算结果"+str(sol2(d1,d2))
    else:
        return "计算结果"+str(sol1(d1))

run(host='192.168.50.51', port=8000)

'''j=input("一元一次方程还是二元一次方程？输入1或者2并回车，输入其他退出程序：")
if j == "1" :

elif j == "2" :
    print("请输入一个含有未知数x,y的二元一次方程组（例如 x+2y=5  x-2y=1 返回结果{x: 3, y: 1}")
    print("如果需要计算小数结果，请在数值后面输入.0，(例如2x+1/3=1.0 返回结果为[0.333333333333333])")
    z1=input("请输入第一个等式：")        
    zz1=subZ(z1)
    z2=input("请输入第二个等式：")
    zz2=subZ(z2)
    x=Symbol('x')
    y=Symbol('y')
    print(solve([zz1,zz2],[x,y]))'''
