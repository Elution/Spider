# 1）要求将所有级别的所有日志都写入磁盘文件中
# 2）all.log文件中记录所有的日志信息，日志格式为：日期和时间 - 日志级别 - 日志信息
# 3）error.log文件中单独记录error及以上级别的日志信息，日志格式为：日期和时间 - 日志级别 - 文件名[:行号] - 日志信息
# 4）要求all.log在每天凌晨进行日志切割

# import logging
# from logging import handlers
# import datetime
#
#
# class selfFilter(logging.Filter):
#     def filter(self, record):
#         return "message" not in record.getMessage()
#
#
# logger = logging.getLogger("run")
#
# file2 = logging.FileHandler(filename="error.log")
# file2.setLevel(logging.ERROR)
#
# file1 = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
# file1.setLevel(logging.DEBUG)
#
# fmt1 = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
# file1.setFormatter(fmt1)
#
# fmt2 = logging.Formatter("%(asctime)s - %(levelname)s -%(filename)s[:%(lineno)d]- %(message)s")
# file2.setFormatter(fmt2)
#
# logger.addHandler(file1)
# logger.addHandler(file2)
# logger.addFilter(selfFilter())
#
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warning message')
# logger.error('error message')
# logger.critical('critical message')

# import  json
# data =[{
#     "name":"yang",
#     "gender":"是",
#     "birthday":"1992-10-18"}
#    ]
# f = open ('data.json','w',encoding="utf-8") 
# json.dump(data,f)

from functools import wraps

def login(args):
    print(args)
    def do(func):
        _name = "alex"
        _password = "123"
        name = input("username:")
        password = input("password:")
        if _name==name and _password==password:
            print("welcome "+ _name + "!")
            @wraps(func)
            def wrapps(*args,**kwargs):
                func(*args,**kwargs)
            return wrapps
        else:
            print("No Loging")
    return do




@login("qq")
def american():
    print("hello american")

def japan():
    print("hello japan")

def beijin():
    print("hello beijing")


american()
print(american.__name__)









