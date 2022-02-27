#!/bin/python3
import sys
import os
from colorama import Fore, Style
import numpy as np
from main import arp_scan, print_table, store_valid_mac
from deauthenticator import deauth

# If not sudo, don't allow to continue
if not "SUDO_UID" in os.environ.keys():
    print(
        f"[{Fore.RED}!{Style.RESET_ALL}] Permission error: {Fore.RED}You need root privileges for this feature.{Style.RESET_ALL}"
    )
    sys.exit()

# Open default gateway addr / interface
with open("_gateway/IP.txt", "r") as g_ip, open("_gateway/MAC.txt", "r") as d_mac, open(
    "_gateway/IP.txt", "r"
) as i_face:
    gateway = g_ip.read().strip()
    g_way = gateway.split(".")[:-1]
    ips = ".".join(g_way) + ".0/24"
    router_mac = d_mac.read().strip()
    interface = i_face.read().strip()
###

err1 = "You have 0 host pls run the scan command"
result = []
ans = []
while True:
    collect_input = input(">>> ")

    if collect_input.strip().lower() == "scan":
        print("scanning.....")
        dic_array = arp_scan(ips, gateway)
        result = dic_array
        print(str(len(result)) + " hosts found")

    elif collect_input.strip().lower() == "hosts":

        if len(result) == 0:
            print(err1)
        else:
            ans = print_table(result)
            store_valid_mac(ans)
            print(ans)

    elif collect_input.strip().lower() == "clear":
        sys.stderr.write("\x1b[2J\x1b[H")

    elif collect_input.strip().lower() == "deauth":
        if len(result) == 0:
            print(err1)
        else:
            with open("white_list/list.txt", "r") as macs:
                get_valid_mac = macs.read().strip().split("\n")
                # loop through the current mac
                current_mac = [str(i["MAC"]).strip() for i in result]
                print(current_mac)
                for mac_addr in current_mac:
                    if (mac_addr not in get_valid_mac) and (mac_addr != router_mac):
                        print(f"{router_mac} gateway mac")
                        print(f"{mac_addr} not among the whitelist")
                        print("starting deauth.")
                        deauth(interface, mac_addr, router_mac)

    elif collect_input.strip().lower() == "quit":
        sys.exit()

    else:
        print("Invalid input")
