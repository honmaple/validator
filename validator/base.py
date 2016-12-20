#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: base.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-20 16:34:47 (CST)
# Last Update:星期二 2016-12-20 21:43:42 (CST)
#          By:
# Description:
# **************************************************************************


class ValidationError(ValueError):
    def __init__(self, message, key=None):
        self.message = message
        self.key = key
        super(ValidationError, self).__init__(message, key)


class Validator(object):
    error = ''

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


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


class ValidatorEqual(Validator):
    error = 'equal format'

    def __call__(self, value, n_value):
        if value != n_value:
            return False
        return True


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
