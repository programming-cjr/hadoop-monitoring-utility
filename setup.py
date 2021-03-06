#!/usr/bin/env python2
import os
from setuptools import setup

setup(name='hadoop-monitoring-utility',
      version='0.0.1',
      description="monitoring utility for hadoop cluster",
      long_description=open(
          os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
      author='Kirill Goldshtein',
      author_email='goldshtein.kirill@gmail.com',
      packages=['monitoring'],
      package_dir={'monitoring': 'monitoring'},
      install_requires=['PyYAML >= 3.10',
                        'psutil >= 0.6.1',
                        'requests >= 1.0',
                        'jinja2'],
      test_suite='tests',
      scripts=['bin/hadoop-monitoring-values',
               'bin/hadoop-monitoring-generate-mibs'],
      license='GPLv2',
      url='https://github.com/go1dshtein/hadoop-monitoring-utility',
      include_package_data=True,
      classifiers=['Intended Audience :: Developers',
                   'Environment :: Console',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Natural Language :: English',
                   'Development Status :: 1 - Planning',
                   'Operating System :: Unix',
                   'Topic :: Utilities'])
