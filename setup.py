from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    r = f.read().splitlines()

setup(
    name="AITravelPlanner",
    install_requires=r,
    packages=find_packages(),
    version="0.1"
)