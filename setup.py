from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='tinybill',
      version=version,
      description="",
      long_description=open(os.path.join('src', 'tinybill', 'README.txt')).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='eRdgEiSt',
      author_email='Gerd Eist',
      url='',
      license='',
      package_dir = {'':'src'},
      packages=find_packages('src', exclude=['ez_setup']),
      namespace_packages=[],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'WebOb',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
[paste.filter_factory]
main = tinybill.main:MainFactory
      """,
      )
