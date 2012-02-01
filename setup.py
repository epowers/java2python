#!/usr/bin/env python

from distutils.core import setup

setup(name='java2python',
      version='0.5',
      packages=[
        'java2python',
        'java2python.mod',
        'java2python.config',
        'java2python.lib',
        'java2python.lang',
        'java2python.compiler',
        ],
      package_data={'java2python.lang': ['Java.tokens']},
      scripts=['bin/j2py'],
      )
