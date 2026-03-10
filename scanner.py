import socket
from colorama import Fore, init

init(autoreset=True)

print(Fore.CYAN + """
=================================
  TERMUX SIMPLE IP PORT SCANNER
=================================
""")

target = input("Enter Target IP: ")

ports = [21,22,23,25,53,80,110,139,143,443,445,8080]

print(Fore.YELLOW + f"\nScanning {target}...\n")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        print(Fore.GREEN + f"[OPEN] Port {port}")
    else:
        print(Fore.RED + f"[CLOSED] Port {port}")

    s.close()

print(Fore.CYAN + "\nScan Finished")