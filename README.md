# network-scanner
Simple ARP Network Scanner for SOC Analysts - Python + Scapy
# - SOC Tool
A simple Python tool to find live devices on your local network using ARP scan.

### Why I built this?
To understand how attackers do host discovery and how SOC Analysts can detect it.

### How to Run
```bash
pip install -r requirements.txt
sudo python scanner.py --hosts 192.168.1.0/24
