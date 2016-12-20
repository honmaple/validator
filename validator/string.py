#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: string.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-20 21:29:17 (CST)
# Last Update:星期二 2016-12-20 21:32:28 (CST)
#          By:
# Description:
# **************************************************************************
from .base import Validator


class ValidatorRequire(Validator):
    error = 'data is required'

    def __call__(self, value):
        if not value:
            return False
        return True


class ValidatorLength(Validator):
    error = 'length error'

    def __call__(self, value):
        min = self.kwargs.get('min')
        max = self.kwargs.get('max')
        length = self.kwargs.get('length')
        if min is not None and max is not None:
            assert min <= max
        v_length = len(value)
        if v_length is not None and v_length != length:
            return False
        if min is not None and v_length < min:
            return False
        if max is not None and v_length > max:
            return False
        return True



class ValidatorPhoneCaptcha(Validator):
    error = 'phone captcha is error'

    def __call__(self, value):
        redis_value = 's'
        if value != redis_value:
            return False
        return True


class ValidatorPictureCaptcha(Validator):
    error = 'picture captcha is error'

    def __call__(self, value):
        redis_value = 's'
        if value != redis_value:
            return False
        return True
