#!/bin/python3

from rich import print
from main import get_host, print_RES, save_valid_mac, compare_mac, deauth
import sys
import os
import subprocess
import time


msg = """
    STEP 1:\b
    \tinput [bold green]scan[/bold green] to discover connected devices on your network\b
    STEP 2:\b
    \tinput [bold green]hosts[/bold green] to view connected devices\b
    STEP 3:\b
    \tinput [bold green]save[/bold green] to whitelist the current devices\b
    STEP 4:\b
    \tinput [bold green]check[/bold green] to validate the current devices connected to the access point.
    \t[yellow bold]NOTE:[/yellow bold] The [bold green]check[/bold green] command compares the current devices connected to the access point
    \twith the whitelist then filters the devices that aren't in the whitelist and save them in the blacklist\b
    STEP 5:\b
    \tinput [bold green]deauth[/bold green] to deauthenticate invalid devices\b
    STEP 6:\b
    \tinput [bold green]exit / quit[/bold green] to exit the program and clean files created during the session excluding the whitelist
    STEP 7:\b
    \tinput [bold green]exit -w / quit -w [/bold green] to exit the program and clean files created during the session including the whitelist

"""

print(f"[white]{msg}[/white]")

while True:
    user_input = input("[!] ")
    format_user_input = user_input.strip().lower()
    if format_user_input == "scan":
        get_host()
        print_RES("RES/arp-scan.txt")
        print("[bold blue]NUMBER OF HOST FOUND ↓[/bold blue]")
        os.system("wc -l RES/arp-scan.txt | cut -d ' ' -f1")
        print("\n")
    elif format_user_input == "hosts":
        hosts = print_RES("RES/arp-scan.txt")
        print(f"\n[bold cyan]{hosts}[/bold cyan]\n")
    elif format_user_input == "save":
        print("[bold green] SAVING..... [/bold green]", end="\r")
        save_valid_mac()
        print("[bold green] SAVED ☑️ [/bold green]", end="\r")
        print()
        print("\n")
    elif format_user_input == "check":
        res = compare_mac()
        print(f"\n[bold red]{res} INVALID HOST[/bold red]\n")
    elif format_user_input == "deauth":
        r_txt = deauth()
        print(f"\n\t[bold white]{r_txt}[/bold white]\n")
    elif format_user_input == "clear":
        sys.stderr.write("\x1b[2J\x1b[H")
    elif format_user_input == "exit" or format_user_input == "quit":
        subprocess.call("./clean.sh", shell=True)
        sys.exit()
    elif format_user_input == "exit -w" or format_user_input == "quit -w":
        subprocess.call("./clean_w.sh", shell=True)
        sys.exit()
    else:
        print("[underline red]Invalid input[/underline red]")
