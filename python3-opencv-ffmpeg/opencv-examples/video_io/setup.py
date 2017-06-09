# to install locally run python3 setup.py sdist && pip3 install -e .

from distutils.core import setup

setup(name='video_io',
      version='0.1',
      py_modules=['io_parser', 'videoreader', 'videowriter']
      )