# Tips for running development tools in professional Win64 environment

## Portable versions

Prefer portable versions. Use ```.bat``` scripts to include the various binaries.

```
set PATH=C:\Tools\MyPath:%PATH%
```

## Java software

If your administrator already installed a default JRE in your system, you can use several tools from any folder, provided you know how to launch them in command line.

To know the default version of your JRE type: `java -version`

See the `CommandLineNoInstall` folder for a potential list of tools that you can run easily.

## Basic tools: proxy and explorer

Here is a list of important tools and tricks to install the portable versions:

  * Cntlm local proxy
    * In case of "Couldn't compute FAST_CWD pointer", please check your ini file is in ISO format (and not UTF-8)
    * A good alternative to Cntlm is Px proxy: https://github.com/genotrance/pxhttps://github.com/genotrance/px
  * DoubleCommander is running on evey environment ans is quite powerful

## Git

See the dedicated README page in the `Git` folder.

## Latex on Windows with no installation rights

### Miktex

Use the portable version. To set the firewall, set the following variable:

```
set ALL_PROXY="http://user:pasword@firewall.com:8080"
```

### TexStudio

Could be useful add the path to Miktex in the PATH (generally in install/miktex/bin).

## Python (native Windows)

Look at the `Python` subfolder in this folder.

## Cygwin

### Home folder

Most portable or Linux-like tools require a home directory.

Under Windows, the home directory is: `C:\Users\Toto\`. In a Cygwin configuration, the home directory is: `C:\Path\To\cygwin64\home\Toto\`.

### Cygwin

Cygwin can be hard to fully operate in an hostile environment.

Useful commands to integrate into the `.bashrc`:

```
# Usefull alias
alias dev='cd c:/Path/to/DEV'
alias ll='ls -al'

# Cntlm or Px proxy
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

Some packages don't work with Cygwin, for instance the `mss` package. Choose to use a local python install.

## Archi

  * See the batch files into the Archi folder to include a certificate inside the embedded Archi JRE. This is generally the best way to get through firewalls.
  * Archi may use the `.gitconfig` file option, especially the `SSLVerify=False` that can be useful for the collaboration plugin of Archi.

## Other usefull tools

  * Emacs
  * FreeFileSync
  * innoump => to unpack installations
  * Zim: a great Python personal Wiki (wee also the `scree-capture` compatible python script in the `tools` folder of this repo).
  * eclipse
  * node
  * WinMerge
  * Apache Jena/Fuseki
  * Puzzles
  * jdk
  * netbeans
  * PyScripter for Windows only
  * Yed (can be run with any JRE with `java -jar yed.jar`)
  * Capella for systems engineering tool
  * Simon Tatham's puzzle collection

*(Last update: July 2020)*
