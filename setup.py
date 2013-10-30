#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='mikoto',
      version='0.0.1',
      keywords=('markdown', 'Douban'),
      description='better Markdown Render',
      license='New BSD',

      url='https://github.com/qingfeng/mikoto',
      author='qingfeng',
      author_email='qingfeng@douban.com',

      packages=find_packages(),
      include_package_data=True,
      platforms='any',
      install_requires=['Pygments',
                        'chardet',
                        'pytest',
                        'misaka-1.0',
                        ],
      dependency_links=[
            'https://github.com/qingfeng/misaka/tarball/master#egg=misaka-1.0'
        ]
      )