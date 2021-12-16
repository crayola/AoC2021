from collections import namedtuple

def parse_bits(bits):
    version, bits = (bits[:3], bits[3:])
    type_id, bits = (bits[:3], bits[3:])
    Packet = namedtuple('Packet', (
        'version', 'type_id', 'groups', 'length_type_id', 
        'subpackets_number', 'subpackets_length', 'subpackets'
        ), defaults=(None,) * 7)
    if type_id == "100":
        groups = []
        trailing, group, bits = (bits[0], bits[1:5], bits[5:])
        groups += [(trailing, group)]
        while trailing == '1':
            trailing, group, bits = (bits[0], bits[1:5], bits[5:])
            groups += [(trailing, group)]
        packet = Packet(
            version = version, type_id = type_id,
            groups = groups
        )
    else:
        length_type_id, bits = (bits[0], bits[1:])
        if length_type_id == '0':
            subpackets_length, bits = (int(bits[:15], 2), bits[15:])
            subpackets_number = subpackets_length / 11
            remaining_bits = subpackets_length % 11
        if length_type_id == '1':
            subpackets_number, bits = (int(bits[:11], 2), bits[11:])
            subpackets_length = subpackets_number * 11
            remaining_bits = 0
        (subpackets, bits) = (bits[:(subpackets_length + 1)], bits[(subpackets_length + 1):])
        packet = Packet(
            version = version, type_id = type_id,
            subpackets = subpackets
        )
    print("bits left:", bits)
    return (packet, bits)

if __name__ == "__main__":
    bits = str(bin(int(open('16/input').read().strip(), 16)))[2:]
    print(bits)
    versions = []
    while True:
        packet, bits = parse_bits(bits)
        print(packet.version)
        print(bits)
        versions += packet.version