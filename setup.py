#!/usr/bin/env python
import os
import sys

from setuptools import setup

if sys.argv[-1] == "publish":
    err = os.system("python -m pytest tests.py")
    if err:
        exit(err)
    os.system("python setup.py bdist_wheel")
    os.system("python -m twine upload --skip-existing dist/*")
    sys.exit(0)

setup(
    version="0.2.0",
    name="django-route-decorator",
    description="A flask-style `route` decorator for django views",
    long_description=open("./README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/imbolc/django-route-decorator",
    author="Imbolc",
    author_email="imbolc@imbolc.name",
    license="ISC",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python :: 3",
    ],
    py_modules=["route_decorator"],
)
