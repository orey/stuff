# Python installation on Windows without install rights 

## Prerequisite

You need to have a folder from where you have the right to execute any program (except the ones that are blocked by your antivirus).

## Download the embeddable Python zip file

https://www.python.org/downloads/

## Env variables

Then, set the environment variables as shown in the `setenv.bat` file in this folder.

## Proxy and certificates

You can use px proxy.

https://github.com/genotrance/px

You may need to add certificates for certain manipulations.

## pip installation

Download `get-pip.py` on the Pypy site and run `python get-pip.py`. This will install pip.

https://pip.pypa.io/en/stable/installing/

Modify the `python37._pth` or `python38._pth` path accordingly to the `python37._pth` file in this folder to enable pip to work. Essentially, you will reference the `Lib` and `Script` folders and uncomment a line.

## Vitual environments

You can use `venv` or `virtualenv` to creat virtual environments if you need to.

https://packaging.python.org/tutorials/installing-packages/#creating-and-using-virtual-environments

## Module installation

Install modules with `pip install module`.

## Strange problems with sme python modules

### Installtion error with the future module

It seems that the `future` module cannot be installed through `pip` on Windows.

Type: `easy_install future` instead, despite the warning of deprecation (tested with Python 3.7.4 and 3.8.3).

Then, it will be possible to install more complex packages, such as `mkdocs` via the standard `pip install mkdocs`.

## Warning about installations on Windows

Even if you installed the portable version of Python, you will not be able to change the installtion from directory. If you try to copy your `Python` folder in another place on your hard drive, that will not work. You have to redo the process.

*(Updated June 2020)*


