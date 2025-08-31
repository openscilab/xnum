# -*- coding: utf-8 -*-
"""Setup module."""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_requires() -> list:
    """Read requirements.txt."""
    requirements = open("requirements.txt", "r").read()
    return list(filter(lambda x: x != "", requirements.split()))


def read_description() -> str:
    """Read README.md and CHANGELOG.md."""
    try:
        with open("README.md") as r:
            description = "\n"
            description += r.read()
        with open("CHANGELOG.md") as c:
            description += "\n"
            description += c.read()
        return description
    except Exception:
        return '''XNum is a simple and lightweight Python library that helps you convert digits between different numeral systems
                  like English, Persian, Hindi, Arabic-Indic, Bengali, and more.
                  It can automatically detect mixed numeral formats in a piece of text and convert only the numbers, leaving the rest untouched.
                  Whether you're building multilingual apps or processing localized data, XNum makes it easy to handle numbers across different
                  languages with a clean and easy-to-use API.'''


setup(
    name='xnum',
    packages=[
        'xnum', ],
    version='0.5',
    description='XNum: Universal Numeral System Converter',
    long_description=read_description(),
    long_description_content_type='text/markdown',
    author='XNum Development Team',
    author_email='xnum@openscilab.com',
    url='https://github.com/openscilab/xnum',
    download_url='https://github.com/openscilab/xnum/tarball/v0.5',
    keywords="convert numeral number numeral-system digits",
    project_urls={
            'Source': 'https://github.com/openscilab/xnum',
    },
    install_requires=get_requires(),
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Manufacturing',
        'Topic :: Education',
        'Topic :: Text Editors :: Text Processing',
        'Topic :: Software Development :: Localization',
    ],
    license='MIT',
)
