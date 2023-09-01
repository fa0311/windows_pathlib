from setuptools import setup, find_packages


NAME = "windows_pathlib"
VERSION = "0.0.1"
PYTHON_REQUIRES = ">=3.6"
REQUIRES = []

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=NAME,
    version=VERSION,
    description="Best Practices for Handling Paths in Windows.",
    author="yuki",
    author_email="yuki@yuki0311.com",
    url="https://github.com/fa0311/windows_pathlib",
    keywords=["pathlib"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description_content_type="text/markdown",
    long_description=long_description,
    package_data={"windows_pathlib": ["py.typed"]},
)
