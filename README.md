# IoT Security: Safeguarding the Connected World

## Overview
This project involves the development of a Python-based penetration testing tool for IoT devices, focusing on protocols such as CoAP, UPnP/SSDP, and MQTT. The tool aims to identify vulnerabilities and weaknesses in these protocols, enabling security professionals to effectively test the security of IoT devices. By detecting and addressing potential vulnerabilities, the tool contributes to enhancing the overall security and resilience of IoT ecosystems.

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

2. Invoke the main.py
   ```
   python3 main.py

### POC
For testing puprose, I have simulated the IOT device with all three type of protocols
![MainPy (1)](https://github.com/user-attachments/assets/0de83d0f-f516-46be-a4c6-1388e71c067d)
![Network_TargetPy (1)](https://github.com/user-attachments/assets/8b0d5d84-2b88-4918-813a-60b8fd5753c3)
![AttackPy (1)](https://github.com/user-attachments/assets/6f7b4759-fe1d-441d-8708-b163b0d6efc8)
![UPnP (1)](https://github.com/user-attachments/assets/663ad921-49b8-428f-938a-cad581fb6902)
![MQTT5 (1)](https://github.com/user-attachments/assets/b0532541-e596-4c5e-a106-2641178cbfb2)
![MQTT4 (2)](https://github.com/user-attachments/assets/520a42bc-adf6-4130-80a2-f4164db4dfd6)
![MQTT4 (1)](https://github.com/user-attachments/assets/4d31b466-77b5-4d09-9827-d3daa49a8838)
![MQTT3 (2)](https://github.com/user-attachments/assets/e201eff5-7ea8-4d1e-a1d6-cdce3ba79d97)
![MQTT3 (1)](https://github.com/user-attachments/assets/7fa0e40e-aa0a-4b7a-989b-2b42fe6d92ae)
![MQTT2 (2)](https://github.com/user-attachments/assets/4a78c65d-912f-45c9-9f1b-5153de52b72d)
![MQTT2 (1)](https://github.com/user-attachments/assets/79c12169-ce99-44be-bb32-15e9d05c1522)
![MQTT1 (2)](https://github.com/user-attachments/assets/b2846254-8444-4131-9733-a3f14476c939)
![MQTT1 (1)](https://github.com/user-attachments/assets/26681e27-09d7-4e2d-afe5-edd0cebafcba)
![MQTT (1)](https://github.com/user-attachments/assets/278122bf-e85b-40a1-8d5b-329a832722e2)
![CoAP (1)](https://github.com/user-attachments/assets/2c16d351-7635-4077-be24-c02e70f06568)


