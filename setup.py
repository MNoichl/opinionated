#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name="opinionated",
    url="https://github.com/MNoichl/opinionated",
    license='MIT',

    author="Maximilian Noichl",
    author_email="noichlmax@hotmail.co.uk",

    description="Add-on for Matplotlib to produce pretty hrbrtheme-like-plots plots",

    long_description="Add-on for Matplotlib to produce pretty hrbrtheme-like-plots plots",

    packages=["opinionated"],
    package_data={
      'opinionated': ['data/*.mplstyle'],
   },
    install_requires=['matplotlib'],

    # Derive version from git. If HEAD is at the tag, the version will be the tag itself.
    version_config={
        "version_format": "{tag}.dev{sha}",
        "starting_version": "v0.0.1"
    },
    setup_requires=['better-setuptools-git-version'],

    classifiers=[
        'Framework :: Matplotlib', 
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    zip_safe=False,
)