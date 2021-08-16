# Install wg111v2 driver on Debian

```
$ su root
$ apt install ndiswrapper ndisgtk
$ ndisgtk
```
Click on install new driver and select the right `.inf` file.

Then (still under root):
```
$ emacs /etc/modules
```
Append to the end of the file: `ndiswrapper`

Reboot and retest.

