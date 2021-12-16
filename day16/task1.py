file_name = 'input.txt'
input_packet = open(file_name, 'r').readline().strip('\n')
sum_of_versions = 0

def unpack_operator_packet(packet):
    global sum_of_versions
    version = int(packet[:3],2)
    sum_of_versions += version
    packet_type_ID = int(packet[3:6],2)
    if packet_type_ID == 4:
        print('Wrong packet type ID of operator packet')
    length_type_ID = int(packet[6],2)
    sub_packets = [] #type,packet
    if length_type_ID == 0:
        total_length_of_sub_packets = int(packet[7:22],2)
        if total_length_of_sub_packets != 0:
            start_of_sub_packet = 22
            while True:
                if int(packet[start_of_sub_packet:],2) == 0:
                    break
                sub_packet_type_ID = int(packet[start_of_sub_packet+3:start_of_sub_packet+6],2)
                if sub_packet_type_ID == 4:
                    unpacked_sub_packet = unpack_literal_value_packet(packet[start_of_sub_packet:])
                    sub_packets.append(unpacked_sub_packet)
                    start_of_sub_packet += len(unpacked_sub_packet['packet'])
                elif sub_packet_type_ID != 4:
                    unpacked_sub_packet = unpack_operator_packet(packet[start_of_sub_packet:])
                    sub_packets.append(unpacked_sub_packet)
                    start_of_sub_packet += len(unpacked_sub_packet['packet'])
                else:
                    print('Operator packet error')
                if start_of_sub_packet+6 > len(packet):
                    break
    elif length_type_ID == 1:
        total_number_of_sub_packets = int(packet[7:18],2)
        start_of_sub_packet = 18
        while total_number_of_sub_packets != 0:
            total_number_of_sub_packets -= 1
            if int(packet[start_of_sub_packet:],2) == 0:
                break
            sub_packet_type_ID = int(packet[start_of_sub_packet+3:start_of_sub_packet+6],2)
            if sub_packet_type_ID == 4:
                unpacked_sub_packet = unpack_literal_value_packet(packet[start_of_sub_packet:])
                sub_packets.append(unpacked_sub_packet)
                start_of_sub_packet += len(unpacked_sub_packet['packet'])
            elif sub_packet_type_ID != 4:
                unpacked_sub_packet = unpack_operator_packet(packet[start_of_sub_packet:])
                sub_packets.append(unpacked_sub_packet)
                start_of_sub_packet += len(unpacked_sub_packet['packet'])
            else:
                print('Operator packet error')
    return {'version':version,'ID':packet_type_ID,'sub_packets':sub_packets,'packet':packet[:start_of_sub_packet]}    
            
def unpack_literal_value_packet(packet):
    global sum_of_versions
    version = int(packet[:3],2)
    sum_of_versions += version
    packet_type_ID = int(packet[3:6],2)
    if packet_type_ID != 4:
        print('Wrong packet type ID of literal value packet')
        return None
    number_bits = []
    start_bit_index = 6
    while True:
        current_bits = packet[start_bit_index:start_bit_index+5]
        number_bits.append(current_bits[1:])
        if current_bits[0] == '0':
            start_bit_index += 5
            break
        else:
            start_bit_index += 5
    number = int(''.join(number_bits),2)
    return {'version':version,'ID':packet_type_ID,'number':number,'packet':packet[:start_bit_index]}
        
    
    
def main():
    global sum_of_versions
    input_packet_size = len(input_packet) * 4
    input_packet_binary = bin(int(input_packet, 16))[2:].zfill(input_packet_size)
    outer_packet_type_ID = int(input_packet_binary[3:6],2)
    if outer_packet_type_ID == 4:
        print(unpack_literal_value_packet(input_packet_binary))
    else:
        print(unpack_operator_packet(input_packet_binary))
    return sum_of_versions


if __name__ == "__main__":
    print(main())
