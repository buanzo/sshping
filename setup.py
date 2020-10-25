# -*- coding: utf-8 -*-
from os import path
from setuptools import setup

# Imports content of requirements.txt into setuptools' install_requires
with open('requirements.txt') as f:
    requirements = f.read().splitlines()


def get_version():
    with open('sshping.py') as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])


description = "ping utility that lets you ping hosts that are only defined in your ~/.ssh/config file"


setup(name='sshping',
      version=get_version(),
      description=description,
      long_description=description,
      keywords="networking,ssh,ping",
      author='Arturo "Buanzo" Busleiman',
      author_email='buanzo@buanzo.com.ar',
      url='https://github.com/buanzo/sshping',
      license='MIT License',
      zip_safe=False,
      python_requires='>=3.6',
      py_modules=['sshping'],
      namespace_packages=[],
      install_requires=requirements,
      entry_points={
         'console_scripts': [
            'sshping = sshping:run',
         ],
      },
      classifiers=[
         'Environment :: Console',
         'Intended Audience :: System Administrators',
         'Programming Language :: Python',
      ])
