import argparse
import shutil
import sys
import os

from scanner import run_selected_scans


def check_nmap():
    if shutil.which("nmap") is None:
        print("[-] Nmap is not installed!")
        print("Install it using: sudo apt install nmap")
        sys.exit()
    else:
        print("[+] Nmap detected.")


def main():
    parser = argparse.ArgumentParser(
        description="AutoReconPy - Intelligent Recon Tool"
    )
    parser.add_argument(
        "-t", "--target", required=True, help="Target IP or domain"
    )

    args = parser.parse_args()
    target = args.target

    print(f"[+] Target selected: {target}")

    check_nmap()

    # ✅ MENU (Correct placement)
    print("\nSelect Scan Types:")
    print("[1] Basic Scan")
    print("[2] Host Discovery")
    print("[3] Full Port Scan")
    print("[4] Service Version Detection")
    print("[5] OS Detection")
    print("[6] NSE Scan (Safe + Vuln)")
    print("[7] Full Scan")

    user_input = input("\nEnter choices (comma-separated, e.g., 1,3,6): ")
    choices = [c.strip() for c in user_input.split(",")]

    print("[+] Starting selected scans...")
    scan_results = run_selected_scans(target, choices)

    # 👉 Ask for report
    while True:
        choice = input("\n[?] Do you want to generate report? (y/n): ").strip().lower()

        if choice == 'y':
            print("[+] Generating report...")

            os.makedirs("reports", exist_ok=True)

            report_lines = []
            report_lines.append("=========== AutoReconPy Report ===========")
            report_lines.append(f"Target: {target}")
            report_lines.append("\n")

            for scan in scan_results:
                report_lines.append(f"--- {scan['type']} ---")
                report_lines.append(f"Command Used: {scan['command']}")
                report_lines.append("\nOutput:\n")
                report_lines.append(scan["output"])
                report_lines.append("\n" + "="*50 + "\n")

            report_text = "\n".join(report_lines)

            # 👉 Print to CLI
            print(report_text)

            # 👉 Save file
            output_file = f"reports/{target}_report.txt"

            with open(output_file, "w") as f:
                f.write(report_text)

            print(f"[+] Report saved to {output_file}")
            break

        elif choice == 'n':
            print("[-] Exiting without generating report.")
            break

        else:
            print("[!] Please enter 'y' or 'n'")


if __name__ == "__main__":
    main()
