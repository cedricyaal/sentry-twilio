#!/usr/bin/env python
"""
sentry-twilio
=============

A plugin for Sentry which sends SMS notifications via Twilio.

:copyright: (c) 2012 by Matt Robenolt
:license: BSD, see LICENSE for more details.
"""
from setuptools import setup, find_packages


install_requires = [
    'sentry>=8.0.0',

    # We don't need full `phonenumbers` library
    'phonenumberslite<8.0',
]

setup(
    name='sentry-twilio',
    version='0.1.0',
    author='Matt Robenolt',
    author_email='matt@ydekproductons.com',
    url='https://github.com/mattrobenolt/sentry-twilio',
    description='A plugin for Sentry which sends SMS notifications via Twilio',
    long_description=__doc__,
    license='BSD',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    entry_points={
        'sentry.apps': [
            'twilio = sentry_twilio',
        ],
        'sentry.plugins': [
            'twilio = sentry_twilio.models:TwilioPlugin',
        ]
    },
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
