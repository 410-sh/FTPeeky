#!/usr/bin/env python3

import ftplib
import argparse

def tryLogin(hostsFile):
    ipList = []
    successList = []

    with open(hostsFile, 'r') as file:
        for line in file:
            ip = line.strip()
            if ip:
                ipList.append(ip)

    for ipAddr in ipList:
        try:
            ftp = ftplib.FTP(ipAddr, timeout=5)
            ftp.login('anonymous', '')
            print(f'{ipAddr} anonymous login \033[92msuccess\033[0m')
            ftp.quit()
            successList.append(ipAddr)
        except Exception:
            print(f'{ipAddr} anonymous login failed')

    if successList:
        with open('successful_anon_ftp.txt', 'w') as outFile:
            for ip in successList:
                outFile.write(ip + '\n')
        print(f'[+] Saved successful logins to successful_anon_ftp.txt')

try:
    parser = argparse.ArgumentParser(description='Anonymous FTP scanner')
    parser.add_argument("-i", type=str, help="Single IP to scan")
    parser.add_argument("-l", type=str, help="List of IPs to scan")
    options = parser.parse_args()

    if options.i:
        ipAddr = options.i
        try:
            ftp = ftplib.FTP(ipAddr, timeout=5)
            ftp.login('anonymous', '')
            print(f'{ipAddr} anonymous login \033[92msuccess\033[0m')
            ftp.quit()
        except Exception:
            print(f'{ipAddr} anonymous login failed')

    elif options.l:
        tryLogin(options.l)

    else:
        parser.error("No arguments provided. Use -i for a single IP or -l for a list.")

except KeyboardInterrupt:
    print("\nStopped by user.")
