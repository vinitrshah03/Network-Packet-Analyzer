from scapy.all import sniff, Raw
from scapy.layers.inet import IP, TCP, UDP
import schedule  # type: ignore
import time
from os import path

packet_data = []
capture_duration = 10  # Capture duration in seconds

def process_packet(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        if TCP in packet:
            sport = packet[TCP].sport
            dport = packet[TCP].dport
            proto_name = "TCP"
            payload = packet[TCP].payload.original if Raw in packet else b''
        elif UDP in packet:
            sport = packet[UDP].sport
            dport = packet[UDP].dport
            proto_name = "UDP"
            payload = packet[UDP].payload.original if Raw in packet else b''
        else:
            sport = None
            dport = None
            proto_name = "Other"
            payload = b''

        pkt_info = " {},  {}  ,      {}      ,         {}         ,     {}     ,    {}".format(ip_src, ip_dst, sport, dport, proto_name, payload)
        packet_data.append(pkt_info)
        print(pkt_info)

def write_packet_data():
    global packet_data
    file_path = "C:/pkt_data.txt"

    # Create the file if it doesn't exist
    if not path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write('---Source_IP---|---Destination_IP---|---Source_port---|---Destination_port---|---Protocol---|---Payload---\n\n')

    with open(file_path, 'a') as f:
        for pkt in packet_data:
            f.write(str(pkt) + '\n')
    packet_data = []

def capture_packets():
    sniff(prn=process_packet, store=0, timeout=capture_duration)

# Schedule the packet data writing every 5 seconds
schedule.every(5).seconds.do(write_packet_data)

if __name__ == "__main__":
    # Start the packet sniffing in a separate thread
    import threading
    sniff_thread = threading.Thread(target=capture_packets)
    sniff_thread.daemon = True
    sniff_thread.start()

    start_time = time.time()

    while True:
        schedule.run_pending()
        time.sleep(1)
        if time.time() - start_time > capture_duration:
            break

    write_packet_data()  # Write any remaining packets after stopping
    print("Packet capture stopped.")
