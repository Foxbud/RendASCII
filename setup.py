from setuptools import find_packages
from setuptools import setup


setup(
    name='rendascii',
    use_scm_version=True,
    setup_requires=['setuptools_scm',],
    description='ASCII 3D rendering engine',
    url='https://bitbucket.org/foxbudpersonal/rendascii',
    author='Garrett Fairburn',
    author_email='breadboardfox@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'': ['*.so',],},
    include_package_data=True
)
