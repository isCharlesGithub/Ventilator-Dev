from setuptools import setup, find_packages
import os
import subprocess

depend_links = []

# detect if on raspberry pi, and
# set location to wheel if we are
IS_RASPI = False
ret = subprocess.call(['grep', '-q', 'BCM', '/proc/cpuinfo'])
if ret == 0:
    IS_RASPI = True
    os.system("sudo +x INSTALL")
    os.system("sudo ./INSTALL")

setup(
    name="ventilator",
    author="vent team",
    author_email="vent@vents.com",
    description="some description of how we made a ventilator",
    keywords="vents ventilators etc",
    url="https://ventilator.readthedocs.io",
    version="0.0.2",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'PySide2',
        'pyqtgraph>=0.11.0rc0',
        'pigpio'
    ],
    dependency_links=depend_links
)
