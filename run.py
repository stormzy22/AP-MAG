#!/bin/python3

from rich import print
from main import get_host, print_result, save_valid_mac, compare_mac, deauth
import sys
import os
import subprocess
import time


msg = """
    [[red]![/red]] input [bold red]scan[/bold red] to discover connected devices on your network
    [[red]![/red]] input [bold red]hosts[/bold red] to view connected devices
    [[red]![/red]] input [bold red]save[/bold red] to whitelist the current devices
    [[red]![/red]] restart the program i.e input [bold red]exit[/bold red]/[bold red]quit[/bold red] then input [bold red]./run.sh[/bold red]
    [[red]![/red]] input [bold red]scan[/bold red] to discover connected devices on your network
    [[red]![/red]] input [bold red]check[/bold red] to validate current devices
    [[red]![/red]] input [bold red]deauth[/bold red] to deauthenticate invalid devices
"""

print(f"[bold green]{msg}[/bold green]")

while True:
    user_input = input("[!] ")
    format_user_input = user_input.strip().lower()
    if format_user_input == "scan":
        get_host()
        print_result("result/arp-scan.txt")
        print("[bold blue]NUMBER OF HOST FOUND ↓[/bold blue]")
        os.system("wc -l result/arp-scan.txt | cut -d ' ' -f1")
        print("\n")
    elif format_user_input == "hosts":
        hosts = print_result("result/arp-scan.txt")
        print(f"\n\t[bold cyan]{hosts}[/bold cyan]\n")
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
        subprocess.call("./clear.sh", shell=True)
        sys.exit()
    elif format_user_input == "exit -w" or format_user_input == "quit -w":
        subprocess.call("./clear_white_list.sh", shell=True)
        sys.exit()
    else:
        print("[underline red]Invalid input[/underline red]")
