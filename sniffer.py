from scapy.all import sniff, IP, TCP, conf
import detector
import database

def process_packet(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        size = len(packet)
        
        # Get TCP details if available
        dst_port = packet[TCP].dport if packet.haslayer(TCP) else None
        tcp_flags = packet[TCP].flags if packet.haslayer(TCP) else None
        
        # Pass the extra details to the detector
        alert_msg = detector.analyze_packet(src_ip, size, dst_port, tcp_flags)
        
        if alert_msg:
            print(f"[!] ALERT: {alert_msg} from {src_ip}")
            database.save_alert(src_ip, alert_msg)

def start_sniffing():
    print(f"Sniffer started on interface: {conf.iface}")
    sniff(iface=conf.iface, prn=process_packet, store=0)