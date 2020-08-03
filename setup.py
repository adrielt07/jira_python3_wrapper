#!/usr/bin/env python3
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='jiraclient', # Change the name
    packages=[
        'jiraclient'
    ],
    license='None',
    version='0.0.1',
    author='Adriel Tolentino',
    author_email='adriel_tolentino@outlook.com',
    long_description='A simple jira wrapper for Jira',
    install_requires=required,
    packages_dir={
        'jiraclient': 'jiraclient'
    },
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
)
