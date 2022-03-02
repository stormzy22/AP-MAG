#!/bin/bash

router_mac=$(sudo cat _gateway/BSSID.txt)
current_list=$(sudo cat store/txt/file.txt)
interface=$(sudo cat _gateway/IF.txt)


mac=$(echo "$current_list" | head -n1 | cut -d "-" -f1 )
ch=$(echo "$current_list" | head -n1 | cut -d "-" -f2 )
if [ "$mac" == "$router_mac" ]
then
echo "${mac}---------------"
sudo airodump-ng --bssid "$router_mac" -c "$ch" "$interface" --write store/csv/mac
fi
python3 get_host_mac.py