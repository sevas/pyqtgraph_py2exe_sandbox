
from distutils.core import setup
import py2exe
import os
import sys 

THIS_DIR = os.path.dirname(__file__)
DIST_DIR = os.path.join(THIS_DIR, "dist_py2exe")

setup(
    windows=['pyside_opengl_app.py', 'pyqtgraph_app.py'],
    options={"py2exe":{
        # this forces the inclusion of ctypes.util, which is required to load 
        # the opengl win32 backend. Neither py2exe nor cx_freeze seem to
        # be able to autodiscover this, which leads to application that 
        # crash without printing an error
        'packages': ['ctypes'],  
        'includes': [],
        'excludes': ["PyQt4", "pysideuic.port_v2", "OpenGL", "OpenGL_accelerate"],
        'dist_dir': DIST_DIR
        }
    } 
)

import shutil

def copy_package_dir(dir, to):
    print("Copying {} to {}".format(dir, to))
    if os.path.exists(to):
        shutil.rmtree(to)
    shutil.copytree(dir, to, ignore=shutil.ignore_patterns("*__pycache__*"))

import OpenGL
copy_package_dir(os.path.dirname(OpenGL.__file__), os.path.join(DIST_DIR, "OpenGL"))

import OpenGL_accelerate
copy_package_dir(os.path.dirname(OpenGL_accelerate.__file__), os.path.join(DIST_DIR, "OpenGL_accelerate"))