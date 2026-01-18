#! /usr/bin/env python
from os import path
from setuptools import setup, find_packages

version = "1.0.5"

with open('README.md') as f:
    long_description = f.read()

install_requires = [
    'acme>=1.12.0',
    'certbot>=1.12.0',
    'dns-lexicon>=3.10.0',
    'dnspython>=2.0',
    'setuptools>=40.8.0',
    'zope.interface>=5.0',
    'requests>=2.25.0'
]

here = path.abspath(path.dirname(__file__))

setup(
    name='certbot-dns-ownadmin',
    version=version,
    description="OwnAdmin Authenticator plugin for Certbot",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Chudeusz/certbot-dns-powerdns-ownadmin',
    author="Chudeusz",
    author_email='chudeusz@ownadmin.pl',
    license='Apache License 2.0',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],

    packages=find_packages(),
    install_requires=install_requires,

    # extras_require={
    #     'docs': docs_extras,
    # },

    entry_points={
        'certbot.plugins': [
            'dns-ownadmin = certbot_dns_ownadmin.dns_ownadmin:Authenticator',
        ],
    }
)
