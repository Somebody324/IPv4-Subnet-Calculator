import ipaddress

def calculate_subnets(ip, num_subnets):
    #create IP address object
    network = ipaddress.IPv4Network(ip)
    
    #calculate the new prefix length based on the number of subnets
    new_prefix = network.prefixlen + (num_subnets - 1).bit_length()
    subnets = list(network.subnets(new_prefix=new_prefix))

    subnet_details = []

    for subnet in subnets[:num_subnets]:
        subnet_info = {
            "Subnet Address": str(subnet.network_address),
            "Usable IP Range": f"{subnet.network_address + 1} - {subnet.broadcast_address - 1}",
            "Subnet Mask": str(subnet.netmask),
            "Broadcast Address": str(subnet.broadcast_address)
        }
        subnet_details.append(subnet_info)
    
    return subnet_details

def display_subnets(subnets):
    print(f"{'Subnet Address':<20} {'Usable IP Address Range':<35} {'Subnet Mask':<20} {'Broadcast Address':<20}")
    for subnet in subnets:
        print(f"{subnet['Subnet Address']:<20} {subnet['Usable IP Range']:<35} {subnet['Subnet Mask']:<20} {subnet['Broadcast Address']:<20}")

if __name__ == "__main__":
    #get user input
    ip_address = input("Enter the IP address with prefix (e.g., '198.32.1.0/24'): ")
    number_of_subnets = int(input("Enter the number of subnets: "))

    subnets = calculate_subnets(ip_address, number_of_subnets)
    display_subnets(subnets)
