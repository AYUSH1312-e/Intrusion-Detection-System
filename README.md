🛡️ Real-Time Network Intrusion Detection System (NIDS)

A modular, high-performance Python-based Intrusion Detection System designed to monitor network traffic, detect malicious patterns, and visualize security alerts through an interactive web dashboard.

 🚀 Key Features
- Live Packet Sniffing**: Captures raw IP and TCP traffic using the Scapy library directly from your internal NIC.
- Advanced Detection Engine**:
  - Blacklist Filtering**: Instantly flags known malicious IP addresses.
  - DDoS/Flood Detection**: Identifies potential SYN flood attacks and packet size anomalies.
  - Port Scan Detection**: Detects reconnaissance activity by tracking connections to multiple destination ports.
- Interactive Dashboard**: A modern web interface powered by Flask and Chart.js, featuring:
  - Real-time threat distribution pie charts.
  - Live alert counters.
  - Auto-refreshing logs for continuous monitoring.
- Database Integration**: Securely logs all security events into an SQLite database (`ids_logs.db`) for historical analysis.

 🛠️ Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.x**
- Npcap (Windows Users): IMPORTANT:** During installation, you must check the box for **"Install Npcap in WinPcap API-compatible Mode".
- libpcap (Linux/macOS): Usually pre-installed, or can be installed via `sudo apt install libpcap-dev`.

 📦 Installation & Setup
1. Clone the Project**:
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git]
