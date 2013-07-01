try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Hangman',
	'author': 'Cody Tessler',
	'download_url': 'git@github.com:Cojate/hangman.git',
	'verision': '1.0',
	'install_requires': ['nose'],
	'packages': [''],
	'scripts': ['art.py'],
	'name': 'hangman'
}
setup(**config)
