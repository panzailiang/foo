from setuptools import setup

setup(
    name='foo',
    version='1.0',
    author='allenpan',
    py_modules=['foo'],
    install_requires=['requests'],
    entry_points={
        'console_scripts':['mycmd = foo:main']
    }
)