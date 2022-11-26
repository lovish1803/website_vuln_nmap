#!/usr/bin/env python

test_string = """Starting Nmap 7.91 ( https://nmap.org ) at 2022-11-18 21:57 IST
Pre-scan script results:
| broadcast-avahi-dos: 
|   Discovered hosts:
|     224.0.0.251
|   After NULL UDP avahi packet DoS (CVE-2011-1002).
|_  Hosts are all up (not vulnerable).
Nmap scan report for 14.141.113.35.static-Delhi.vsnl.net.in (14.141.113.35)
Host is up (0.00028s latency).
Not shown: 991 closed ports
PORT     STATE SERVICE
21/tcp   open  ftp
|_sslv2-drown: 
25/tcp   open  smtp
|_sslv2-drown: 
80/tcp   open  http
|_http-aspnet-debug: ERROR: Script execution failed (use -d to debug)
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-vuln-cve2014-3704: ERROR: Script execution failed (use -d to debug)
110/tcp  open  pop3
|_sslv2-drown: 
143/tcp  open  imap
|_sslv2-drown: 
443/tcp  open  https
| http-aspnet-debug: 
|_  status: DEBUG is enabled
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-enum: 
|_  /admin/: Possible admin folder
| http-slowloris-check: 
|   VULNERABLE:
|   Slowloris DOS attack
|     State: LIKELY VULNERABLE
|     IDs:  CVE:CVE-2007-6750
|       Slowloris tries to keep many connections to the target web server open and hold
|       them open as long as possible.  It accomplishes this by opening connections to
|       the target web server and sending a partial request. By doing so, it starves
|       the http server's resources causing Denial Of Service.
|       
|     Disclosure date: 2009-09-17
|     References:
|       http://ha.ckers.org/slowloris/
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-6750
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_sslv2-drown: 
445/tcp  open  microsoft-ds
5060/tcp open  sip
8008/tcp open  http
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-vuln-cve2014-3704: ERROR: Script execution failed (use -d to debug)

Host script results:
|_samba-vuln-cve-2012-1182: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR
|_smb-vuln-ms10-054: false
|_smb-vuln-ms10-061: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR

Nmap done: 1 IP address (1 host up) scanned in 1120.76 seconds
root@kali:~# sudo nmap --script vuln www.bennett.edu.in
Starting Nmap 7.91 ( https://nmap.org ) at 2022-11-18 22:21 IST
Pre-scan script results:
| broadcast-avahi-dos: 
|   Discovered hosts:
|     224.0.0.251
|   After NULL UDP avahi packet DoS (CVE-2011-1002).
|_  Hosts are all up (not vulnerable).
Stats: 0:04:05 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 97.98% done; ETC: 22:25 (0:00:04 remaining)
Stats: 0:04:05 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 97.98% done; ETC: 22:25 (0:00:04 remaining)
Stats: 0:04:10 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 97.98% done; ETC: 22:25 (0:00:04 remaining)
Stats: 0:04:11 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 97.98% done; ETC: 22:25 (0:00:04 remaining)
Stats: 0:04:12 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 97.98% done; ETC: 22:25 (0:00:04 remaining)
"""

def fetch_fun(test_str):
    print(".\n.\n.\n.\n.\n.\n.\n.")
    print("The scan is complete...")
    str_lst = test_str.split(" ")
    res = ""
    for word in str_lst:
        if (word == "VULNERABLE:\n|"):

            res = str_lst[str_lst.index(word) + 3] + " attack is possible!"
            print(res)


# str_lst = test_string.split(" ")
# print(str_lst)
# res=""
# for word in str_lst:
#     if(word=="VULNERABLE:\n|"):
#         res = str_lst[str_lst.index(word)+3]+" attack is possible!"
#         print(res)

fetch_fun(test_str=test_string)