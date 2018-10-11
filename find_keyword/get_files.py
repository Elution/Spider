#!/usr/bin/env python
#coding=utf-8
import os
import os.path as op
import re
class Get_File_By_Method():
    def __init__(self):
        self.path = [r"D:\国家能源集团\shenhua_SH\2-系统开发实施\(3)编码\SHReport2\webapp\SHReport\Frame\jsp",r"D:\国家能源集团\shenhua_SH\2-系统开发实施\(3)编码\SHReport2\src\com\shenhua\shreport\web\servlet"]
        # self.path = r"D:\国家能源集团\shenhua_SH\2-系统开发实施\(3)编码\SHReport2\src\com\shenhua\servlet"
        # self.path = r"C:\Users\shenhua_mabiao\Desktop\apache-tomcat-7.0.82\webapps\SHReport2\SHReport\files\excel\lua"
        self.jsps = []

    def get_file(self,path):
        if op.isfile(path):
            self.jsps.append(path)
        else:
            lds = os.listdir(path)
            for ld in lds:
                self.get_file(path+"\\"+ld)
        return self.jsps

    def get_method(self,method,path):
        for path in self.path:
            jsps = self.get_file(path)
            for jsp in jsps:
                with open(jsp,"r",encoding="utf-8") as f:
                    text = f.read()
                    pattern = re.compile(method)
                    result = re.findall(pattern,text)
                    if len(result)>0:
                        print(len(result))
                        print(jsp)
                        print(result)

a = Get_File_By_Method()
a.get_method("getServletContext",a.path)

# x = "alex12345"
# print(re.search('([a-z]+)([0-9]+)',x).groups())
    # /SHReport/Frame/jsp/data/data.jsp