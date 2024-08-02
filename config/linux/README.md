# Useful tips for Debian

## Create a bootable USB key with an ISO file

First, connect as `root`:

    $ su root
    $ lsblk

List the devices to address the proper one.

    $ umount /dev/sbd1
    $ dd bs=4M if=/path/to/file.iso of=/dev/sdb status=progress oflag=sync

Warning: To create a bootable USB key, you have to target /dev/**sdb** and not /dev/**sdb1**

## Partition configuration Debian

Disks:

  * /dev/sda: 1 Tb
  * /dev/sdb: 32 Gb Flash

This configuration seems to be nice:

  * /dev/sda
    * Boot partition UEFI 5 Gb
    * Data ext4: 995 Gb
  * /dev/sdb
    * swap: 32 Gb

## Backlight

To set backlight(in administrative mode)

    $ echo 4882 > /sys/class/backlight/intel_backlight/brightness

## DNS issue with Debian

### Check the hostname

In a console, type:
```
$ hostname
```

to determine your hostname.

```
debian
```

### DNS resolv.conf

In some installations, the ```/etc/resolv.conf``` file can use the "domain" provided in the installation like that:

```
mydomain
search:mydomain
```

This file can be overriden and so any direct modification is useless.

First, install the ```resolvconf``` package. Then, edit the ```/etc/resolvconf/resolv.conf.d/head``` with the following names:

```
# Address of the box
192.168.1.1
# Google DNS names
8.8.8.8
8.8.8.4
```

Then run ```resolvconf -u``` to update the resolv.conf file.

### Check also your "hosts" file

Located in ```/etc/hosts```, your file may contain:

```
192.168.1.1  box
127.0.0.1    localhost
127.0.0.1    debian.home debian

```

## Global zoom for LXDE

Create a `.Xresources` file in the home diretory and type:

```
Xft.dpi: 80
```

100 is the standard value. 200 will zoom all graphical controls, and 80 will reduce everything.

## Name a terminal

Put that command in the `.bashrc`.


```
termtitle() { printf "\033]0;$*\007"; }
```