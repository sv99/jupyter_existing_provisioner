# jupyter_existing_provisioner

This package register existing_provisioner endpoint for attach to the running jupyter kernel.

    pip install jupyter_existing_provisioner
    # check endpoint
    jupyter pyxll install

Based on [PyXLL-Jupyter](https://github.com/pyxll/pyxll-jupyter).

## Requirements

- Jupyter-client >= 7.0.0
  
### Optional

- jupyterlab >= 4.0.0

## Installation

To install this package use:

    pip install jupyter_existing_provisioner

Once installed register `existing_provisioner` endpoint for `jupyter_client`.

    # check endpoints
    jupyter kernelspec provisioners

## Jupyter Lab

    # prepare working environment
    pip install jupyterlab
    pip install qtconsole
    python embed_qtconsole.py

    # connect to the last kernel
    jupyter lab --KernelProvisionerFactory.default_provisioner_name=existing-provisioner
    
    # linux: connect to the kernel-xxxx.json file 
    EXISTING_CONNECTION_FILE=kernel-xxxx.json jupyter lab --KernelProvisionerFactory.default_provisioner_name=existing-provisioner
    
    # windows: connect to the kernel-xxxx.json file 
    set EXISTING_CONNECTION_FILE=kernel-xxxx.json
    jupyter lab --KernelProvisionerFactory.default_provisioner_name=existing-provisioner
    
In the working kernel show connection info magic `%connect_info`

## Google Colab

[Connect instruction](https://research.google.com/colaboratory/local-runtimes.html) 

    # prepare for connect colab
    pip install jupyter_http_over_ws
    jupyter serverextension enable --py jupyter_http_over_ws

    jupyter lab --KernelProvisionerFactory.default_provisioner_name=existing-provisioner \
        --ServerApp.allow_origin='https://colab.research.google.com'
    
Start [Google Colab](https://colab.research.google.com/?hl=ru_ru) and 
connect to the local environment - url from terminal.

