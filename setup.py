#!/usr/bin/env python
import os
import sys
from setuptools import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit(0)

setup(
    version='0.0.1',
    name='django-route-decorator',
    description='A flask-style `route` decorator for django views',
    long_description=open('./README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/imbolc/django-route-decorator',

    author='Imbolc',
    author_email='imbolc@imbolc.name',
    license='ISC',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python :: 3',
    ],

    py_modules=['django_route_decorator'],
)
