# Scanner_Assignment
# 🚀 Network Scanning Automation (Cybersecurity Assignment)

## 📌 Project Overview

This project automates essential network reconnaissance tasks using Python. It includes implementations of **Ping Scanner**, **ARP Scanner**, and **Nmap Scanner**, along with an advanced **Unified Network Scanner** that integrates all functionalities.
The project demonstrates practical cybersecurity concepts such as host discovery, network mapping, port scanning, and automation using Python.

## Objectives

* Automate network scanning tools using Python
* Understand host discovery and network reconnaissance
* Parse command-line outputs using Python
* Implement modular and reusable code
* Enhance performance using advanced features (bonus)

## Technologies Used

* Python 3.x
* Nmap
* VS Code / Command Prompt
* Windows OS

## Installation Guide

### 1. Install Python

Download Python from:
https://www.python.org/downloads/

### 2. Install Nmap

Download from:
https://nmap.org/download.html

✔ Install using Windows `.exe` installer
✔ Npcap will be installed automatically

### 3. Verify Installation

```bash
python --version
nmap --version
```

## Project Structure

```
network-scanning-tools/
│
├── ping_scanner.py          # Ping automation
├── arp_scanner.py           # ARP table scanner
├── nmap_scanner.py          # Nmap automation
├── network_scanner.py       # Unified scanner (BONUS)
├── output.csv               # Exported ARP data (BONUS)
├── scan_log.txt             # Log file (BONUS)
├── README.md
└── screenshots/
```

## How to Run

### ▶️ Ping Scanner

```bash
python ping_scanner.py
```

### ▶️ ARP Scanner

```bash
python arp_scanner.py
```

### ▶️ Nmap Scanner

```bash
python nmap_scanner.py
```

### 🔥 Unified Network Scanner (BONUS)

```bash
python network_scanner.py
```

**Features:**

* Ping scanning
* ARP scanning
* Nmap scanning
* Network range scanning
* CSV export
* Logging
* Multi-threading

### GUI Scanner (BONUS)

```bash
python gui_scanner.py
```

## Screenshots

Screenshots of program outputs are available in the `screenshots/` folder:

* ping_output.png
* arp_output.png
* nmap_output.png
* networkoutput1.png
* networkoutput2.png
* networkoutput3.png
* networkoutput4.png and networkoutput4.1)

## Features Implemented

### Core Features

* Ping automation using subprocess
* ARP table extraction and parsing
* Nmap scanning with multiple options
* Cross-platform compatibility
* Error handling

### Bonus Features

* Unified scanner combining all tools
* CSV export of ARP results
* Network range scanning
* Multi-threaded scanning for faster execution
* Logging functionality (scan_log.txt)
* Simple GUI using Tkinter

## Ethical Considerations

This project is developed strictly for educational purposes.
All scans were performed only on:

* Localhost (127.0.0.1)
* Private network

Unauthorized scanning of external systems is strictly avoided.

## Learning Outcomes

* Understanding of network scanning techniques
* Practical usage of cybersecurity tools
* Automation using Python subprocess
* Parsing outputs using regular expressions
* Implementation of advanced programming concepts

## Conclusion

This project successfully demonstrates automation of network scanning tools and provides a strong foundation in cybersecurity practices. The inclusion of advanced features enhances usability and performance.

**Name:** Divyashree N
**Course:** Cybersecurity and Ethical Hacking
**Institution:** CampusPe Edufu private limited
