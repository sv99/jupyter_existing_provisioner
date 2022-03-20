"""
jupyter_existing_provisioner

This package register existing_provisioner endpoint for attach to the running jupyter kernel.

    pip install jupyter_existing_provisioner
    # check endpoints
    jupyter kernelspec provisioners
"""
from .existing import ExistingProvisioner