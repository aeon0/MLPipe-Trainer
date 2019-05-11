from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='MLPipe',  
    version='0.1.0',
    author="Johannes Dobler",
    author_email="jdobler@protonmail.com",
    description="Manage training results, weights and data flow of your Tensorflow models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/j-o-d-o/MLPipe-Trainer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research'
    ],
    packages=find_packages())