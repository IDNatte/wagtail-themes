import os
from setuptools import find_packages, setup


install_requires = [
    'django>=1.8',
    'wagtail>=1.2'
]

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='wagtail-themes',
    version='0.1.1',
    description='Site specific theme loader for Django Wagtail.',
    long_description=read('README.md'),
    author='Rob Moorman',
    author_email='rob@moori.nl',
    url='https://github.com/moorinteractive/wagtail-themes',
    license='MIT',
    install_requires=install_requires,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5'
    ]
)
