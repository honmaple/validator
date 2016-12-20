#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: test.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-20 21:42:30 (CST)
# Last Update:星期二 2016-12-20 21:48:30 (CST)
#          By:
# Description:
# **************************************************************************
from validator import *
import unittest


class T(unittest.TestCase):
    def test_require(self):
        validator = ValidatorRequire()
        username = ''
        username1 = []
        username2 = {}
        username3 = 'hello'
        self.assertTrue(validator(username3))
        self.assertFalse(validator(username))
        self.assertFalse(validator(username1))
        self.assertFalse(validator(username2))

    def test_url(self):
        validator = ValidatorUrl()
        a = 'www.baidu.com'
        b = 'http://www.baidu.com'
        c = 'https://www.baidu.com'
        self.assertFalse(validator(a))
        self.assertTrue(validator(b))
        self.assertTrue(validator(c))

    def test_email(self):
        validator = ValidatorEmail()
        a = 'example@ccc.com'
        b = 'example@ccc.c'
        c = 'example@ccc'
        d = 'exampleccc.co'
        self.assertTrue(validator(a))
        self.assertTrue(validator(b))
        self.assertFalse(validator(c))
        self.assertFalse(validator(d))

    def test_phone(self):
        validator = ValidatorPhone()
        a = '1323213213'
        b = '1323213213s'
        c = '13232132134'
        self.assertFalse(validator(a))
        self.assertFalse(validator(b))
        self.assertTrue(validator(c))

    def test_integer(self):
        validator = ValidatorInteger()
        self.assertTrue(validator(3))
        self.assertFalse(validator('s'))
        validator = ValidatorInteger(min=1, max=4)
        self.assertTrue(validator(3))
        self.assertFalse(validator(6))
        validator = ValidatorInteger(min=1, max=4, size=2)
        self.assertTrue(validator(2))
        self.assertFalse(validator(3))

    def test_and(self):
        validator = And(ValidatorInteger(), ValidatorRequire())
        self.assertFalse(validator('ss'))
        self.assertTrue(validator('1'))

    def test_or(self):
        validator = Or(ValidatorInteger(), ValidatorRequire())
        self.assertTrue(validator('ss'))
        self.assertTrue(validator('1'))


if __name__ == '__main__':
    unittest.main()
