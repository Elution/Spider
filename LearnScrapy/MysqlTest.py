from pymysql import connect,cursors


connection = connect(host="localhost",user="root", password="root",
                 database=None, port=3306, unix_socket=None,
                 charset='utf8',db="tests")

sql = 'create database if not exists tests;'
cursor = connection.cursor()
# cursor.execute(sql)
sql1 = 'create table test (code varchar(20) primary key,name varchar(20) not null);'
sql2 ="create table ceshi (ids int auto_increment primary key,uid varchar(20),name varchar(20),learn varchar(20) );"
# cursor.execute(sql2)
sql3 = "insert into ceshi(uid,name,learn) values('%s','%s','%s')"
data = ("3456789",'雷军','python')
# cursor.execute("set names 'utf8'")
cursor.execute((sql3 % data))
sql4 = "select * from ceshi"
cursor.execute(sql4)
print(cursor.fetchone())
print(cursor.fetchall())
connection.commit()
print(cursor.rowcount)