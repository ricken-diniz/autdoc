from dataclasses import dataclass
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

@dataclass(frozen=True)
class SysVars:

    ROOT = Path.cwd()

    DATA_ROOT = ROOT / "data"
    WHITELIST_PATH = DATA_ROOT / "telegram" / "whitelist.json"
    UPLOADS_PATH = DATA_ROOT / "uploads"

    NAPS2_PATH = Path("C:/") / "Program Files" / "NAPS2" / "NAPS2.Console.exe"
    NAPS2_USER = os.getenv("NAPS2_USER")

    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    PRIME_ID = int(os.getenv("PRIME_ID"))
    GEMINI_KEY = os.getenv("GEMINI_KEY")