import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="JustifyText",
	version="0.2.1.post3",
	author="cjtx",
	author_email='cjtx.code@gmail.com',
	license='Apache License 2.0',
	description="Returns list of strings *exactly* n width",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/cjtx/JustifyText",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: Apache Software License",
		"Operating System :: OS Independent",
	],
	keywords='justify string format'
)
