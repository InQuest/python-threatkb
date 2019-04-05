import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='threatkb',
    version='1.0.0-alpha2',
    include_package_data=True,
    py_modules=[
        'threatkb',
    ],
    install_requires=['requests'],
    entry_points={
          'console_scripts': [
              'threatkb = threatkb:main'
          ]
    },
    license='BSD',
    description='API and command-line tool for InQuest ThreatKB',
    long_description=README,
    url='https://github.com/InQuest/python-threatkb',
    author='InQuest Labs',
    author_email='labs@inquest.net',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries',
        'Topic :: Internet',
    ],
)
