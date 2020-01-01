"""Setup for the ezkey package."""

import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Wes Bailey",
    author_email="espressoandcode@gmail.com",
    name='ezkey',
    license="Apache 2.0",
    description='ezkey is a package that allows developers to easily manage locally stored API keys.',
    version='v0.0.1',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/espressoAndCode/ezkey',
    packages=setuptools.find_packages(),
    python_requires=">=2.7",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
