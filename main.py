#!/bin/python3

import sys
from datetime import datetime
from scapy.all import *
import pandas as pd
import numpy as np
import threading

now = datetime.now()


# Open default gateway addr / interface


def arp_scan(ip, gateway):
    #    Performs a network scan by sending ARP requests to an IP address or a range of IP addresses.
    #    Args:
    #         ip (str): An IP address or IP address range to scan. For example:
    #                     - 192.168.1.1 to scan a single IP address
    #                     - 192.168.1.1/24 to scan a range of IP addresses.
    #     Returns:
    #         A list of dictionaries mapping IP addresses to MAC addresses. For example:
    #         [
    #             {'IP': '192.168.2.1', 'MAC': 'c4:93:d9:8b:3e:5a'}
    #         ]

    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
    ans, unans = srp(request, timeout=2, retry=1, verbose=0)
    result = []
    for sent, received in ans:
        if received.psrc != gateway:
            result.append(
                {"IP": received.psrc, "MAC": received.hwsrc, "Discovered on": dt_string}
            )
    return result


def print_table(arg):
    table = pd.DataFrame(arg)
    return table


def store_valid_mac(result_value):
    valid_mac = np.array(result_value["MAC"])
    store_valid_mac = open("white_list/list.txt", "a")
    with open("white_list/list.txt", "r") as v_mac_l:
        valid_mac_array = v_mac_l.read().strip().split("\n")

    # append valid mac addr in a file
    for val in valid_mac:
        # ensure the mac addr are not stored twice
        if val not in valid_mac_array:
            store_valid_mac.write(f"{val}\n")
