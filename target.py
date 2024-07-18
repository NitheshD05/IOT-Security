#!/usr/bin/env python3

import os
import subprocess

def is_tool_installed(name):
    """Check whether `name` is on PATH and marked as executable."""
    return subprocess.call(["which", name], stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

def is_interface_in_monitor_mode(interface):
    try:
        mode = subprocess.check_output(["iwconfig", interface], stderr=subprocess.STDOUT, universal_newlines=True)
        return "Mode:Monitor" in mode
    except subprocess.CalledProcessError:
        return False

def target_network():  # Renamed the function to target_network
    if not is_tool_installed("airodump-ng"):
        print("Error: airodump-ng not found. Please install it first.")
        return

    bssid = input("Enter the BSSID (e.g., AA:BB:CC:DD:EE:FF): ")
    if len(bssid.split(":")) != 6:
        print("Invalid BSSID format.")
        return

    channel_no = input("Enter the channel number (e.g., 1-14 for 2.4GHz): ")
    if not channel_no.isdigit() or not (1 <= int(channel_no) <= 14):
        print("Invalid channel number.")
        return

    Interface = input("Enter the interface in monitor mode (e.g., wlan0mon): ")
    if not is_interface_in_monitor_mode(Interface):
        print(f"Error: Interface {Interface} is not in monitor mode.")
        return

    os.system(f"airodump-ng --bssid {bssid} -c {channel_no} {Interface}")

if __name__ == "__main__":
    target_network()  # Renamed the function call
