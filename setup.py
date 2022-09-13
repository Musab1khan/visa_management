from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in visa_management/__init__.py
from visa_management import __version__ as version

setup(
	name="visa_management",
	version=version,
	description="This module is developed for visa management of employees. It provides details information about Visa Applications, Visa Approvals, Reports for Visa Information, Visa Availability and Visa Usage Details",
	author="Solufy",
	author_email="contact@solufy.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
