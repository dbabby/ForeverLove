#!/usr/bin/python3
# -*- coding: utf-8 -*-

# JSON类型  Python类型
# {}                  dict
# []                  list
# "string"        str
# 1234.56         int或float
# true/false      True/False
# null                None

import json

d = dict(name='Bob', age=20, score=88)

print(json.dumps(d))


json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))