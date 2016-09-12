#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
	'numpy', 'matplotlib', 'seaborn', 'pandas', 'scipy', 'sympy',
	'pyzmq', 'pytz', 'jinja2', 'ipython', 'tornado', 'jsonschema',
	'networkx', 'scikit-image', 'scikit-learn',
]
requirements.reverse()

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='scibag',
    version='0.2.0',
    description="Data science meta-package",
    long_description=readme + '\n\n' + history,
    author="Javi Palanca",
    author_email='jpalanca@gmail.com',
    url='https://github.com/javipalanca/scibag',
    packages=[
        'scibag',
    ],
    package_dir={'scibag':
                 'scibag'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='scibag',
    classifiers=[
        'Development Status :: 7 - Inactive',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
