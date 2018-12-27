#!/usr/bin/env python
# -*- coding: utf-8 -*-


##### CONFIGURE A SETUP FILE FOR REAL....

from setuptools import setup
	
# Get dependencies
with open('requirements.txt') as f:
	# converting the requirements.txt to a list of requirements
    all_reqs = f.read().split('\n')

# What does an entry point do?
setup(
    name='Budget',
    python_requires='>=3.6',
    install_requires=all_reqs, # takes a list
    entry_points={'console_scripts': [
        'budget=BudgetREPO.cli:main'], }
)

