#!/usr/bin/env python3

import ftplib
import argparse

def displayBanner():
    bannerText = r'''
__/\\\\\\\\\\\\\__/\\\\\\\\\\\\\___/\\\\\\\\\\\\\__________________________________________________________
 _\/\\\/////////__\/////\\\/////___\/\\\/////////\\\_____________________________/\\\_______________________
  _\/\\\________________\/\\\_______\/\\\_______\/\\\____________________________\/\\\____________/\\\__/\\\_
   _\/\\\\\\\\\__________\/\\\_______\/\\\\\\\\\\\\\/___/\\\\\\\\______/\\\\\\\\__\/\\\\\\\\______\//\\\/\\\__
    _\/\\\/////___________\/\\\_______\/\\\/////////___/\\\/////\\\___/\\\/////\\\_\/\\\////\\\_____\//\\\\\___
     _\/\\\________________\/\\\_______\/\\\___________/\\\\\\\\\\\___/\\\\\\\\\\\__\/\\\\\\\\/_______\//\\\____
      _\/\\\________________\/\\\_______\/\\\__________\//\\///////___\//\\///////___\/\\\///\\\____/\\_/\\\_____
       _\/\\\________________\/\\\_______\/\\\___________\//\\\\\\\\\\__\//\\\\\\\\\\_\/\\\_\///\\\_\//\\\\/______
        _\///_________________\///________\///_____________\//////////____\//////////__\///____\///___\////________
        '''
    print(bannerText)


def tryLogin(hostsFile,timeoutValue,contentsValue):
    displayBanner()
    ipList = []
    successList = []

    with open(hostsFile, 'r') as file:
        for line in file:
            ip = line.strip()
            if ip:
                ipList.append(ip)

    for ipAddr in ipList:
        try:
            ftp = ftplib.FTP(ipAddr, timeout=timeoutValue)
            ftp.login('anonymous', '')
            print(f'{ipAddr} anonymous login \033[92msuccess\033[0m')
            
            if contentsValue:
                files = []
                print(f"\nDirectory lisiting for {ipAddr}:")
                try:
                    files = ftp.nlst()
                except ftplib.error_perm as resp:
                    if str(resp) == "550 No files found":
                        print("No files in this directory")
                    else:
                        raise
        
                for f in files:
                    print(f)
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
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-i", type=str, help="Single IP to scan")
    group.add_argument("-l", type=str, help="List of IPs to scan")
    parser.add_argument("-t", type=int, default=5, help="Timeout in seconds (default 5)")
    parser.add_argument("-c", action='store_true', help="List contents in root directory of server")
    options = parser.parse_args()
    timeoutValue = options.t

    if options.i:
        displayBanner()
        ipAddr = options.i
        try:
            ftp = ftplib.FTP(ipAddr, timeout=timeoutValue)
            ftp.login('anonymous', '')
            print(f'{ipAddr} anonymous login \033[92msuccess\033[0m')
            
            if options.c:
                files = []
                print(f"\nDirectory lisiting for {ipAddr}:")
                try:
                    files = ftp.nlst()
                except ftplib.error_perm as resp:
                    if str(resp) == "550 No files found":
                        print("No files in this directory")
                    else:
                        raise
            
                for f in files:
                    print(f)

            ftp.quit()
        except Exception:
            print(f'{ipAddr} anonymous login failed')

    elif options.l:
        tryLogin(options.l,timeoutValue,options.c)


except KeyboardInterrupt:
    print("\nStopped by user.")
