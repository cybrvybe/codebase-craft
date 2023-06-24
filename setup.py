from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="codebase-craft",
    version="0.1",
    packages=["codebase_craft"],
    entry_points={
        "console_scripts": [
            "codebase=codebase_craft.codebase:main",
        ],
    },
    install_requires=requirements
)
