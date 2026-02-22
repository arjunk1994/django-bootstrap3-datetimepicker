import sys
from setuptools import setup

long_description = ''
if 'upload' in sys.argv or 'register' in sys.argv:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')

VERSION = '2.8.4'

setup(
    name='django-bootstrap3-datetimepicker-2',
    packages=['bootstrap3_datetime'],
    include_package_data=True,
    python_requires='>=3.10',
    version=VERSION,
    description='Bootstrap3 compatible datetimepicker for Django projects.',
    long_description=long_description,
    author='Nakahara Kunihiko/Samuel Colvin',
    author_email='s@muelcolvin.com',
    url='https://github.com/samuelcolvin/django-bootstrap3-datetimepicker',
    license='Apache License 2.0',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 4.2',
        'Framework :: Django :: 5.1',
        'Framework :: Django :: 5.2',
    ],
)
