# coding=utf-8
from os import path
from distutils.core import setup
from setuptools import find_packages

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="pyage",
    description="Python Agent-based evolution",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    version="1.2.12",
    author="Maciej Kaziród",
    author_email="kazirod.maciej@gmail.com",
    install_requires=['Pyro4==4.17']
)
