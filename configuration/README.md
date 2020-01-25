# Tips for running development tools in professional environment

## Portable versions

Prefer portable versions. Use ```.bat``` scripts to include the various binaries.

```
set PATH="C:\Tools\MyPath":%PATH
```

Command lines: Many tools can be run provided there is a JRE in the path. Some may have a untrivial launching commands. See [here](https://github.com/orey/stuff/tree/master/Configuration-Windows/CommandLineNoInstall) for sample of portable tools.

## Important tools

Here is a list of important tools and tricks to install the portable versions:

  * Cntlm
    * In case of "Couldn't compute FAST_CWD pointer", please check your ini file is in ISO format (and not UTF-8)
  * DoubleCommander

### Git

Use the portable version. Declare the firewall option:

```
git config --global http.proxy http://user:password@firewal.com:8080
```

If your firewall is using a certificate that is internally signed, Git may complain like ```SSL Certificate problem: unable to get local issuer```. Try this.

```
git config --global http.sslVerify false
```

Good page to browse: https://confluence.atlassian.com/bitbucketserverkb/ssl-certificate-problem-unable-to-get-local-issuer-certificate-816521128.html

See also the [recipe](https://github.com/orey/stuff/tree/master/Configuration-Windows/Recipes) page.

### Miktex

Use the portable version. To set the firewall, set the following variable:

```
set ALL_PROXY="http://user:pasword@firewall.com:8080"
```

### TexStudio

Could be useful add the path to Miktex in the PATH (generally in install/miktex/bin).

### Python (native Windows)

1. You can download the zip version and put it in a directory.

2. Then, set the environment variables as shown in the `Python\setenv.bat` file.

3. Download `get-pip.py` on the Pypy site and run `python get-pip.py`. This will install pip.

4. Then, modify the `python37._pth` path accordingly to the `Python\python37._pth` file to enable pip to work.

5. Install modules with `pip install module`.

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

Some packages don't work with Cygwin, for instance the `mss` package. Choose to use a local python install.

## Archi

  * See the batch into the Archi folder to include a certificate inside the embedded Archi JRE.
  * Archi may use the `.gitconfig` file option, especially the `SSLVerify=False` that can be useful for the collaboration plugin of Archi.

## Extended list of useful softwares that can be installed without admin rights

### General tools

  * cygwin
  * cntlm => proxy
  * DoubleCommander
  * Emacs
  * FreeFileSync
  * Git
  * innoump => to unpack installations
  * Zim

### Latex

  * MikTek
  * Texstudio

### Dev

  * eclipse
  * node
  * WinMerge
  * Apache Jena/Fuseki
  * Puzzles

### Java

  * jdk
  * netbeans

### Python

  * PyScripter for Windows only
  
### Architecture tools
  
  * Archi
  * Yed
  
### Systems engineering tools

  * Capella
  
### Specific software
  
  * Apache Jena
  * Fuseki

### Puzzles

  * Simon Tatham's puzzle collection

