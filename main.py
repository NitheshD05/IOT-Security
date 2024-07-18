import os
import time
from subprocess import call
from attacks import display_protocols


def clear_screen():
    os.system('clear')

def display_main_menu():
    clear_screen()
    print("==== IoT Security Testing Tool ====")
    print("1. Network Scanning")
    print("2. Target Network")
    print("3. Attacks")
    print("0. Exit")
    choice = input("Enter your choice: ")
    return choice

def network_scanning():
    interface = input("Enter the interface name to switch to monitor mode: ")
    # Code to change the interface to monitor mode and start scanning
    # This will involve system commands for airodump-ng and other tools
    # Placeholder below for demonstration purposes:
    os.system(f'sudo ifconfig {interface} down')
    os.system(f'sudo iwconfig {interface} mode monitor')
    os.system(f'sudo ifconfig {interface} up')
    os.system(f'sudo airodump-ng {interface}')
    
    # After CTRL+C is pressed, you may need to add code here to process the results
    input("Press Enter to return to the main menu...")

def target_network():
    os.system('python3 target.py') 
    input("Press Enter to return to the main menu...")

def attacks():
    while True:
        display_protocols()
        choice = input("Press Enter to return to the main menu or enter 'q' to quit: ")
        if choice.lower() == "q":
            break


def main():
    while True:
        choice = display_main_menu()

        if choice == "1":
            network_scanning()
        elif choice == "2":
            target_network()
        elif choice == "3":
            attacks()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
