from scapy.all import *

def detect_protocols(interface, bssid=None):
    # Filtering expression for capturing MQTT, CoAP, and UPnP/SSDP packets
    filter_str = "(tcp port 1883) or (udp port 5683 or udp port 5684) or (udp port 1900)"
    
    if bssid:
        filter_str += f" and ether host {bssid}"

    print("Scanning... Press Ctrl+C to interrupt.")
    
    try:
        packets = sniff(iface=interface, filter=filter_str, count=10, store=0, timeout=10)
        
        mqtt_detected = False
        coap_detected = False
        upnp_detected = False
        
        for packet in packets:
            if packet.haslayer(TCP) and packet[TCP].dport == 1883:
                mqtt_detected = True
            elif packet.haslayer(UDP):
                if packet[UDP].dport in [5683, 5684]:
                    coap_detected = True
                elif packet[UDP].dport == 1900:
                    upnp_detected = True

        if mqtt_detected:
            print_detected("MQTT")
        if coap_detected:
            print_detected("CoAP")
        if upnp_detected:
            print_detected("UPnP/SSDP")

        if not (mqtt_detected or coap_detected or upnp_detected):
            print("No known IoT protocols detected.")

    except KeyboardInterrupt:
        print("\nScanning interrupted by user. Returning to mode selection...")
    except Exception as e:
        print(f"Error: {e}")

def print_detected(protocol):
    print(f"Detected Protocol: {protocol}")

if __name__ == "__main__":
    interface = input("Please enter the network interface's name: ")

    while True:
        try:
            mode = input("\nChoose a mode [manual/default]: ").lower()

            bssid = None
            if mode == "manual":
                bssid = input("Enter the BSSID (MAC address) of the target IoT device or network: ")

            detect_protocols(interface, bssid)

        except KeyboardInterrupt:
            print("\nUser interrupted the mode selection. Exiting...")
            break
