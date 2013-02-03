import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Peeper",
    version = "0.1",
    author = "Jose Vidal",
    author_email = "javidgon@gmail.com",
    description = ("Thin events' recorder library"),
    license = "BSD",
    keywords = "events recorder github",
    url = "http://josevidal.me",
    zip_safe=False,
    packages=['peeper', 'peeper.services'],
    install_requires=read('requirements.pip'),
    long_description=read('README.md')
)
