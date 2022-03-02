#!/bin/bash

get_router_ip () {
    router_ip=$(netstat -nr | awk '$1 == "0.0.0.0"{print$2}')
    router_mac=$(ip neigh|grep "$(ip -4 route list 0/0|head -1|cut -d' ' -f3) "|cut -d' ' -f5|tr '[a-f]' '[A-F]')
    interface=$(ip route get 8.8.8.8 | grep -oP 'dev \K[^ ]+')
    bssid=$(iwconfig "$interface" | sed -n 's/.*Access Point: \([0-9\:A-F]\{17\}\).*/\1/p')
    if [ "$router_ip" != "" ] || [ "$router_mac" != "" ] || [ "$ssid" != "" ]
    then
    echo "$router_ip" > _gateway/IP.txt && echo "$router_mac" > _gateway/MAC.txt && echo "$interface" > _gateway/IF.txt && echo "$bssid" > _gateway/BSSID.txt 
    else
    echo -e "\e[31mPls connect to a router\e[0m"
    exit
    fi 
}
get_router_ip

logo=$(figlet Network-Scan)
echo -e "\e[1m\e[32m$logo\e[0m"

sudo python3 run.py