#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: base.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-20 16:34:47 (CST)
# Last Update:星期五 2016-12-23 17:17:57 (CST)
#          By:
# Description:
# **************************************************************************
from re import compile


class ValidationError(ValueError):
    def __init__(self, message, key=None):
        self.message = message
        self.key = key
        super(ValidationError, self).__init__(message, key)


class Validator(object):
    callback = ''
    value = ''

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        if 'callback' in kwargs:
            self.callback = kwargs['callback']


class ValidatorEqual(Validator):
    callback = 'equal format'

    def __call__(self, value, new_value):
        self.value = value
        if value != new_value:
            return False
        return True


class ValidatorRequire(Validator):
    callback = 'data is required'

    def __call__(self, value):
        self.value = value
        if not value:
            return False
        return True


class And(Validator):
    def __call__(self, value):
        self.value = value
        for validator in self.args:
            if not self.validation(validator, value):
                self.callback = validator.callback
                return False
        return True

    def validation(self, validator, value):
        if isinstance(validator, (And, Or)):
            v = validator(value)
        elif isinstance(validator, ValidatorEqual):
            target = validator.kwargs['target']
            v = validator(value, self.kwargs[target])
        else:
            v = validator(value)

        return v


class Or(And):
    def __call__(self, value):
        self.value = value
        for validator in reversed(self.args):
            if self.validation(validator, value):
                return True
        self.callback = validator.callback
        return False


class Validation(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def is_valid(self):
        fields = self.Meta.fields
        kwargs = self.kwargs
        for field in fields:
            value = kwargs.get(field, '')
            validator = self.get_validator(field)
            if not self.validation(validator, value):
                raise ValidationError(validator.callback, field)
        return True

    def validation(self, validator, value):
        if isinstance(validator, (And, Or)):
            validator.kwargs = self.kwargs
            v = validator(value)
        elif isinstance(validator, ValidatorEqual):
            target = validator.kwargs['target']
            v = validator(value, self.kwargs[target])
        else:
            v = validator(value)

        return v

    def get_validator(self, field):
        if not hasattr(self, field):
            return ValidatorRequire(callback=field + ' require')
        callback = None
        validator = getattr(self, field)
        if isinstance(validator, dict):
            callback = validator.get('callback')
            validator = validator.get('validator')
        if callback:
            validator.callback = callback
        return validator

    class Meta:
        fields = []


# class Test(VVV):
#     username = ValidatorRequire(callback=lambda: '用户名不能为空')
#     password = {'validator': validate_require, 'callback': 'asdad萨d'}
#     repassword = And(validate_require,
#                      ValidatorEqual(
#                          target='password', callback='两次密码不一致'))
#     captcha = {
#         'validator': And(validate_require, validate_email),
#         'callback': 'asdasdad'
#     }

#     class Meta:
#         fields = ['username', 'password', 'repassword', 'captcha']


# def main():
#     test = Test(username='asda', password='sa', repassword='sa', captcha='sa')
#     try:
#         print(test.is_valid())
#     except ValidationError as e:
#         if callable(e.message):
#             print('sssssssssssssssssss')
#             return e.message()
#         print(e)


# if __name__ == '__main__':
#     main()
