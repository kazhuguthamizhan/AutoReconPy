import subprocess
import os

def run_nmap_scan(target):

    output_file = f"scans/{target}_scan.xml"

    command = [
        "nmap",
        "-sS",
        "-sV",
        "-O",
        "-oX",
        output_file,
        target
    ]

    print("[+] Running Nmap...")
    
    try:
        subprocess.run(command, check=True)
        print(f"[+] Scan completed. Results saved in {output_file}")
    except subprocess.CalledProcessError:
        print("[-] Nmap scan failed.")
