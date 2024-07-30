
import os
import subprocess
import sys

# Create a virtual environment
subprocess.check_call([sys.executable, '-m', 'venv', 'venv'])

# Activate the virtual environment
activate_script = os.path.join('venv', 'Scripts', 'activate') if os.name == 'nt' else os.path.join('venv', 'bin', 'activate')

# Upgrade pip
subprocess.check_call([os.path.join('venv', 'bin', 'python'), '-m', 'pip', 'install', '--upgrade', 'pip'])

# List of dependencies
dependencies = [
    'absl-py==2.1.0',
    'attrs==23.2.0',
    'cffi==1.16.0',
    'contourpy==1.2.0',
    'cycler==0.12.1',
    'et-xmlfile==1.1.0',
    'flatbuffers==23.5.26',
    'fonttools==4.47.2',
    'kiwisolver==1.4.5',
    'matplotlib==3.8.2',
    'mediapipe==0.10.9',
    'mpmath==1.3.0',
    'node==1.2.1',
    'numpy==1.26.3',
    'odict==1.9.0',
    'opencv-contrib-python==4.9.0.80',
    'opencv-python==4.9.0.80',
    'openpyxl==3.1.4',
    'packaging==23.2',
    'pillow==10.2.0',
    'plumber==1.7',
    'protobuf==3.20.3',
    'pycparser==2.21',
    'pygame==2.5.2',
    'PyOpenGL==3.1.7',
    'pyparsing==3.1.1',
    'python-dateutil==2.8.2',
    'six==1.16.0',
    'sounddevice==0.4.6',
    'zope.component==6.0',
    'zope.deferredimport==5.0',
    'zope.deprecation==5.0',
    'zope.event==5.0',
    'zope.hookable==6.0',
    'zope.interface==6.2',
    'zope.lifecycleevent==5.0',
    'zope.proxy==5.2'
]

# Install dependencies
for package in dependencies:
    subprocess.check_call([os.path.join('venv', 'bin', 'pip'), 'install', package])

print("All dependencies have been installed.")
