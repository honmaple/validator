#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: regex.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-20 21:29:52 (CST)
# Last Update:星期五 2016-12-23 17:16:7 (CST)
#          By:
# Description:
# **************************************************************************
from .base import Validator
from re import compile


class ValidatorRegex(Validator):
    regex = ''

    def __call__(self, value):
        self.value = value
        regex = self.kwargs.get('regex')
        if regex is not None:
            self.regex = regex
        pattern = compile(self.regex)
        if not pattern.match(value):
            return False
        return True


class ValidatorEmail(ValidatorRegex):
    regex = r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$'
    callback = 'email format error'


class ValidatorUrl(ValidatorRegex):
    regex = r'^[a-z]+://(?P<host>[^/:]+)(?P<port>:[0-9]+)?(?P<path>\/.*)?$'
    callback = 'url format error'


class ValidatorPhone(ValidatorRegex):
    regex = r'^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$'
    callback = 'phone format error'

