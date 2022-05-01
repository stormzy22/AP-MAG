#!/bin/bash

router_mac=$(sudo cat _gateway/BSSID.txt)
current_list=$(sudo cat store/txt/file.txt)
interface=$(sudo cat _gateway/IF.txt)
ch=$(sudo cat _gateway/CH.txt)

x-terminal-emulator -e sudo airodump-ng --bssid "$router_mac" -c "$ch" "$interface"