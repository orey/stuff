# README

This is a set of software and recipes to install them in harsh conditions.

## Software that just run

  * Cntlm
  * DoubleCommander
  * Python portable zip
  * TexStudio

## Home folder

Most portable or Linux-like tools require a home directory.

Under Windows, the home directory is: `C:\Users\Toto\`. In a Cygwin configuration, the home directory is: `C:\Path\To\cygwin64\home\Toto\`.

## Cygwin

Cygwin can be hard to fully operate in an hostile environment.

Useful commands to integrate into the `.bashrc`:

```
# Usefull alias
alias dev='cd c:/Path/to/DEV'
alias ll='ls -al'

# Cntlm proxy
proxy=127.0.0.1:3128

# Classical proxy environment variables
export http_proxy=$proxy
export HTTP_PROXY=$proxy
export https_proxy=$proxy
export HTTPS_PROXY=$proxy

# Setup of the "requests" Python package that checks the certificates
# The certificate must be in pem format
REQUESTS_CA_BUNDLE=c:/Path/To/DEV/cert/cacert.pem
export REQUESTS_CA_BUNDLE

export PYTHONPATH=C:/Path/To/DEV/Software/cygwin64/lib/python3.6
```

Usefull Cygwin programs

  * python3
  * nano
  * curl
  * wget
  * git
  * bash-completion

Some installations of Cygwin are not consistent:

  * `pip3 install module` installs the module in `/cygdrive/c/path/to/cygwin64/lib/python3.6/site-packages`
  * The default configuration sets the `sys.path` variable to `/usr/lib/python3.6/*`

Creating a link to `/cygdrive/c/path/to/cygwin64/lib` can solve the problem.

```
$ cd /usr
$ ln -s /cygdrive/c/path/to/cygwin64/lib lib
```

Alternatively, all important folders can be added to the `sys.path` by adding them to the `PYTHONPATH`:

```
export PYTHONHOME=/cygdrive/c/path/to/cygwin64/lib/python3.6
export PYTHONPATH=$PYTHONHOME:$PYTHONHOME/site-packages:$PYTHONHOME/lib-dynload
export PATH=$PYTHONPATH:$PATH

```

## Git

Git can be installed as a Windows portable software or as a component of Cygwin. The firewall can be a problem.

Please integrate the `.gitconfig` into your home directory (see Git folder).

## Archi

  * See the batch into the Archi folder to include a certificate inside the embedded Archi JRE.
  * Archi may use the `.gitconfig` file option, especially the `SSLVerify=False` that can be useful for the collaboration plugin of Archi.


