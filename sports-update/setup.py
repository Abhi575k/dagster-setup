from setuptools import find_packages, setup

setup(
    name="sports_update",
    packages=find_packages(exclude=["sports_update_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
