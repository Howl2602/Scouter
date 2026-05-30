#config.py

import yaml
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG_PATH = BASE_DIR / "config" / "settings.yaml"


def load_config():
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)

        if not config:
            print("[ERROR] settings.yaml is empty!")
            sys.exit(1)

        if "telegram" not in config:
            print("[ERROR] Missing [telegram] section!")
            sys.exit(1)

        telegram = config["telegram"]

        if not telegram.get("token"):
            print("[ERROR] Telegram bot token is empty!")
            sys.exit(1)

        if not telegram.get("chat_id"):
            print("[ERROR] Telegram chat_id is empty!")
            sys.exit(1)

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


config = load_config()
