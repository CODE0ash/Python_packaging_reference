
#from distutils.core import setup
from setuptools import setup, find_packages

setup(name='flask_daemon',
      version='1.0',
      description='Python Distribution Utilities',
      author='Panchal',
      author_email='ashupanchal.007@gmail.com',
      #url='https://www.python.org/sigs/distutils-sig/',
      packages=find_packages(), #[flask_deamon]
      include_package_data=True,
      zip_safe=False,
      entry_points = {
              'console_scripts':[
                  'flask_daemon = flask_daemon.test_flask_daemon:main'
                              ]
                      },
      install_requires =['Flask','waitress']
      
      
      )
      
      
      
      
#to install , get to the setup.py containing directory and type: 
#for development
#pip install -e .

#for production
#pip install .