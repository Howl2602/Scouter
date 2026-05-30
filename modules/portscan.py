#portscan.py

import socket
from concurrent.futures import ThreadPoolExecutor


def scan_single_port(target, port, timeout):

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.settimeout(timeout)

        result = sock.connect_ex((target, port))

        sock.close()

        if result == 0:
            print(f"[OPEN] Port {port}")
            return port

    except:
        pass

    return None


def scan_ports(target, start_port, end_port, timeout, max_threads):

    ports = range(start_port, end_port + 1)

    open_ports = []

    with ThreadPoolExecutor(max_workers=max_threads) as executor:

        results = executor.map(
            lambda port: scan_single_port(target, port, timeout),
            ports
        )

    for result in results:
        if result:
            open_ports.append(result)

    return open_ports
