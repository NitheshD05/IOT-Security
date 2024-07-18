# IoT Security Testing Tool

## Overview
This repository contains scripts for an IoT Security Testing Tool. The tool is designed to assist in network scanning, targeting specific networks, and detecting IoT protocols.

## Features
- **Network Scanning:** Switch interface to monitor mode and perform network scans using tools like airodump-ng.
- **Target Network:** Allows targeting specific networks by providing BSSID and channel details.
- **Attacks:** Provides a menu to explore different attack protocols related to IoT.
- **Detection of IoT Protocols:** Scans for MQTT, CoAP, and UPnP/SSDP protocols within a specified network.

## Prerequisites
- Python 3.x
- Required Python packages (install using `pip install -r requirements.txt`)

## Usage
### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/NitheshD05/IOT-Security.git
   cd IoT-Security
   pip install -r requirements.txt
   python3 Main.py
```

