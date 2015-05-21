import os
from setuptools import setup, find_packages


def read_file(filename):
    basepath = os.path.dirname(os.path.dirname(__file__))
    filepath = os.path.join(basename, filename)
    if os.path.exists(filepath):
        return open(filepath).read()
    else:
        return ''


setup(
  name='guestbook',
  version='1.0.0',
  description='A guestbook web application.',
  long_description=read_file('README.md'),
  author='yhoshino11',
  author_email='yhoshino11@gmail.com',
  url='https://github.com/yhoshino11/GuestBook.git',
  classifiers=[
    'Development Status :: 4 - beta',
    'Framework :: Flaskk',
    'License :: MIT',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
  ],
  packages=find_packages(),
  include_package_data=True,
  keywords=['web', 'guestbook'],
  license='MIT License',
  install_requires=[
    'Flask',
  ],
  entry_points="""
    [console_scripts]
    guestbook = guestbook:main
  """,
)
