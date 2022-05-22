#!/bin/bash

router_mac=$(sudo cat ROUTER/BSSID.txt)
interface=$(sudo cat ROUTER/IF.txt)
ch=$(sudo cat ROUTER/CH.txt)

x-terminal-emulator -e sudo airodump-ng --bssid "$router_mac" -c "$ch" "$interface"
