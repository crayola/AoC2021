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
    Parses a single packet from a binary string, extracting version, type ID, and
    data, and recursively parses any subpackets based on the type ID and length
    type ID.

    Args:
        bits (str): Used to represent the binary representation of a packet, which
            is a string of binary digits (bits) that needs to be parsed.
        sumversions (int): Accumulated to keep track of the sum of versions of all
            packets encountered during the parsing process.

    Returns:
        Tuple[Packet,str,int]: A tuple containing a Packet object, the remaining
        bits of the input, and the total sum of version numbers.

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
    Parses a stream of binary bits into a specified number of packets or until the
    end of the stream is reached, returning the parsed packets, remaining bits,
    and total version sum.

    Args:
        bits (List[int]): Represented as a sequence of binary digits, where each
            digit is represented by an integer.
        num_packets (int | None): Optional. It specifies the number of packets to
            parse. If set to -1, it will parse all remaining packets, regardless
            of the length of the input bits.

    Returns:
        Tuple[List[object],List[int],int]: List of parsed packets, the remaining
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
    Decodes and processes a packet based on its type ID, recursively processing
    subpackets when necessary, and returns the decoded groups for literal packets
    or the result of applying a function from a dictionary for other packet types.

    Args:
        packet (Packet*): An object that contains information about a packet,
            including its type and subpackets.

    Returns:
        List[Union[int,float,str,bool]]|Dict[str,int]: A list of packets or a
        dictionary of key-value pairs, depending on the packet type.

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
