import sys
from sys import exit, stderr, argv
from argparse import ArgumentParser
from scapy.all import Ether, ARP, srp
from prettytable import PrettyTable
from mac_vendor_lookup import MacLookup

class NetworkScanner:
    def __init__(self, hosts):
        self.hosts = hosts
        self.alive = {}
        for host in self.hosts:
            self.host = host
            self.create_packet()
            self.send_packet()
            self.get_alive()
        self.print_alive()

    def create_packet(self):
        layer1 = Ether(dst="ff:ff:ff:ff:ff:ff")
        layer2 = ARP(pdst=self.host)
        self.packet = layer1 / layer2

    def send_packet(self):
        answered, unanswered = srp(self.packet, timeout=1, verbose=False)
        if answered:
            self.answered = answered
        else:
            self.answered = []

    def get_alive(self):
        for sent, received in self.answered:
            self.alive[received.psrc] = received.hwsrc

    def print_alive(self):
        table = PrettyTable(["IP", "MAC", "VENDOR"])
        for ip, mac in self.alive.items():
            try:
                table.add_row([ip, mac, MacLookup().lookup(mac)])
            except:
                table.add_row([ip, mac, "Unknown"])
        print(table)


def get_args():
    parser = ArgumentParser(description="Network Scanner")
    parser.add_argument("-t", "--hosts", dest="hosts", nargs="+", help="Hosts to scan", required=True)
    arg = parser.parse_args()
    return arg.hosts


if __name__ == "__main__":
    hosts = get_args()
    NetworkScanner(hosts)
