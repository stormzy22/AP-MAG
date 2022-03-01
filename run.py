#!/bin/python3

from rich import print
from main import get_host, print_result, save_valid_mac, compare_mac, deauth
import sys
import os

while True:
    ci = input("[!] ")
    fci = ci.strip().lower()
    if fci == "scan":
        get_host()
        print_result("result/arp-scan.txt")
        print("[blue]No of host found ↓[/blue]")
        os.system("wc -l result/arp-scan.txt | cut -d ' ' -f1")
        msg = """
        Done
        Enter hosts to see all hosts on your network
        """
        print(f"[bold green]{msg}[/bold green]")
        print("[bold purple]-[/bold purple]" * 50)
    elif fci == "hosts":
        hosts = print_result("result/arp-scan.txt")
        print(f"[bold cyan]{hosts}[/bold cyan]")
    elif fci == "save":
        save_valid_mac()
        print("[bold green] saved [/bold green]")
    elif fci == "check":
        res = compare_mac()
        print(f"[bold red]{res} invalid host[/bold red]")
    elif fci == "deauth":
        deauth()
    elif fci == "clear":
        sys.stderr.write("\x1b[2J\x1b[H")
    elif fci == "exit" or fci == "quit":
        sys.exit()
    else:
        print("[underline red]Invalid input[/underline red]")
