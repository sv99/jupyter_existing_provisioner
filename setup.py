"""
jupyter_existing_provisioner

This package register existing_provisioner endpoint for attach to the running jupyter kernel.

    pip install jupyter_existing_provisioner
    # check endpoints
    jupyter kernelspec provisioners
"""
from setuptools import setup, find_packages
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="jupyter_existing_provisioner",
    description="Connect to the last started kernel or by connection file.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    version="0.1.3",
    packages=['jupyter_existing_provisioner'],
    include_package_data=True,
    project_urls={
        "Source": "https://github.com/sv99/jupyter_existing_provisioner",
        "Tracker": "https://github.com/sv99/jupyter_existing_provisioner/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows"
    ],
    entry_points={
        "jupyter_client.kernel_provisioners": [
            "existing-provisioner = jupyter_existing_provisioner:ExistingProvisioner"
        ]
    },
    install_requires=[
        "jupyter_client >= 7.0.0",
    ]
)
