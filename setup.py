#!/usr/bin/env python3
import pathlib
import subprocess

from setuptools import setup
from setuptools.command.install import install


class InstallWithCompiledMessages(install):
    def run(self):
        subprocess.run(["make", "-C", pathlib.Path(__file__).parent], check=True)
        super().run()


setup(
    name="python-template",
    version="0.1",
    description="Python project template",
    long_description="Turris python project template.",
    url="https://gitlab.labs.nic.cz/turris/python-template",
    author="CZ.NIC, z. s. p. o.",
    author_email="software@turris.cz",
    license="GPLv3.0-or-later",
    packages=[
        "foo",
    ],
    entry_points={
        "console_scripts": ["foo = foo.__main__:main"],
    },
    package_data={
        "foo": ["locale/*/*.mo"],
    },
    install_requires=[],
    install_extra_requires=[],
    setup_requires=["babel"],
    cmdclass={"install": InstallWithCompiledMessages},  # type: ignore
)
