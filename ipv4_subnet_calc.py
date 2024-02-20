import sys
import subnet_utils

def ipv4_subnet_calculator(ip, current_subnet, borrowed_bits, output_file):
    octets = current_subnet.split('.')
    prefix = subnet_utils.get_current_prefix(octets)
    custom_subnet_prefix = prefix+borrowed_bits
    host_bits = 32 - custom_subnet_prefix
    num_created_subnets = subnet_utils.get_num_created_subnets(borrowed_bits)
    num_assignable_ip = subnet_utils.get_num_assignable_ipaddr(host_bits)
    total_ip_per_sub = num_assignable_ip + 2
    interesting_octet = subnet_utils.determine_interesting_octet(custom_subnet_prefix)
    block_size = subnet_utils.determine_block_size(interesting_octet, custom_subnet_prefix)
    address_ranges = subnet_utils.populate_subnets(ip, num_created_subnets, total_ip_per_sub)
    subnet_utils.print_subnet_info(address_ranges, ip, custom_subnet_prefix, num_created_subnets, num_assignable_ip, block_size, output_file)
    
if __name__=="__main__":
    try:
        ipv4_subnet_calculator(str(sys.argv[1]), str(sys.argv[2]), int(sys.argv[3]), str(sys.argv[4]))
    except:
        print('None or incorrect command line args passed.\n')
        try:
            ip=str(input('Enter the Network IP Address (192.168.0.0): '))
            subnet=str(input('Enter the Subnet Mask you would like to borrow from (255.255.0.0): '))
            borrowed_bits=int(input('Enter the number of bits you want to borrow from the Subnet Mask '))
            output_file=str(input('Enter the /path/to/filename.txt in which you would like the output to be written. It will be created if not exists.: '))
        except:
            print('Data Entry Error. Be sure to enter the information correctly.')
        else:
            ipv4_subnet_calculator(ip, subnet, borrowed_bits, output_file)
