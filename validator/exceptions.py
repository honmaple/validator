#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: exceptions.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-20 16:32:53 (CST)
# Last Update:星期二 2016-12-20 18:34:22 (CST)
#          By:
# Description:
# **************************************************************************
# from django.core.exceptions import ValidationError
from re import compile


class ValidationError(ValueError):
    def __init__(self, message, key):
        self.message = message
        self.key = key
        super(ValidationError, self).__init__(message)


class Validator(object):
    error = ''

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


class ValidatorRequire(Validator):
    error = 'data is required'

    def __call__(self, value):
        if not value:
            return False
        return True


class ValidatorEmail(Validator):
    regex = r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$'
    error = 'email format error'

    def __call__(self, value):
        pattern = compile(self.regex)
        if not pattern.match(value):
            return False
        return True


class ValidatorUrl(Validator):
    regex = r'^[a-z]+://(?P<host>[^/:]+)(?P<port>:[0-9]+)?(?P<path>\/.*)?$'
    error = 'url format error'

    def __call__(self, value):
        pattern = compile(self.regex)
        if not pattern.match(value):
            return False
        return True


class ValidatorPhone(Validator):
    regex = r'^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$'
    error = 'phone format error'

    def __call__(self, value):
        pattern = compile(self.regex)
        if not pattern.match(value):
            return False
        return True


class ValidatorLength(Validator):
    error = 'length error'

    def __call__(self, value):
        min = self.kwargs.get('min')
        max = self.kwargs.get('max')
        length = len(value)
        if min is not None and length < min:
            return False
        if max is not None and length > max:
            return False
        return True


class ValidatorInteger(Validator):
    def __call__(self, value):
        min = self.kwargs.get('min')
        max = self.kwargs.get('max')
        try:
            value = int(value)
            if min is not None and value < min:
                return False
            if max is not None and value > max:
                return False
        except ValueError:
            return False
        return True


class ValidatorEqual(Validator):
    error = 'equal format'

    def __call__(self, value, n_value):
        if value != n_value:
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


class And(Validator):
    def __init__(self, *args):
        self.args = args

    def __call__(self, value):
        for arg in self.args:
            if not arg(value):
                self.error = arg.error
                return False
        return True


class Or(And):
    def __call__(self, value):
        for arg in self.args:
            if arg(value):
                return True
        self.error = arg.error
        return False


class BaseValidator(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def is_valid(self):
        for k, v in self.kwargs.items():
            if hasattr(self, k):
                if not self.valid(k, v):
                    return False
        return True

    def get_valid(self, k):
        return getattr(self, k)

    def valid(self, k, v):
        validator = self.get_valid(k)
        if isinstance(validator, (list, tuple)):
            for valid in validator:
                if isinstance(valid, ValidatorEqual):
                    if not valid(v,
                                 self.kwargs.get(valid.kwargs.get('target'))):
                        return self.valid_fail(k, valid)
                elif not valid(v):
                    return self.valid_fail(k, valid)
        else:
            if isinstance(validator, ValidatorEqual):
                if not validator(
                        v, self.kwargs.get(validator.kwargs.get('target'))):
                    return self.valid_fail(k, validator)
            elif not validator(v):
                return self.valid_fail(k, validator)
        return True

    def valid_fail(self, k, valid):
        if hasattr(self, k + '_callback'):
            raise ValidationError(getattr(self, k + '_callback'))
        raise ValidationError(valid.error, k)


validate_url = ValidatorUrl()
validate_email = ValidatorEmail()
validate_require = ValidatorRequire()
validate_phone = ValidatorPhone()
validate_equal = ValidatorEqual

import unittest


class UserValidator(BaseValidator):
    username = Or(ValidatorLength(min=4, max=23))
    # password = And(validate_require)
    # email = [validate_require, validate_email]
    # url = validate_url


class T(unittest.TestCase):
    def test_hello(self):
        pass


def test():
    validator = UserValidator(
        username='as',
        password='asdada',
        repassword='asdadass',
        email='xiyang0807@gmail.com')
    try:
        validator.is_valid()
        return 'ok'
    except ValidationError as e:
        if callable(e.message):
            return e.message()
        return e.message + ' ' + e.key


a = test()
print(a)
