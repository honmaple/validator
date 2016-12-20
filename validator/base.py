#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: base.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-20 16:34:47 (CST)
# Last Update:星期二 2016-12-20 16:35:51 (CST)
#          By:
# Description:
# **************************************************************************


class Validator(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self, value):
        pass
