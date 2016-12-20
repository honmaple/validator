#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: exceptions.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-20 16:32:53 (CST)
# Last Update:星期二 2016-12-20 21:31:22 (CST)
#          By:
# Description:
# **************************************************************************


class ValidationError(ValueError):
    def __init__(self, message, key=None):
        self.message = message
        self.key = key
        super(ValidationError, self).__init__(message, key)
