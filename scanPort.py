import socket
from colorama import Style, Fore, init
import argparse
import pyfiglet
from concurrent.futures import ThreadPoolExecutor
import threading

parser = argparse.ArgumentParser(description="Scanner de Port ! !")
parser.add_argument("--ip", "-p", help="Adresse IP", required=True)
parser.add_argument("--min", "-mn", help="Le port de début", type=int, required=True)
parser.add_argument("--max", "-mx", help="Le port de fin", type=int, required=True)
args = parser.parse_args()

init(autoreset=True)
banner = pyfiglet.figlet_format("Port Scanner\nScorpionMT")
print(Fore.GREEN + Style.BRIGHT + banner)

ip = args.ip
min_port = args.min
max_port = args.max

open_ports = []
lock = threading.Lock()

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.1)  # Temps d'attente réduit pour plus de vitesse
            if sock.connect_ex((ip, port)) == 0:
                with lock:
                    open_ports.append(port)
                    print(Fore.YELLOW + f"Port {port} OUVERT")
    except:
        pass

with ThreadPoolExecutor(max_workers=500) as executor:
    for port in range(min_port, max_port + 1):
        executor.submit(scan_port, ip, port)

print(Fore.CYAN + f"\nScan terminé : {len(open_ports)} port(s) ouvert(s)")
