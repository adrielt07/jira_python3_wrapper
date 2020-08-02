#!/usr/bin/env python3
import sys

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name=sys.argv[1],
    packages=find_packages(),
    license='None',
    version='0.0.1',
    author='Adriel Tolentino',
    author_email='adriel_tolentino@outlook.com',
    long_description='A simple jira wrapper for Jira',
    install_requires=required,
    entry_point={
        'control_scripts': [
            'cli=testfolder.testfile:main',
        ],
    }
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ]
)
