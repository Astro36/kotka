from codecs import open
from os import path
from setuptools import setup, find_packages

basedir = path.abspath(path.dirname(__file__))
with open(path.join(basedir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='kotka',
    version='0.1.0',
    description='Korean Obfuscation ToolKit Advanced',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Seungjae Park',
    author_email='astro.psj@gmail.com',
    url='https://github.com/Astro36/kotka',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Korean',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic',
    ],
    license='MIT',
    keywords='korean-nlp, korean-text-processing, hangul, toolkit',
    python_requires='>=3.6',
)
