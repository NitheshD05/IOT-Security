from scapy.all import ARP, Ether, srp, conf
import socket
import ipaddress

def get_default_ip_range():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.254.254.254', 1))
        local_ip = s.getsockname()[0]
        ip_net = ipaddress.ip_interface(local_ip + '/24')
        return str(ip_net.network)
    except Exception:
        return "192.168.1.0/24"
    finally:
        s.close()

def get_ip_range_choice():
    print("Choose scanning method:")
    print("1. Scan default subnet")
    print("2. Enter custom IP range")
    choice = input("Enter your choice (1/2): ")
    
    if choice == "1":
        return get_default_ip_range()
    elif choice == "2":
        return input("Enter the IP range (e.g., 192.168.1.1/24): ")
    else:
        print("Invalid choice! Using default subnet.")
        return get_default_ip_range()

def scan_network(ip_range):
    arp_req_frame = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_range)
    broadcast_ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast_arp_req_frame = broadcast_ether_frame / arp_req_frame

    answered_list = srp(broadcast_arp_req_frame, timeout=1, verbose=False)[0]
    devices = []

    for i in range(len(answered_list)):
        device_info = {"ip": answered_list[i][1].psrc, "mac": answered_list[i][1].hwsrc}
        devices.append(device_info)

    return devices

def select_device(devices):
    print("Available devices:")
    for index, device in enumerate(devices):
        print(f"{index}. IP: {device['ip']}, MAC: {device['mac']}")
    choice = int(input("Select a device by entering its number: "))

    if 0 <= choice < len(devices):
        return devices[choice]
    else:
        print("Invalid choice!")
        return None

def main():
    ip_range = get_ip_range_choice()
    print(f"Scanning the IP range: {ip_range}")
    devices = scan_network(ip_range)

    if not devices:
        print("No devices found.")
        return

    chosen_device = select_device(devices)
    if chosen_device:
        print(f"Chosen Device: IP: {chosen_device['ip']}, MAC: {chosen_device['mac']}")
    else:
        print("No device chosen. Exiting.")
        return

if __name__ == "__main__":
    main()
