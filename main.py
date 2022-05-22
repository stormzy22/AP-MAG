#!/bin/python3
import pandas as pd
import subprocess
import numpy as np
from rich import print
from pathlib import Path


def get_host():
    subprocess.call("./scanner.sh", shell=True)


def print_RES(path):
    res = pd.read_table(path, delimiter="\t", header=None, names=["IP", "MAC", "NAME"])
    return res


def save_valid_mac():

    with open("store/white_list/list.txt", "r") as f1:
        stored_mac = f1.read().strip().split()
    file = open("store/white_list/list.txt", "a")
    res = print_RES("RES/arp-scan.txt")
    valid_mac = np.array(res["MAC"].unique())
    if len(valid_mac) == 0:
        print("[red bold]Pls run the scan command[/red bold]")
    else:
        for val in valid_mac:
            if val not in stored_mac:
                file.write(f"{val}\n")


def append_to_blacklist(mac):
    storeINVALID = open("store/black_list/file.txt", "a")
    with open("store/black_list/file.txt", "r") as f1:
        bl_store = f1.read().strip().split()
    [storeINVALID.write(f"{i}\n") for i in mac if i not in bl_store]


def compare_mac():
    subprocess.call("./check-scanner.sh", shell=True)
    invalid_mac = []
    with open("store/white_list/list.txt", "r") as f1:
        w_list = f1.read().strip().split()
    res = print_RES("RES/arp-scan.txt")
    mac = np.array(res["MAC"].unique())
    for i in mac:
        if i not in w_list and i not in invalid_mac:
            invalid_mac.append(i)
    append_to_blacklist(invalid_mac)
    with open("store/black_list/file.txt", "r") as f2:
        b_list = f2.read().split()
    return len(b_list)


def deauth():
    err_msg = "\tTHERE IS NO BLACKLIST AVAILABLE TO DISPLAY, RUN THE CHECK"
    pathtoblacklist = "store/black_list/file.txt"
    path = Path(pathtoblacklist)
    if not path.is_file():
        return err_msg
    else:
        subprocess.call("./deauth.sh", shell=True)
        return "DEAUTHING........."
