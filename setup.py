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

setup(name='lenny',
      version='0.1',
      description='A package for Exploratory Data Analysis',
      url='http://github.com/mitchelllisle/lenny',
      author='Mitchell Lisle',
      author_email='lislemitchell@gmail.com',
      packages=['lenny'],
      license='MIT',
      install_requires=[
          'boto3',
          'pandas',
          'numpy'
      ],
      python_requires='>=3',
      zip_safe=False)
