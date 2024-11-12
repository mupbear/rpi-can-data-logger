from setuptools import setup, find_packages
setup(
    name='python-can-sender',
    version='1.0',
    author='Jan Sevrin & Joost Asbreuk',
    description='A Python application written for Raspberry Pi that can connect to the a PiCAN shield and transmit all received CAN data to a MySQL database.',
    long_description='Ensure that you have properly set up the PiCAN on the Pi before running. Make sure you change the can0 port to the correct one inside the app.py source code.',
    url='',
    keywords='development, setup, setuptools',
    python_requires='>=3.7, <4',
    packages=find_packages(include=['app', 'app.*']),
    install_requires=[
        'mysql-connector==2.2.9',
        'python-can==4.1.0',
        'pyinstaller==5.10.0',
    ],
)
