def get_current_prefix(octets)->int:
    prefix=int()
    network_bits=str()
    for n in range(len(octets)):
        octets[n]= int(octets[n])
        network_bits+=str(bin(octets[n])).strip(r'\0b')
    for bits in network_bits:
        if(bits=='1'):prefix+=1
        else:break
    return prefix

def get_num_created_subnets(borrowed_bits)->int:
    return pow(2,borrowed_bits)

def get_num_assignable_ipaddr(host_bits)->int:
    return (pow(2,host_bits)-2)

def determine_interesting_octet(custom_subnet_mask)->int:
    if(custom_subnet_mask<=8):return 1
    elif(custom_subnet_mask<=16):return 2
    elif(custom_subnet_mask<=24):return 3
    else:return 4

def determine_block_size(interesting_octet, custom_subnet)->int:
    custom_subnet_octets=list()
    for n in range(0,4):
        custom_subnet_octets.append('')
        for i in range(0,8):
            if(not(custom_subnet == 0)):
                custom_subnet_octets[n]+='1'
                custom_subnet-=1
            else:
                custom_subnet_octets[n]+='0'
    return 256 - int(custom_subnet_octets[interesting_octet-1], base=2)

def populate_subnets(ip, num_subnets, total_ip_per_sub)->list:
    ip_octets = list()
    created_subs_and_ipRange=list()
    oct_value=0
    [ip_octets.append(int(oct)) for oct in ip.split('.')]
    for subnet in range(num_subnets):
        sub_list=list()
        for block_iter in range(total_ip_per_sub):
            if((oct_value % 256 == 0) and (not oct_value == 0)):
                temp=ip_octets[2] + 1
                if(temp>255):
                    ip_octets[1] += 1
                    ip_octets[2] = 0
                else:
                    ip_octets[2]=temp
                oct_value = 0       
            sub_list.append(f'{ip_octets[0]}.{ip_octets[1]}.{ip_octets[2]}.{oct_value}')
            oct_value+=1
        created_subs_and_ipRange.append(sub_list)
    return created_subs_and_ipRange

def resolve_subnet_configuration(working_bits) -> str:
    block = 8
    octets = 4
    subnet_mask_bits=''
    for n in range(32):
        if(working_bits == 0):subnet_mask_bits +='0'
        else:
            subnet_mask_bits+='1'
            working_bits-=1
        if(((n+1) % block == 0) and (not(n == 0 or n == block * octets - 1))):
            subnet_mask_bits += '.'
    subnet_mask_octs = subnet_mask_bits.split('.')
    for n in range(octets):
        subnet_mask_octs[n] = int(subnet_mask_octs[n], 2)
    subnet_mask=''.join([str(oct)+'.' for oct in subnet_mask_octs])[:-1]
    return subnet_mask

def print_subnet_info(address_ranges, ip, custom_subnet_prefix, new_subnet, num_created_subnets, num_assignable_ip, block_size, output_file)->None:
    #print some data to terminal
    print(f'{chr(0x0a)}Subnet info for: {ip}/{custom_subnet_prefix}')
    print(f'New Subnet Mask: {new_subnet}')
    print(f'Number of subnets created: {num_created_subnets}')
    print(f'Assignable ip per subnet: {num_assignable_ip}')
    print(f'Subnet block size: {block_size}')
    #write everything to file
    try:
        fhandle = open(output_file, mode='w')
    except FileExistsError as e:
        print(f'{type(e).__name__} {e.args}')
    finally:
        try:
            fhandle.write(f'Subnet info for: {ip}/{custom_subnet_prefix}{chr(0x0a)}')
            fhandle.write(f'New Subnet Mask: {new_subnet}')
            fhandle.write(f'Number of subnets created: {num_created_subnets}{chr(0x0a)}')
            fhandle.write(f'Assignable ip per subnet: {num_assignable_ip}{chr(0x0a)}')
            fhandle.write(f'Subnet block size: {block_size}{chr(0x0a)}')
            fhandle.write('\nCREATED SUBNETS AND ASSIGNABLE IP ADDRESSES:\n')
            for i in range(len(address_ranges)):
                fhandle.write(f'{chr(0x0a)}Subnet #{i+1}')
                fhandle.write('\n======================================================\n')
                for n in range(len(address_ranges[i])):
                    line=''
                    if(n==0):line+=('Subnet Address - ')
                    elif(n==len(address_ranges[i])-1):line+=('Broadcast Address - ')
                    else:line+=('Assignable Address - ')
                    line+=(address_ranges[i][n])
                    fhandle.write(line+'\n')
                fhandle.write('======================================================\n')
        except Exception as e:
            print(f'{type(e).__name__} {e.args}')
        else:
            print(f'{chr(0x0a)}File write to {output_file} successful.{chr(0x0a)}Please review the .txt file for complete information.{chr(0x0a)}')
            print("")
