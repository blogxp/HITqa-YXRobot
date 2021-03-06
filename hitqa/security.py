# -*- coding: utf-8 -*-
'''
@author: xinghuazhang
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: xing_hua_zhang@126.com
@software: PyCharm 2017.1.4
@file: security.py
@time: 2017/8/27 22:04
@desc: Python简单密码加密程序
       随机生成4位salt，与原始密码组合，通过md5加密
'''
from random import Random
from hashlib import md5

# 获取由4位随机大小写字母、数字组成的salt值
def create_salt(length=4):
    salt = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    len_chars = len(chars) - 1
    random = Random()
    for i in xrange(length):
        # 每次从chars中随机取一位
        salt += chars[random.randint(0, len_chars)]
    return salt

# 获取原始密码+salt的md5值
def create_md5(pwd, salt):
    md5_obj = md5()
    md5_obj.update(pwd + salt)
    return md5_obj.hexdigest()

