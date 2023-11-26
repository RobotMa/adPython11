#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Qianli Ma",
    author_email='qianli.ma622@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Advanced techniques in using Python 3.11, especially those that are different from C++",
    entry_points={
        'console_scripts': [
            'adPython11=adPython11.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='adPython11',
    name='adPython11',
    packages=find_packages(include=['adPython11', 'adPython11.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/RobotMa/adPython11',
    version='0.0.1',
    zip_safe=False,
)
