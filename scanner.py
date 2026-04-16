import subprocess
import os

def run_selected_scans(target, choices):
    os.makedirs("scans", exist_ok=True)

    scan_results = []

    scan_map = {
        "1": {
            "name": "Basic Scan",
            "cmd": ["nmap", target]
        },
        "2": {
            "name": "Host Discovery",
            "cmd": ["nmap", "-sn", target]
        },
        "3": {
            "name": "Full Port Scan",
            "cmd": ["nmap", "-p-", target]
        },
        "4": {
            "name": "Service Version Detection",
            "cmd": ["nmap", "-sV", target]
        },
        "5": {
            "name": "OS Detection",
            "cmd": ["nmap", "-O", target]
        },
        "6": {
            "name": "NSE Scan (Safe + Vuln)",
            "cmd": ["nmap", "--script=safe,vuln", target]
        },
        "7": {
            "name": "Full Scan",
            "cmd": ["nmap", "-sS", "-sV", "-O", "--script=default,vuln", target]
        }
    }

    for choice in choices:
        if choice not in scan_map:
            continue

        scan = scan_map[choice]
        print(f"\n[+] Running {scan['name']}...")

        try:
            result = subprocess.run(
                scan["cmd"],
                capture_output=True,
                text=True
            )

            output = result.stdout

            print(output)

            scan_results.append({
                "type": scan["name"],
                "command": " ".join(scan["cmd"]),
                "output": output
            })

        except Exception as e:
            print(f"[-] Error running {scan['name']}: {e}")

    return scan_results
