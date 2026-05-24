from scapy.all import *

def analyzer(pkt):
    if pkt.haslayer(IP):
        src_ip=pkt[IP].src
        dst_ip=pkt[IP].dst
        proto_name="Unknown"

        if pkt.haslayer(TCP):
            proto_name="TCP"

        elif pkt.haslayer(UDP):
            proto_name="UDP"

        elif pkt.haslayer(ICMP):
            proto_name="ICMP"

        if pkt.haslayer(Raw):
            print(f"[+] payload: {pkt[Raw].load}")

        print("-"*50)

        print(f"[*]New packet: {src_ip} ----({proto_name})----> {dst_ip}")

sniff(iface="Wi-Fi",prn=analyzer)
