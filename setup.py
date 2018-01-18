#-*-coding:utf-8-*-

import os
from setuptools import setup

def fread(fname):
    filepath = os.path.join(os.path.dirname(__file__), fname)
    with open(filepath, 'r') as fp:
        return fp.read()

setup(
    name='pick2',
    version='0.7.0',
    description='pick an option in the terminal with a simple GUI',
    long_description=fread('README.md'),
    keywords='terminal gui',
    url='https://github.com/wong2/pick',
    author='jaitaiwan',
    author_email='dan@djcentric.com',
    license='MIT',
    packages=['pick2'],
    tests_require=['nose'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6'
    ]
)
