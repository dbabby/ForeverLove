#!/usr/bin/python3
# -*- coding: utf-8 -*-

# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'

# lisa = Student('Lisa', 99)
# bart = Student('Bart', 59)
# print(lisa.name, lisa.get_grade())
# print(bart.name, bart.get_grade())            

# bart.age = 8
# print('bart.age: %s'  % bart.age)

# print(lisa.age)
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
print('bart.get_name() =', bart.get_name())
bart.set_score(60)
print('bart.get_score() =', bart.get_score())

print('DO NOT use bart._Student__name:', bart._Student__name)
