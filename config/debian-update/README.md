# README

Make sure you have the NVIDIA driver of your current version of the Linux kernel, let's say version N.

As you will upgrade to version N+1, download the new NVIDIA driver of the version N+1. Make it executable.

Steps :

* su root
* apt all-upgrade ou dist-upgrade
* Install the headers of the new kernel (not installed by default and required by the NVIDIA).
* Remove no package on your previous installation
* Reboot
* Choose to log on in root at startup in non graphical mode in order to install the new NVIDIA driver
* Install it
* Reboot

That should be OK.

In case of trouble, reboot in the previous kernel version N. If the graphical installation did not work, reinstall the previous NVIDIA driver for the previous kernel, reboot on the previous kernel and troubleshoot.

