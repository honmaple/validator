#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: string.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-20 21:29:17 (CST)
# Last Update:星期五 2016-12-23 17:16:51 (CST)
#          By:
# Description:
# **************************************************************************
from .base import Validator


class ValidatorLength(Validator):
    callback = 'length error'

    def __call__(self, value):
        self.value = value
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
