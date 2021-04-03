""" The setup.py file will contain information about your package,
specifically the name of the package, its version, platform-dependencies and a whole lot more."""

from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = '42ai Python package '
LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

# Setting up
setup(
    # the name must match the folder name '42ai'
    name="42ai",
    version=VERSION,
    author="Mo-san",
    author_email="<moboustt@student.1337.ma>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package.

    keywords=['python', 'ai', '42ai'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)