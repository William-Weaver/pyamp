import os
import sys
from setuptools import setup

try:
    print 'Testing gstreamer python support...'
    import pygst
    pygst.require('0.10')
    import gst
except ImportError:
    sys.exit("Cannot install pyamp, no gstreamer python bindings present")

__version__ = None
# Populate __version__ using _pyamp._version module, without importing
this_dir_path = os.path.dirname(__file__)
version_module_path = os.path.join(this_dir_path, 'pyamp', '_version.py')
exec(file(version_module_path).read())

setup(
    name='pyamp',
    version=__version__,
    install_requires=[
        'Twisted',
        'blessings'],
    packages=[
        'pyamp'],
)