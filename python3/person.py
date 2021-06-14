#!/usr/bin/python3
# -*- coding: utf-8 -*-

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')


# print('for x in [1, 2, 3, 4, 5]:')
# for x in [1, 2, 3, 4, 5]:
#  #   print(x)

# print('for x in iter([1, 2, 3, 4, 5]):')
#for x in iter([1, 2, 3, 4, 5]):
 #   print(x)

L  =  [ x * x for x in range(10) ]
print(L)

g = (x * x for x in range(10))
print(g)
for n in g:
    print(n)