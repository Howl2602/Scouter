#engine.py
from modules.portscan import scan_ports
from core.notifier import send_message
from core.config import config
from utils.helpers import format_alert_message

def run():
    target = config["portscan"]["target"]
    start_port = config["portscan"]["startport"]
    end_port = config["portscan"]["endport"]
    
    timeout = config["scanner"]["timeout"]
    max_threads = config["scanner"]["max_threads"]
    
    print(f"[INFO] Scanning {target}")

    open_ports = scan_ports(target, start_port, end_port, timeout, max_threads)

    msg = format_alert_message(target, open_ports)
    
    send_message(msg)