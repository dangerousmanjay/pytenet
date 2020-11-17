#!/usr/bin/env python

from setuptools import setup
import sys


setup(
    name='pytenet',
    version='0.0.1',
    description='Don’t try to understand it. Feel it.',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS INDEPENDENT',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    author='Jae Joon Kim (Thanks to Christopher Nolan)',
    author_email='ojayyezzir@gmail.com',
    url='https://github.com/ojayyezzir/pytenet',
    packages=['pytenet'],
    install_requires=['pyautogui>=0.9'],
    entry_points={
        'console_scripts': [
            'tenet = pytenet:main',
        ],
    },
)
