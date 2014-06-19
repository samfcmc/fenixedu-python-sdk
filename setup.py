"""Script to install FenixEdu API python SDK"""

#!/usr/bin/env python

from distutils.core import setup

setup(name='fenixedu_api_sdk',
		version='1.0',
		description='FenixEdu API SDK for python',
		author='Samuel Coelho',
		author_email='samuelfcmc@gmail.com',
		url='https://github.com/samfcmc/fenixedu-python-sdk',
		py_modules=['fenixedu'],
		install_requires=['requests']
		)
