"""Script to install FenixEdu API python SDK"""

#!/usr/bin/env python

from distutils.core import setup, Extension

setup(name='fenixedu',
		version='1.0.0',
		description='FenixEdu API SDK for python',
		author='Samuel Coelho',
		author_email='samuelfcmc@gmail.com',
		url='https://github.com/samfcmc/fenixedu-python-sdk',
		install_requires=['requests'],
		packages=['fenixedu']
		)
