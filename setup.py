"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['Channel_3_Ver_2.py']
DATA_FILES = []
OPTIONS = {'iconfile':'arc.icns',}

setup(
    name="Channel_3_Ver_1",
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
