# FTPeeky

FTPeeky is a lightweight Python script that scans one or more IP addresses for anonymous FTP login access.  
It's designed to fit into recon workflows or work as a standalone tool for quick assessments.

---

## Features

- Checks for anonymous FTP login access
- Accepts a single IP or a list of IPs from a file
- Saves successful logins to `successful_anon_ftp.txt` when scanning from a list

---

## Requirements

- Python 3.x

---

## Usage

```bash
# Scan a single IP address
python3 ftpeeky.py -i 192.168.1.100

# Scan a list of IPs from a file
python3 ftpeeky.py -l targets.txt
