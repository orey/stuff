## Lynx basic configuration

3 files are necessary to configure lynx:

  * .lynxrc
  * lynx.lss
  * lynx_bookmarks.html

### .lynxrc

The `.lynxrc` file enables to override certain commands permanetly such as lynx asking for cookie acceptance.

To be placed in the ~ directory.

### lynx.lss file

I searched for a while to have lynx finding the file by itself but I did not succeed (while I remember doing it in the past).

To be placed in the ~ directory and to be invoked in command line with the `-lss` option:

```
$ lynx -lss lynx.lss
```

Or use the basic shell script attached.

### Bookmarks

The file `lynx_bookmarks.html` is located in the ~ folder and seems to be found automatically by lynx (which is not the case for `lynx.lss`).

It can be edited manually.

### lynx.cfg

I did not have to customize this one.

## Lynx basic commands

  * `v`: go to bookmark page
  * `g`: type URL
  * `a`: bookmark the current link
  * `d`: download the current file

Good online help, but to see it, you need to have multiple lynx windows.
