from setuptools import setup, find_packages, version
from setuptools.depends import Require

def read_requirements():
    with open('requirements.txt') as req:
        content = req.read()
        requirements = content.split('\n')

setup(
    name='crack',
    version='0',
    packages=find_packages(),
    install_package_data=True,
    install_required=read_requirements(),
    entry_points='''
        [console_scripts]
        crack=crack.crack:crack
    '''
)