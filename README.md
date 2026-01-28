# FTPeeky

FTPeeky is a lightweight Python script that scans one or more IP addresses for anonymous FTP login access.  
It's designed to fit into recon workflows or work as a standalone tool for quick assessments.

---

## Features

- Checks for anonymous FTP login access
- Accepts a single IP or a list of IPs from a file
- Saves successful logins to `successful_anon_ftp.txt` when scanning from a list
- Can pick a custom timeout. Default is set to 5 seconds, however, you may want to lower this threshold when working with a large target list
- When using the -c flag, the contents of the root directory will display in the terminal. That is not yet included in the saved file but is planned for the future.

---

## Requirements

- Python 3.x

---

## Usage

```bash
./ftpeeky.py -i [IP Address]
./ftpeeky.py -l [IP Address List] 

Options:
  -h, --help show this help message and exit
  -i         Single IP to scan
  -l         List of IPs to scan
  -t         Timeout in seconds (default 5)
  -c         List contents in root directory of server

Examples:
./ftpeeky.py -i 192.168.1.5
./ftpeeky.py -l iplist.lst -c -t 2
```

