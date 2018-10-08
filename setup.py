#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='cibToGoStruct',
      packages=find_packages(),
      version='0.5',
      author='Xin Liang',
      author_email='XLiang@suse.com',
      scripts=['bin/cibToGoStruct'],
      install_requires=['lxml', 'jinja2'])
