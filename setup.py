# coding: utf-8
import setuptools

setuptools.setup(
    name = 'Riddles',
    version = '0.1.2',
    author = 'Aleksey Yeletsky',
    author_email = 'a.eletsky@gmail.com',
    packages = setuptools.find_packages(),
    url = 'https://github.com/Tiendil/riddles-collection',
    license = 'LICENSE',
    description = "my hobby project — collection of russian riddles",
    long_description = open('README').read(),
    include_package_data = True # setuptools-git MUST be installed
)
