"""
See: https://adventofcode.com/2021/day/16
"""

def parse_input():
    with open('input/test_16.txt', 'r') as file:
        return file.read()

def hex_to_binary(hex_str):
    h_size = len(hex_str) * 4
    return ( bin(int(hex_str, 16))[2:] ).zfill(h_size)

def binary_to_hex(bin_str):
    num = int(bin_str, 2)
    return format(num, 'x')

class Packet:
    def __init__(self, bin_str):
        self.src = bin_str
        self.version = binary_to_hex(bin_str[:3])
        self.type_id = binary_to_hex(bin_str[3:][:3])
        self.subpackets = []

        if self.type_id == "4":
            value = self.extract_literal(bin_str[6:])
            return

        self.len_type_id = bin_str[6]

        if self.len_type_id == "0":
            len_subpackets = int(bin_str[7:][:15], 2)   
            bin_data = ""
            for i in range(len_subpackets):
                bin_data += bin_str[22:][i]
                try:
                    p = Packet(bin_data)
                except Exception as e:
                    continue
                print("Successful 0 subpacket with data", bin_data)
                bin_data = ""
                self.subpackets.append(p)
        else:
            subpackets_num = int(bin_str[7:][:11], 2)
            subpacket_count = 0
            bin_data = ""
            data_idx = 0
            
            while subpackets_num > subpacket_count:
                bin_data += bin_str[18:][data_idx]
                try:
                    p = Packet(bin_data)
                except Exception as e:
                    data_idx += 1
                    continue
                print("Successful 1 subpacket with data", bin_data)
                bin_data = ""
                subpacket_count += 1
                data_idx += 1
                self.subpackets.append(p)
        
    def extract_literal(self, text):
        final_bin = ""
        while len(text) >= 5:
            chunk = text[:5]
            text = text[5:]
            final_bin += chunk[1:]
            if chunk[0] == "0":
                break

        return int(final_bin, 2)

def packet_version_sum(packet):
    if packet.version == "4":
        return 4
    else:
        res = int(packet.version)
        for sp in packet.subpackets:
            res += packet_version_sum(sp)
    return res

def part1():
    data = parse_input()
    data = hex_to_binary(data)
    
    p = Packet(data)
    print("Subpackets:", len(p.subpackets))
    # print(p.subpackets[0].src)
    

    return packet_version_sum(p)

if __name__ == '__main__':
    print(part1())
