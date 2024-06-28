from scapy.all import *
import logging

# Set up logging
logging.basicConfig(filename='network_activity.log', level=logging.INFO)

def log_packet(packet):
    # Get the IP address of the sender and receiver
    src_ip = packet[IP].src
    dst_ip = packet[IP].dst

    # Get the timestamp of the packet
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Get the size of the packet in bytes
    packet_size = len(packet)

    # Log the packet information
    logging.info(f"{timestamp}  {src_ip} -> {dst_ip}  Size: {packet_size} bytes")

# Start capturing packets
sniff(filter="ip", prn=log_packet)