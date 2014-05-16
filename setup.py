try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Tool for running SQL code on multiple databases',
    'author': 'Fero kittler',
    'url': 'https://github.com/ferokittler/pysqlall',
    'download_url': 'https://github.com/ferokittler/pysqlall/archive/master.zip',
    'author_email': 'kittler.fero@gmail.com',
    'version': '0.1',
    'install_requires': [],
    'packages': ['pysqlall'],
    'scripts': [],
    'name': 'pysqlall'
}

setup(**config)
