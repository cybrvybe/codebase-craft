from setuptools import setup

setup(
    name="codebase-craft",
    version="0.1",
    packages=["codebase_craft"],
    entry_points={
        "console_scripts": [
            "codebase=codebase_craft.codebase:main",
        ],
    },
)
