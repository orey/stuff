# README

Get the keys for the packages signature. As `root`:

```
root@workstation:# wget -q http://build.openmodelica.org/apt/openmodelica.asc -O- | apt-key add - 
root@workstation:# apt-key fingerprint
```

On Debian 10, add the following line to your `sources.list`:

```
root@workstation:# deb https://build.openmodelica.org/omc/builds/linux/releases/1.14.1/ buster release
```

Then, update and install:

```
root@workstation:# apt update
root@workstation:# apt install openmodelica

```

