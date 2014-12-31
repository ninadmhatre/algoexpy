__author__ = 'Ninad'

from setuptools import setup, find_packages

setup(
    name="pylrn",
    version="0.2.4",
    description="Common algorithms & data structure implementations in python",
    url='http://ninadmhatre.github.io/pylrn',
    author="Ninad Mhatre",
    author_email='ninad.mhatre@gmail.com',
    packages=[
        'pylrn',
        'pylrn.Sort',
        'pylrn.DataStructures',
        'pylrn.Quiz'
    ],
    package_data={
        'pylrn': ['setup.py', 'Helper.py', 'Test.py'],
        'pylrn.Sort': ['*.py', '*.info'],
        'pylrn.Quiz': ['*.py', '*.info'],
        'pylrn.DataStructures': ['*.py', '*.info'],
    },
    install_requires=['addonpy'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Education',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Education',
    ],
)
