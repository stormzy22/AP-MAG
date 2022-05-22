#/bin/bash

interface=$(cat ROUTER/IF.txt)
sudo arp-scan --localnet -I "$interface" -x > RES/arp-scan.txt