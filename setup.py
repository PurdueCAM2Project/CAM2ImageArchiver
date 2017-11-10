from setuptools import setup
setup(
  name = 'CAM2ImageArchiver',
  packages = ['CAM2ImageArchiver'],
  version = '0.1',
  description = 'Network camera image retrieval and archiving.',
  author = 'CAM2 Research Group',
  author_email = 'cam2proj@ecn.purdue.edu',
  license='Apache License 2.0',
  url = 'https://github.com/cam2proj/CAM2ImageArchiver',
  download_url = 'https://github.com/cam2proj/CAM2ImageArchiver/archive/0.1.tar.gz',
  keywords = ['computer', 'vision', 'CAM2'],
  classifiers = [
    'Development Status :: 4 - Beta',
    'Programming Language :: Python :: 2.7',
    'License :: OSI Approved :: Apache Software License'
  ],
  python_requires='2.7.*',
  install_requires=[
    'alabaster',
    'Babel',
    'certifi',
    'chardet',
    'funcsigs',
    'idna',
    'imagesize',
    'Jinja2',
    'MarkupSafe',
    'mock',
    'MySQL-python',
    'numpy',
    'pbr',
    'Pygments',
    'pytz',
    'six',
    'snowballsstemmer',
    'typing',
    'urllib3'
  ]
)