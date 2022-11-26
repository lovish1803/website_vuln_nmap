#!/usr/bin/env python

import subprocess

target = input("enter the target host: ")

def vuln_scan(t):
    subprocess.call(["sudo", "nmap", "--script", "vuln", t])

vuln_scan(target)

