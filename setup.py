from setuptools import setup, find_packages

setup(
    name='backup grep',
    version='1.0.0',
    description='to find the known backup errors in mms0.log file',
    author='Gregory Vinopal',
    author_email='gregory.vinopal@mongodb.com',
    packages=find_packages(),
    install_requires=['colorama'],
)

