#!/usr/bin/env python3
from setuptools import setup

setup(name='dev_aberto_bardeus',
      version='0.1',
      packages=['dev_aberto'],
      author='hsalberti',
      python_requires= '>=3.6',
      install_requires=[
            'requests',],
      scripts=['scripts/hello.py'],
      
      )