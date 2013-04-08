#!/usr/bin/env python

import os
from setuptools import setup

import paypalpy

setup(
    name='paypalpy',
    version=paypalpy.__version__,
    description='Python library for the NVP API of PayPal',
    long_description='',
    author='CoNWeT Lab',
    author_email='fdelavega@conwet.com',
    url='http://github.com/conwetlab/paypalpy',
    license='GPLv3+',
    packages=('paypalpy',),
    include_package_data=False,
    install_requires=(),
    tests_require=(),
    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    )
)
