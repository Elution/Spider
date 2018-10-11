# li = [1,2,3,4,5,6,7,8,8]
# 能组成多少个互不相同且不重复的数字的两位数

# 利用内置函数chr(),ord()以及random模块写一个简单随机4位验证码
# 实现用户输入用户名和密码，当用户名为 seven且密码为123时，显示登陆成功，否则登陆失败，失败时允许重复输入三次
def check(person_in):
    def wrapper(*args,**kwargs):
        print('hellow')
        return person_in
    return wrapper()


@check
def person_in():
    in_name = input("请输入用户名：")
    in_password = input('请输入密码：')
    if in_name == 'seven' and in_password == '123':
        print('登陆成功')
        # break
    else:
        i += 1
        print('用户名或密码错误')

#
# name = 'seven'
# password = '123'
# i = 0
# while True:
#     if i<3:
#         in_name = input("请输入用户名：")
#         in_password = input('请输入密码：')
#         if in_name == name and in_password == password:
#             print('登陆成功')
#             break
#         else:
#             i +=1
#             print('用户名或密码错误')
#     else:
#         print('已达最高输入次数，请稍后再试')
#         break

