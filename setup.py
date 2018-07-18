#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:copyright: (c) 2018 by Mitchell Lisle
:license: MIT, see LICENSE for more details.
"""
import os
import sys

from setuptools import setup
from setuptools.command.install import install

setup(name='martha',
      version='JumpyParrot',
      description='A package for Exploratory Data Analysis',
      url='http://github.com/mitchelllisle/martha',
      author='Mitchell Lisle',
      author_email='lislemitchell@gmail.com',
      packages=['martha'],
      license='MIT',
      install_requires=[
          'boto3',
          'pandas',
          'numpy',
          'hurry.filesize',
          'altair'
      ],
      python_requires='>=3',
      zip_safe=False)
