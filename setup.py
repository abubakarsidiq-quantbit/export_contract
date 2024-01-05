from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in export_contract/__init__.py
from export_contract import __version__ as version

setup(
	name="export_contract",
	version=version,
	description="export_contract",
	author="export_contract",
	author_email="21pradipjadhav@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
