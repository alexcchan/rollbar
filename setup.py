#!/usr/bin/python

from distutils.core import setup

setup(
	# Basic package information.
	name = 'rollbar',
	version = '0.0.0',
	packages = ['rollbar'],
	include_package_data = True,
	install_requires = ['httplib2', 'simplejson'],
	url = 'https://github.com/alexcchan/rollbar/tree/master',
	keywords = 'rollbar api',
	description = 'Rollbar API Wrapper for Python',
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Internet'
	],
)


