#!/bin/sh
# To be run in root mode 
echo "install algif_aead /bin/false" > /etc/modprobe.d/disable-algif.conf
rmmod algif_aead
