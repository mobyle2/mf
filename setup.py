#!/usr/bin/env python

from setuptools import setup, find_packages

requires = [
    'pymongo',
    'mongokit >= 0.8.2'
    ]

setup(name='mf',
      version='0.1.39',
      description='Annotator for mf-pyramid',
      author='Olivier Sallou',
      author_email='olivier.sallou@irisa.fr',
      license='LGPL',
      url='https://github.com/mobyle2/mf',
      packages=['mf'],
      install_requires=requires
     )
