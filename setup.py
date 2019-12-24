#!/usr/bin/env python

"""Kegbot Server package.

Kegbot is a hardware and software system to record and monitor access to a
kegerator.  For more information and documentation, see http://kegbot.org/
"""

from setuptools import setup, find_packages

VERSION = '1.4.0'
DOCLINES = __doc__.split('\n')

SHORT_DESCRIPTION = DOCLINES[0]
LONG_DESCRIPTION = '\n'.join(DOCLINES[2:])
DEPENDENCIES = [
    'Celery',
    'django-bootstrap-pagination',
    'django-crispy-forms',
    'django-imagekit',
    'django-nose',
    'django-redis',
    'django-registration-redux',
    'Django~=2.2',
    'flake8',
    'foursquare',
    'gunicorn',
    'httplib2',
    'isodate',
    'jsonfield',
    'kegbot-api',
    'kegbot-pyutils',
    'mock',
    'PyMySQL',
    'pillow',
    'protobuf',
    'python-gflags',
    'pytz',
    'redis',
    'rednose',
    'requests',
    'requests-mock',
    'requests-oauthlib',
    'tweepy',
    'vcrpy',
    'whitenoise',
]


setup(
    name='kegbot',
    version=VERSION,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='Bevbot LLC',
    author_email='info@bevbot.com',
    url='https://kegbot.org/',
    packages=find_packages(),
    scripts=[
        'bin/kegbot',
        'bin/setup-kegbot.py',
    ],
    install_requires=DEPENDENCIES,
    dependency_links=[
        'https://github.com/jakogut/kegbot-api/tarball/master#egg=kegbot-api-1.2.0',
        'https://github.com/jakogut/kegbot-pyutils/tarball/master#egg=kegbot-pyutils-0.2',
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': ['instance=django.core.management:execute_manager'],
    },
)
