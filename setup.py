from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ftdi-rf',
    version='0.9.7',
    author='Dimitrios Politis',
    author_email='civisd@gmail.com',
    description='Sending and receiving 433/315MHz signals with low-cost GPIO RF modules on a Generic PC, using ftdi serial hardware',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dpolitis/ftdi-rf',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords=[
        'ftdi',
        'rf',
        'gpio',
        'radio',
        '433',
        '433mhz',
        '315',
        '315mhz'
    ],
    install_requires=['pyftdi'],
    scripts=['scripts/ftdi-rf_send', 'scripts/ftdi-rf_receive'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests'])
)
