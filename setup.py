#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'slack_handler',
    'author': 'Dan Cohen',
    'url': 'www.github.com/danie1cohen/slack_handler',
    'download_url': 'https://www.github.com/danie1cohen/slack_handler.git',
    'author_email': 'daniel.o.cohen@gmail.com',
    'version': '0.1.5',
    'install_requires': ['requests'],
    'packages': ['slack_handler'],
    'scripts': [],
    'name': 'slack_handler'
}

setup(**config)
