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


    