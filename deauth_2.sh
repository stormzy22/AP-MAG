#!/bin/bash

router_mac=$(sudo cat _gateway/BSSID.txt)
interface=$(sudo cat _gateway/IF.txt)
ch=$(sudo cat _gateway/CH.txt)

x-terminal-emulator -e sudo airodump-ng --bssid "$router_mac" -c "$ch" "$interface"