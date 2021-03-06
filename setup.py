#!/usr/bin/env python

from setuptools import setup

setup(
    name='PyMata',
    packages=['PyMata'],
    #install_requires=['pyserial==2.7'],
    install_requires=['pyserial'],

    version='2.17',
    description="A Python Protocol Abstraction Library For Arduino Firmata",
    author='Alan Yorinks',
    author_email='MisterYsLab@gmail.com',
    url='https://github.com/MrYsLab/PyMata',
    download_url='https://github.com/MrYsLab/PyMata',
    keywords=['Firmata', 'Arduino', 'Protocol'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
        'Topic :: Home Automation',
    ],
)
