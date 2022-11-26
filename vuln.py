#!/usr/bin/env python
import subprocess

target = input("enter the target host: ")
print("Performing the scan... Please wait...")

def vuln_scan(t):
    subprocess.call(["sudo", "nmap", "--script", "vuln", t], stderr=subprocess.DEVNULL)

def fetch_fun(test_str):
    print(".\n.\n.\n.\n.\n.\n.\n.")
    print("The scan is complete...")
    str_lst = test_str.split(" ")
    res = ""
    for word in str_lst:
        if (word == "VULNERABLE:\n|"):

            res = str_lst[str_lst.index(word) + 3] + " attack is possible!"
            print(res)

test_str = str(vuln_scan(target))
fetch_fun(test_str)
