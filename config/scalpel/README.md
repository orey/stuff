# Scalpel to recover files accidently removed with "rm"

## Intro

Scalpel is a great tool that is not well known. It does not need complex unmounting partitions efforts or huge partition copies (warning about using ```testdisk``` that can fill your drive completely).

## Install

```
$ su root
# apt install scalpel
```

## Configuration file

See in the folder.

```
# TAB fileextension TAB y TAB filesize TAB firstcharsofthefile
    js    y     100000   /***********
```

It is crucial to provide the first chars of the files to be recovered and to provide a size that can contain the file you just deleted (because if the size is too small, you will end up having just a part of the file).

## Command line

Use your partition

```
$ su root
# scalpel /dev/sda2 -o /home/foo/an_empty_folder/
```

