#!/usr/bin/env python3

import ftplib
import argparse
import ipaddress
import sys
#import time
from rich.progress import track


def parseTargets(targetInput):
    targets = []

    # check if file
    try:
        with open (targetInput, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):  # Skip empty lines and comments
                    # check if line is CIDR
                    if '/' in line:
                        targets.extend([str(ip) for ip in ipaddress.ip_network(line, strict=False)])
                    else:
                        targets.append(line)
            return targets
    except FileNotFoundError:
        pass  # not a file, continue to others

    # check if input is CIDR
    if '/' in targetInput:
        try:
            network = ipaddress.ip_network(targetInput, strict=False)
            return [str(ip) for ip in network]
        except ValueError as e:
            print(f"Error: Invalid CIDR notation - {e}")
            sys.exit(1)
    
    # otherwise, assume single IP
    try:
        # Validate it's a proper IP
        ipaddress.ip_address(targetInput)
        return [targetInput]
    except ValueError:
        print(f"Error: '{targetInput}' is not a valid IP address, file, or CIDR range")
        sys.exit(1)


def tryLogin(target,timeoutValue,contentsValue):
    successList = []

    try:
        ftp = ftplib.FTP(target, timeout=timeoutValue)
        ftp.login('anonymous', '')
        print(f'{target} anonymous login \033[92msuccess\033[0m')

        if contentsValue:
            files = []
            print(f"\nDirectory lisiting for {target}:")
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
               # successList.append(target)
        return target
        
    except Exception:
        pass
            #print(f'{target} anonymous login failed')

    #if successList:
     #   with open('successful_anon_ftp.txt', 'w') as outFile:
      #      for ip in successList:
       #         outFile.write(ip + '\n')
        #print(f'[+] Saved successful logins to successful_anon_ftp.txt')

if __name__ == "__main__":
        parser = argparse.ArgumentParser(
        description='FTPeeky - FTP Enumeration Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
   ./ftpeeky.py 192.168.1.1
   ./ftpeeky.py 192.168.1.0/24 -t 10
   ./ftpeeky.py targets.txt -c
   ./ftpeeky.py 10.0.0.1 -t 5 -c
        '''
    )

        parser.add_argument('target',help='Single IP, file containing IPs, or CIDR range')
        parser.add_argument('-t', '--timeout',type=int,default=5,help='Connection timeout in seconds (default: 5)')
        parser.add_argument('-c', '--contents',action='store_true',help='View file contents')

        args = parser.parse_args()
        
        targets = parseTargets(args.target)

        print(f"[*] Scanning {len(targets)} target(s)...")
    
        successList = []
        for target in track(targets,description="Scanning"):
                result = tryLogin(target,args.timeout,args.contents)
                if result:
                    successList.append(result)

        if successList:
            with open('successful_anon_ftp.txt', 'w') as outFile:
                for ip in successList:
                    outFile.write(ip + '\n')
            print(f'[+] Saved successful logins to successful_anon_ftp.txt')
