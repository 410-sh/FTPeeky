# FTPeeky

FTPeeky is a lightweight Python script that scans one or more IP addresses for anonymous FTP login access.  
It's designed to fit into recon workflows or work as a standalone tool for network assessments.

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

## Usage Examples

```bash

./ftpeeky.py 192.168.1.1
./ftpeeky.py 192.168.1.0/24 -t 10
./ftpeeky.py targets.txt -c
./ftpeeky.py 10.0.0.1 -t 5 -c
```

