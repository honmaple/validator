#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: internet.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-20 16:36:38 (CST)
# Last Update:星期二 2016-12-20 16:43:0 (CST)
#          By:
# Description:
# **************************************************************************
from .base import Validator
from .exceptions import ValidateError
from re import compile


class ValidatorEmail(Validator):
    regex = '^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$'

    def __call__(self, value):
        pattern = compile(self.regex)
        if not pattern.match(value):
            raise ValidateError('email format error')


class ValidatorUrl(Validator):
    regex = r'^[a-z]+://(?P<host>[^/:]+)(?P<port>:[0-9]+)?(?P<path>\/.*)?$'

    def __call__(self, value):
        pattern = compile(self.regex)
        if not pattern.match(value):
            raise ValidateError('url format error')
