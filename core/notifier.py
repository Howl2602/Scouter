import yaml
import sys
import requests


def load_config(path="./setting.yaml"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)

        # File trống
        if not config:
            print("[ERROR] setting.yaml is empty!")
            sys.exit(1)

        # Check telegram section
        if "telegram" not in config:
            print("[ERROR] Missing [telegram] section!")
            sys.exit(1)

        telegram = config["telegram"]

        # Check token
        if not telegram.get("token"):
            print("[ERROR] Telegram bot token is empty!")
            sys.exit(1)

        # Check chat_id
        if not telegram.get("chat_id"):
            print("[ERROR] Telegram chat_id is empty!")
            sys.exit(1)

        return config

    except FileNotFoundError:
        print("[ERROR] setting.yaml not found!")
        sys.exit(1)

    except yaml.YAMLError as e:
        print(f"[YAML ERROR] {e}")
        sys.exit(1)

    except Exception as e:
        print(f"[CONFIG ERROR] {e}")
        sys.exit(1)


config = load_config()

BOT_TOKEN = config["telegram"]["token"]
CHAT_ID = config["telegram"]["chat_id"]


def send_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(url, data=payload)

    return response.json()


send_message("Bot hoạt động 😭")