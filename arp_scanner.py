import subprocess
import re

def get_arp_table():
    try:
        result = subprocess.run(
            ['arp', '-a'],
            stdout=subprocess.PIPE,
            text=True
        )
        return result.stdout
    except Exception as e:
        print("Error:", e)
        return ""

def parse_arp(output):
    pattern = r'(\d+\.\d+\.\d+\.\d+)\s+([a-fA-F0-9:-]{17})'
    matches = re.findall(pattern, output)
    return matches

def display(entries):
    print("\nIP Address\t\tMAC Address")
    print("-"*40)
    
    for ip, mac in entries:
        print(f"{ip}\t{mac}")
    
    print("\nTotal Entries:", len(entries))


if __name__ == "__main__":
    print("=== ARP Scanner ===")
    
    output = get_arp_table()
    entries = parse_arp(output)
    display(entries)