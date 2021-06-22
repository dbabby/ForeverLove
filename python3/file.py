#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
# f = open('/Users/abbydb/dbabby/ForeverLove/python3/Readme.txt', 'r')

# print(f.read());
# f.close();     # need close


# with open('/Users/abbydb/dbabby/ForeverLove/python3/Readme.txt', 'r')  as f:
#      print(f.read());

# print(os.name)
# print(os.uname())

# #split path and filename
# print(os.path.split('/Users/abbydb/dbabby/ForeverLove/python3/Readme.txt',))

# print(os.path.splitext('/Users/abbydb/dbabby/ForeverLove/python3/Readme.txt',))

#print all files in  .
#[x for x in os.listdir('.') if os.path.isdir(x)]

for x in os.listdir('.'):
    if os.path.isdir(x):
        print(x)


for x in os.listdir('.'):
    if os.path.isfile(x) and  os.path.splitext(x)[1]=='.py':
        print(x)

# # 查看当前目录的绝对路径:
# os.path.abspath('.')
# # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# os.path.join('/Users/michael', 'testdir')
# # 然后创建一个目录:
# os.mkdir('/Users/michael/testdir')
# # 删掉一个目录:
# os.rmdir('/Users/michael/testdir')
