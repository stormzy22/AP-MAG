#!/bin/bash

interface_path="_gateway/IF.txt"
interface=$(cat $interface_path)

if [ "${#interface}" -ne "0" ];then
sudo arp-scan --localnet -I "$interface" -x > result/arp-scan.txt
echo -ne "\e[37m\e[42m\e[1m DONE \e[0m" "<" $(for i in $(seq 1 `expr $(tput cols) / 2`); do printf "="; done)"\r\n"
else
echo "CAN'T FIND INTERFACE"
echo "EXITING PROGRAM"
fi


