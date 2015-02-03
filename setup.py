#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='Chrono',
    version='0.1',
    packages=['chrono'],
    url='https://github.com/Edelstadt/Chrono',
    license='BSD',
    author='Marek Dlabacek',
    author_email='marcus.scalpere@gmail.com',
    description='Tool for historical chronology',
    keywords=["historical", "chronology"],
    requires=['docopt'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education, Science/Research,  End Users/Desktop',
        'Topic :: Sociology',
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.4',
        'Natural Language :: Czech',
        ],
        long_description = """\
Tool for historical chronology - Computus
-------------------------------------

Function
 - Dominical letter julian and gregorian
 - cyclus solaris
 - concurrentes
 - numerus aureus (golden number)
 - epactae julian/gregorian
 - easter (pascha) julian and gregorian
 - and Moveable Feast

This version requires Python 3 or later
"""

)
