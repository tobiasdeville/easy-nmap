import nmap
import sys
import os

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_header():
    print("="*40)
    print("  Nmap Interactive Menu (macOS)")
    print("="*40)

def get_target():
    target = input("Enter target IP address or hostname: ")
    return target

def get_ports():
    ports = input("Enter ports to scan (e.g., 22,80,443 or 1-1000), or leave blank for default: ")
    return ports if ports else None

def get_output():
    save = input("Save output to a file? (y/n): ").lower()
    if save == 'y':
        filename = input("Enter output filename: ")
        return filename
    return None

def run_scan(target, ports, arguments, output_file):
    nm = nmap.PortScanner()
    print(f"\nRunning scan: target={target}, ports={ports}, args={arguments}")
    nm.scan(target, ports, arguments=arguments)
    output = nm.csv()
    print("\nScan Results:\n")
    print(output)
    if output_file:
        with open(output_file, 'w') as f:
            f.write(output)
        print(f"\nResults saved to {output_file}")

def main_menu():
    while True:
        clear_screen()
        print_header()
        print("Select a scan type:")
        print("[1] Quick Scan (common ports)")
        print("[2] Full TCP Scan (all ports)")
        print("[3] Service & Version Detection")
        print("[4] OS Detection")
        print("[5] Host Discovery (Ping Sweep)")
        print("[6] Custom Scan")
        print("[0] Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nQuick Scan: Scans the most common 1000 TCP ports using a SYN scan (-sS). Fast and stealthy, but may require sudo for best results.[11][12]")
            target = get_target()
            output_file = get_output()
            run_scan(target, None, '-sS', output_file)

        elif choice == '2':
            print("\nFull TCP Scan: Scans all 65535 TCP ports. Comprehensive but slower. Use for thorough port discovery.[10][11]")
            target = get_target()
            output_file = get_output()
            run_scan(target, '1-65535', '-sS', output_file)

        elif choice == '3':
            print("\nService & Version Detection: Identifies services and their versions on open ports (-sV). Useful for vulnerability assessment.[10][11]")
            target = get_target()
            ports = get_ports()
            output_file = get_output()
            run_scan(target, ports, '-sV', output_file)

        elif choice == '4':
            print("\nOS Detection: Attempts to determine the operating system of the target (-O). May require root privileges for accuracy.[10][12]")
            target = get_target()
            output_file = get_output()
            run_scan(target, None, '-O', output_file)

        elif choice == '5':
            print("\nHost Discovery (Ping Sweep): Finds live hosts on a network without scanning ports (-sn). Good for mapping networks.[8][11]")
            target = get_target()
            output_file = get_output()
            run_scan(target, None, '-sn', output_file)

        elif choice == '6':
            print("\nCustom Scan: Enter any additional Nmap arguments for advanced scanning (e.g., -A for aggressive, --script for NSE scripts).[4][6]")
            target = get_target()
            ports = get_ports()
            args = input("Enter additional Nmap arguments: ")
            output_file = get_output()
            run_scan(target, ports, args, output_file)

        elif choice == '0':
            print("Exiting. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Try again.")
        input("\nPress Enter to return to the menu...")

if __name__ == '__main__':
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nScan interrupted by user. Exiting.")

