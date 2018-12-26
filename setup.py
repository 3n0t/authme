# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='authme',
    version='0.1.0',
    author='3n0t',
    description='aU0?',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    entry_points={'console_scripts': ['authme=authme.cli:run']},
)
