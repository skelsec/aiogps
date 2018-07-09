from setuptools import setup, find_packages

setup(
    # Application name:
    name="aiogps",

    # Version number (initial):
    version="0.0.1",

    # Application author details:
    author="",
    author_email="",

    # Packages
    packages=find_packages(),

    # Include additional files into the package
    include_package_data=True,


    # Details
    url="https://github.com/skelsec/aiogps",

    zip_safe = True,
    #
    # license="LICENSE.txt",
    description="Library to interface with GPSD using asyncio",

    # long_description=open("README.txt").read(),
    python_requires='>=3.6',
    classifiers=(
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
    )    
)
