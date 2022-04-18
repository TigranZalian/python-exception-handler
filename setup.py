from setuptools import find_packages, setup
from src.exception_handler import __version__

dev_requires = open("dev-requirements.txt").read().strip().split("\n")

setup(
    name="exception_handler",
    version=__version__,
    description="Exception Handler python package.",
    long_description=open("README.md").read(),
    author="Tigran Zalian",
    package_dir={"": "src"},
    requires=["typing_extensions"],
    packages=find_packages(where="src"),
    license="MIT",
    python_requires=">=3.7"
)