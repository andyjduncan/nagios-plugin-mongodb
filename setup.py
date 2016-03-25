from setuptools import setup
setup(name='nagios-plugin-mongodb',
      version='1.0',
      description='Nagios MongoDB plugin',
      author='Andy Duncan',
      author_email='andy@adjectivecolournoun.com',
      url='https://github.com/andyjduncan/nagios-plugin-mongodb/',
      install_requires=['pymongo'],
      py_modules=['check_mongodb'],
      )
