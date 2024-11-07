from collections import namedtuple
import math

Packet = namedtuple('Packet', (
    'version', 'type_id', 'groups', 'length_type_id', 
    'subpackets_number', 'subpackets_length', 'subpackets'
    ), defaults=(None,) * 7)

func_dict = {
        0: sum, 1: math.prod, 2: min, 3: max, 
        5: lambda x: x[0] > x[1],
        6: lambda x: x[0] < x[1], 
        7: lambda x: x[0] == x[1],
    }

def parse_one_packet(bits, sumversions):
    """
    Parses a single packet of binary data from the given `bits` string into a
    `Packet` object, extracting version, type ID, and subpackets information, and
    returns the packet, remaining bits, and the total sum of versions encountered.

    Args:
        bits (str): Constructed from a binary string representing a packet in
            hexadecimal format, where each binary digit corresponds to a single bit.
        sumversions (int): Used to accumulate the version numbers of packets.

    Returns:
        Tuple[Packet,str,int]: A tuple containing a Packet object, the remaining
        binary bits, and the sum of the packet's version number.

    """
    version, bits = (int(bits[:3], 2), bits[3:])
    type_id, bits = (int(bits[:3], 2), bits[3:])
    if type_id == 4: # literal
        groups = ""
        trailing, group, bits = (bits[0], bits[1:5], bits[5:])
        groups += group
        while trailing == '1':
            trailing, group, bits = (bits[0], bits[1:5], bits[5:])
            groups += group
        packet = Packet(
            version = version, type_id = type_id,
            groups = int(groups, 2)
        )
        sumversions += version
    else:
        length_type_id, bits = (bits[0], bits[1:])
        if length_type_id == '0':
            subpackets_length, bits = (int(bits[:15], 2), bits[15:])
            packets, _, versions = parse_packets(bits[:subpackets_length])
            packet = Packet(
                version = version, type_id = type_id, length_type_id = '0',
                subpackets_length = subpackets_length, subpackets = packets
                )
            sumversions += version + versions 
            bits = bits[subpackets_length:]
        if length_type_id == '1':
            subpackets_number, bits = (int(bits[:11], 2), bits[11:])
            packets, bits, versions = parse_packets(bits, subpackets_number)
            packet = Packet(
                version = version, type_id = type_id, length_type_id = '1',
                subpackets_number = subpackets_number, subpackets = packets
                )
            sumversions += version + versions 
    return (packet, bits, sumversions)

def parse_packets(bits, num_packets = -1):
    """
    Parses a specified number of packets from a binary string, or all remaining
    packets if no limit is provided. It returns a list of packets, the remaining
    binary string, and the sum of version numbers of all packets.

    Args:
        bits (List[int]): Representing the binary representation of the input data
            as a list of integers, where each integer corresponds to a bit.
        num_packets (int | None): Optional. It specifies the number of packets to
            be parsed. If set to a positive integer, parsing stops after that many
            packets. If set to -1, parsing continues until the end of the input bits.

    Returns:
        Tuple[List[object],List[int],int]: A list of packets, a list of remaining
        bits, and the total sum of versions.

    """
    packets = []
    sumversions = 0
    i = 0
    while (i < num_packets) or (num_packets == -1 and len(bits) > 3): # avoid possible trailing zeros
        i += 1
        packet, bits, versions = parse_one_packet(bits, 0)
        packets += [packet]
        sumversions += versions
    return packets, bits, sumversions

def process_packet(packet: Packet):
    """
    Handles packet processing based on its type. If the packet is of type 4, it
    returns the packet's groups. Otherwise, it applies a function from a dictionary
    to the packet's subpackets, recursively processing each subpacket.

    Args:
        packet (Packet): An object representing a network packet.

    Returns:
        List[Union[int,str]]: A list of either integers or strings, depending on
        the packet type.

    """
    if packet.type_id == 4:
        return packet.groups
    else:
        return func_dict[packet.type_id]([process_packet(x) for x in packet.subpackets])

if __name__ == "__main__":
    bits = str(bin(int(open('16/input').read().strip(), 16)))[2:]
    bits = '0' * ((- (len(bits))) % 4) + bits # leading zeros
    packet, bits, sumversions = parse_one_packet(bits, 0)
    print("Part 1:", sumversions)
    print("Part 2:", process_packet(packet))
