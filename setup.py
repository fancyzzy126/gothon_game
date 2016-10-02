#!usr/bin/python

try:      	
    from setuptools import setup

except ImportError:
    from distutils.core import setup


config = {
    'description': 'My Project',
    'author': 'Felix Zhang',
    'uri': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'felix.zhang@alcatel-lucent.com.',
    'version': '0.1',
    'install_reuqires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47_project'

}

setup(**config)
