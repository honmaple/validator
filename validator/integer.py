#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: integer.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-20 21:30:29 (CST)
# Last Update:星期五 2016-12-23 17:16:21 (CST)
#          By:
# Description:
# **************************************************************************
from .base import Validator


class ValidatorInteger(Validator):
    def __call__(self, value):
        self.value = value
        min = self.kwargs.get('min')
        max = self.kwargs.get('max')
        size = self.kwargs.get('size')
        if min is not None and max is not None:
            assert min <= max
        try:
            value = int(value)
            if size is not None and size != value:
                return False
            if min is not None and value < min:
                return False
            if max is not None and value > max:
                return False
        except ValueError:
            return False
        return True


