# 🛡️ Advanced ARP Network Scanner for SOC Analysts

A lightweight and efficient Python-based network discovery tool built using **Scapy**. Designed to help Security Operations Center (SOC) analysts and penetration testers identify live hosts, MAC addresses, and hardware vendors on a local network segment.

## 🚀 Features
- **ARP Scanning:** Fast live host discovery using ARP broadcast requests.
- **Vendor Lookup:** Automatically fetches and displays the physical hardware vendor for each detected MAC address.
- **Structured Output:** Clean and readable tabular representation using `PrettyTable`.
- **Automated Logging:** Automatically captures and saves a screenshot of the scan results upon successful execution.

## 🛠️ Tech Stack
- **Python 3.x**
- **Scapy** (Packet manipulation and network scanning)
- **PrettyTable** (Terminal data formatting)
- **Mac-Vendor-Lookup** (OUI vendor identification)

---

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/rabsabubakarrao-png/network-scanner.git](https://github.com/rabsabubakarrao-png/network-scanner.git)
   cd network-scanner
