#!/usr/bin/env python3

from setuptools import setup

setup(name='CibToGo',
      version='0.1',
      author='Xin Liang',
      author_email='XLiang@suse.com',
      scripts=['bin/cibToGo'],
      install_requires=['lxml', 'jinja2'])
