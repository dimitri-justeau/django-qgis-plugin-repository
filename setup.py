# coding: utf-8

import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-qgis-plugin-repository',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='GPLv3',
    description='Django reusable application providing a simple way to self-host a QGIS plugin repository within a django project.',
    long_description=README,
    url='https://github.com/dimitri-justeau/django-qgis-plugin-repository/',
    author='Dimitri Justeau (IAC/AMAP)',
    author_email='dimitri.justeau@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPLv3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
    ],
)
