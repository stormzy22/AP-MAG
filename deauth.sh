#!/bin/bash

router_mac=$(cat _gateway/MAC.txt)
interface=$(cat _gateway/IF.txt)

sudo ifconfig "$interface" down
sudo airmon-ng check kill
sudo iwconfig "$interface" mode monitor
sudo ifconfig "$interface" up
sudo airodump-ng "$interface" --write store/CH
sudo airodump-ng --bssid "$router_mac" -c "$1" "$interface"
sudo service NetworkManager restart
