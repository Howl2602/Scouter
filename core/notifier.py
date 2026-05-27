import yaml
from pathlib import Path
import sys
import requests


BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG_FILE = BASE_DIR / "config" / "settings.yaml"


def load_config():
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)

        if not config:
            raise ValueError("settings.yaml is empty!")

        return config

    except FileNotFoundError:
        print("[ERROR] settings.yaml not found!")
        sys.exit(1)

    except yaml.YAMLError as e:
        print(f"[YAML ERROR] {e}")
        sys.exit(1)

    except Exception as e:
        print(f"[CONFIG ERROR] {e}")
        sys.exit(1)


CONFIG = load_config()

BOT_TOKEN = CONFIG["telegram"]["token"]
CHAT_ID = CONFIG["telegram"]["chat_id"]


def send_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(url, data=payload)

    return response.json()


send_message("Bot hoạt động 😭")