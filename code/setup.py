from setuptools import setup
from setuptools import find_packages

setup(name='dlgo',
      version='0.2',
      description='Deep Learning and the Game of Go',
      url='http://github.com/maxpumperla/deep_learning_and_the_game_of_go',
      install_requires=[
            'numpy<=2.5.4', 
            'tensorflow==2.12.1', 
            'keras==3.15.0', 
            'gomill', 
            'Flask>=0.10.1', 
            'Flask-Cors', 
            'future', 
            'h5py', 
            'six'],
      license='MIT',
      packages=find_packages(),
      zip_safe=False)
