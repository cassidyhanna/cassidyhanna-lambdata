# setup.py file
from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="cassidy-lambdata",
    version="1.0",
    author="MJ Rossetti",
    author_email="datacreativellc@gmail.com",
    description="For example purposes",
    long_description=long_description,
    # required if using a md file for long desc
    long_description_content_type="text/markdown",
    # license="MIT",
    url="https://github.com/cassidyhanna/cassidyhanna-lambdata",
    # keywords="",
    packages=find_packages()  # ["Lambdata"]
)
