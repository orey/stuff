# Python installation on Windows without install rights 

## Prerequisite

You need to have a folder from where you have the right to execute any program (except the ones that are blocked by your antivirus).

## 1. Download the embeddable Python zip file

https://www.python.org/downloads/

## 2. Modify the python path

Modify the `python37._pth` or `python38._pth` path accordingly to the `python37._pth` file in this folder to enable pip to work. Essentially, you will reference the `Lib` and `Script` folders and uncomment a line.

Note: Those folders are referenced in the `setenv.bat` file.

See samples in this folder.

## 3. Env variables in setenv

Then, set the environment variables as shown in the `setenv.bat` file in this folder, pointing to your folder

See sample in this folder.

## 4. Proxy and certificates

You can use px proxy.

https://github.com/genotrance/px

## 5. pip installation

Download `get-pip.py` on the Pypy site and run `python get-pip.py`. This will install pip.

https://pip.pypa.io/en/stable/installation/

To be able to run "python get-pip.py" with no certificate issues:

* Gather your certificates in a folder (Bin64, x509)
* Use the setenv provided
* Create the pip env variable in setenv and add the pip.ini file in the target of this env variable (generally the `python` folder)

## 6. venv installation

`venv` is not part of the minimal portable distribution of Python, so you have to install it.

```
> pip install virtualenv
```

## 7. Module installation

Install modules with `pip install module`.

### Warning about installations on Windows

Even if you installed previously the portable version of Python, you will not be able to change the installation from the initial directory to another. If you try to copy your `Python` folder in another place on your hard drive, that will not work. You have to redo the process.

## 8. pip.ini in home directory

Don't forget to include the pip.ini file in the home directory and to enable the main domain name of your company.

## Troubleshooting

### Installation error with the future module

It seems that the `future` module cannot be installed through `pip` on Windows.

Type: `easy_install future` instead, despite the warning of deprecation (tested with Python 3.7.4 and 3.8.3).

Then, it will be possible to install more complex packages, such as `mkdocs` via the standard `pip install mkdocs`.

*Note June 2021*: The Python 3.9.5 does not offer this option anymore (`easy_install` deprecated).

### Problem when installing mkdocs

For `mkdocs` with Python 3.9.5, installation was not possible due a dependency problem in `markdown` package: `AttributeError: 'zipimporter' object has no attribute 'exec_module'`.

The following fix (downgrading the version of `markdown`) is working:

```
> pip uninstall markdown
> pip install markdown==3.2.2
```

*(Updated May 2025)*

