# def test1():
#     '''test1...'''
#     print('test1')
#
# def test2():
#     '''test2...'''
#     print('test2')
#
# print (test1.__name__)
# print (test1.__doc__)
#
# print (test2.__name__)
# print (test2.__doc__)



#
# from functools import wraps
#
# def login_required(func):
#     def wrapper(*args,**kwargs):
#         print("Hello")
#         func(*args,**kwargs)
#     return wrapper
#
# @login_required
# def test1():
#     '''test1...'''
#     print('test1')
#
# @login_required
# def test2():
#     '''test2...'''
#     print('test2')
#
# test1()
# test2()
#
# print (test1.__name__)
# print (test1.__doc__)
#
# print (test2.__name__)
# print (test2.__doc__)



#
# from functools import wraps
#
# def login_required(view_func):
#     @wraps(view_func)
#     def wrapper(*args,**kwargs):
#         pass
#     return wrapper
#
# @login_required
# def test1():
#     '''test1...'''
#     print('test1')
#
# @login_required
# def test2():
#     '''test2...'''
#     print('test2')
#
# print (test1.__name__)
# print (test1.__doc__)
#
# print (test2.__name__)
# print (test2.__doc__)
from functools import wraps
def ss(text):
    def derector(func):
        @wraps(func)
        def wraspper(*args,**kwargs):
            print("text")
            func(*args,**kwargs)
        return wraspper
    return derector

@ss("sm")
def test1():
    print("hello")

test1()
print(test1.__name__)