# GPIB RESTful Service

A REST API for Linux GPIB

## Non python Requirements

- Linux GPIB (Setup for Raspberry: https://xdevs.com/guide/agilent_gpib_rpi/)
- GPIB Adapter (I used his one: Agilent 82357B)

## Running the Server

### Installing the python requirements

The Python Requirements are listed in the "requirements.txt" file and can be insalled in the following way.

```console
$ pip install -r requirements.txt
```
### Only Devmode

In Devmode you can run the Server without having Linux GPIB Installed and Running. 
You can use the dummy implemnts of the python gpib module.

For enableing run the following script 

```console
$ ./enable_dummy_gpib.sh
```
this will copy a dummy module of gpib into the project with Mock returns for the GPIB VISA Commmands.

```console
$ ./disable_dummy_gpib.sh
```
will disable the dummy

### How to Start

To start your Server for Localhost for Development, navigate to the src directory and then type

```console
$ python gpib_server.py
```
this will start the GPIB RESTful Service for your local IP Range.

For productive use in an Automated Test and Messurement System an WSGI Server like gunicorn is recomended
