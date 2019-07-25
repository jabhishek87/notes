#!/usr/bin/env python
from setuptools import setup

setup(
    setup_requires=['pbr', 'pytest-runner'],
    tests_require=['pytest', 'pytest-cov'],
    pbr=True,
    test_suite="tests",
)
