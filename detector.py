from collections import defaultdict
import time

# Thresholds for detection
SYN_THRESHOLD = 20  # Requests per 5 seconds
SCAN_THRESHOLD = 15 # Different ports per 5 seconds

# Memory to track behavior
ip_stats = defaultdict(lambda: {"syn_count": 0, "ports": set(), "last_reset": time.time()})

def analyze_packet(src_ip, payload_size, dst_port=None, tcp_flags=None):
    blacklist = ["192.168.1.100", "45.33.22.11"]
    current_time = time.time()
    stats = ip_stats[src_ip]

    # Reset stats every 5 seconds for rate limiting
    if current_time - stats["last_reset"] > 5:
        stats["syn_count"] = 0
        stats["ports"] = set()
        stats["last_reset"] = current_time

    # 1. Blacklist Check
    if src_ip in blacklist:
        return "Blacklisted IP"

    # 2. SYN Flood Detection (DDoS)
    if tcp_flags == 'S': # 'S' flag means a SYN (connection) request
        stats["syn_count"] += 1
        if stats["syn_count"] > SYN_THRESHOLD:
            return "Potential SYN Flood (DDoS)"

    # 3. Port Scanning Detection
    if dst_port:
        stats["ports"].add(dst_port)
        if len(stats["ports"]) > SCAN_THRESHOLD:
            return "Port Scanning Detected"

    # 4. Payload Size Check
    if payload_size > 1400:
        return "Large Packet/Potential Overflow"

    return None