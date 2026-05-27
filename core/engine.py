#engine.py
from modules.portscan import scan_ports
from core.notifier import send_message
from core.config import config


def run():
    target = config["portscan"]["target"]
    startport = config["portscan"]["startport"]
    endport = config["portscan"]["endport"]
    
    timeout = config["scanner"]["timeout"]
    max_threads = config["scanner"]["max_threads"]
    
    print(f"[INFO] Scanning {target}")

    open_ports = scan_ports(target, startport, endport, timeout, max_threads)

    send_message(f"[RESULT] ports opened: {open_ports}")