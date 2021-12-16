from functools import reduce
file_name = 'day16/input.txt'
input_packet = open(file_name, 'r').readline().strip('\n')

def unpack_packet(packet,depth=0):
    _,bits = int(packet[:3],2),packet[3:]
    packet_type_ID,bits = int(bits[:3],2),bits[3:]
    value = 0
    if packet_type_ID == 4:
        number_bits = []
        seq,bits = bits[:5],bits[5:]
        number_bits.append(seq[1:])
        while seq[0] != '0':
            seq,bits = bits[:5],bits[5:]
            number_bits.append(seq[1:])
        value = int(''.join(number_bits),2)
        for i in range(depth):
            print(' ',end='')
        print('num',value)
        return value,bits
    else:
        length_type_ID,bits = int(bits[:1],2),bits[1:]
        values_of_sub_packets = []
        if length_type_ID == 0:
            length = 15
        else:
            length = 11
        num,bits = int(bits[:length],2),bits[length:]
        if length_type_ID == 0:
            subpackets, bits = bits[:num], bits[num:]
            
            while len(subpackets) >= 11:
                value, subpackets = unpack_packet(subpackets,depth+1)
                values_of_sub_packets.append(value)
        else:
            for i in range(num):
                value,bits = unpack_packet(bits,depth+1)
                values_of_sub_packets.append(value)
        for i in range(depth):
            print(' ',end='')
        if packet_type_ID == 0:
            # print('+',end='')
            print('+',values_of_sub_packets,end='')
            value = sum(values_of_sub_packets)
        elif packet_type_ID == 1:
            print('*',end='')
            # print('*',values_of_sub_packets,end='')
            value = reduce((lambda x,y : x*y),values_of_sub_packets)
        elif packet_type_ID == 2:
            value = min(values_of_sub_packets)
        elif packet_type_ID == 3:
            print('max',end='')
            # print('max',values_of_sub_packets,end='')
            value = max(values_of_sub_packets)
        elif packet_type_ID == 5:
            if len(values_of_sub_packets) > 2:
                print('Error, more than 2 args of',end='')
            print('>',end='')
            # print('>',values_of_sub_packets,end='')
            if values_of_sub_packets[0] > values_of_sub_packets[1]:
                value = 1
            else:
                value = 0
        elif packet_type_ID == 6:
            if len(values_of_sub_packets) > 2:
                print('Error, more than 2 args of',end='')
            print('<',end='')
            # print('<',values_of_sub_packets,end='')
            if values_of_sub_packets[0] < values_of_sub_packets[1]:
                value = 1
            else:
                value = 0
        elif packet_type_ID == 7:
            if len(values_of_sub_packets) > 2:
                print('Error, more than 2 args of',end='')
            print('=',end='')
            # print('=',values_of_sub_packets,end='')
            if values_of_sub_packets[0] == values_of_sub_packets[1]:
                value = 1
            else:
                value = 0
        print(value)
        return value,bits    
    
    
def main():
    input_packet_size = len(input_packet) * 4
    input_packet_binary = bin(int(input_packet, 16))[2:].zfill(input_packet_size)
    value,bits = unpack_packet(input_packet_binary)
    return value


if __name__ == "__main__":
    print(main())
