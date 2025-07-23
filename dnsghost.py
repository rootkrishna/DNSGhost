# DNSGhost - Subdomain Enumeration Tool
# Developed by KRISHNA

import requests
import threading
import queue
import sys
import os

BANNER = """
   ____  _   _ ____   ____ _               _     
  |  _ \| \ | |  _ \ / ___| |__   ___  ___| | __ 
  | | | |  \| | | | | |  _| '_ \ / _ \/ __| |/ / 
  | |_| | |\  | |_| | |_| | | | |  __/ (__|   <  
  |____/|_| \_|____/ \____|_| |_|\___|\___|_|\_\ 
          Subdomain Enumeration Tool - KRISHNA
"""

print(BANNER)

# Check arguments
if len(sys.argv) != 3:
    print("[!] Missing arguments.")
    print("Usage: python dnsghost.py <target-domain> <wordlist.txt>")
    print("\n[⚠] Running in test mode with default values for debugging...\n")
    # Test Mode Fallback
    target_domain = "example.com"
    wordlist_file = "test-wordlist.txt"

    # Create test wordlist if not exist
    if not os.path.exists(wordlist_file):
        with open(wordlist_file, "w") as f:
            f.write("www\nmail\nftp\n")
else:
    target_domain = sys.argv[1]
    wordlist_file = sys.argv[2]

q = queue.Queue()
threads = []

# Load subdomains
try:
    with open(wordlist_file, 'r') as f:
        for line in f:
            sub = line.strip()
            q.put(sub)
except FileNotFoundError:
    print(f"[!] Wordlist file not found: {wordlist_file}")
    sys.exit(1)

def scan():
    while not q.empty():
        subdomain = q.get()
        url = f"http://{subdomain}.{target_domain}"
        try:
            response = requests.get(url, timeout=3)
            print(f"[+] Found: {url} - Status: {response.status_code}")
        except requests.ConnectionError:
            pass
        except requests.exceptions.RequestException:
            pass

# Thread pool
for _ in range(20):
    t = threading.Thread(target=scan)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("\n[✔] Scan complete. Stay Ghost. 👻")
