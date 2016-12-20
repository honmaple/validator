#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: __init__.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-20 16:32:42 (CST)
# Last Update:星期二 2016-12-20 21:46:51 (CST)
#          By:
# Description:
# **************************************************************************
from .base import And,Or
from .regex import ValidatorEmail, ValidatorPhone, ValidatorUrl
from .string import (ValidatorRequire, ValidatorLength, ValidatorPhoneCaptcha,
                     ValidatorPictureCaptcha)
from .integer import ValidatorInteger
