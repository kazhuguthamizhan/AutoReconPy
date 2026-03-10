import argparse
import shutil
import sys
from scanner import run_nmap_scan

def check_nmap():
    if shutil.which("nmap") is None:
        print("[-] Nmap is not installed!")
        print("Install it using: sudo apt install nmap")
        sys.exit()
    else:
        print("[+] Nmap detected.")

def main():
    parser = argparse.ArgumentParser(description="AutoReconPy - Intelligent Recon Tool")
    parser.add_argument("-t", "--target", required=True, help="Target IP or domain")

    args = parser.parse_args()
    target = args.target

    print(f"[+] Target selected: {target}")

    check_nmap()

    print("[+] Starting Nmap scan...")
    run_nmap_scan(target)

if __name__ == "__main__":
    main()
