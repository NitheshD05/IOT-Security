import nmap

def identify_protocols(ip_address):
    nm = nmap.PortScanner()
    nm.scan(ip_address, arguments='-F')  # Fast scan

    services = []

    for proto in nm[ip_address].all_protocols():
        lport = nm[ip_address][proto].keys()
        for port in lport:
            service = nm[ip_address][proto][port]['name']
            services.append(service)

    return services

ip = input("Enter the IP address of the device: ")
protocols = identify_protocols(ip)
print(f"Identified protocols/services for {ip}: {', '.join(protocols)}")
