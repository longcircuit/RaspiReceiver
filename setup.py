from setuptools import setup, find_packages

setup(
    name="raspi_receiver",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "raspi_receiver = raspi_receiver.cli:main"
        ]}
    )

