#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'slack_handler',
    'author': 'Dan Cohen',
    'url': 'git.usccreditunion.org',
    'download_url': 'git.usccreditunion.org/cu/slack_handler',
    'author_email': 'dcohen@usccreditunion.org',
    'version': '0.1.10',
    'install_requires': [],
    'packages': ['slack_handler'],
    'scripts': [],
    'name': 'slack_handler'
}

setup(**config)
