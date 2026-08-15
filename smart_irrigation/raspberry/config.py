"""Runtime configuration. All limits are conservative defaults and must be field validated."""
from __future__ import annotations
import os
from dataclasses import dataclass
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = BASE_DIR / "model" / "model.joblib"
DATABASE_PATH = Path(os.getenv("IRRIGATION_DB", BASE_DIR / "irrigation.db"))
LORA_TIMEOUT_SECONDS = float(os.getenv("LORA_TIMEOUT_SECONDS", "5"))
LORA_RETRIES = int(os.getenv("LORA_RETRIES", "3"))
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

@dataclass(frozen=True)
class SafetyLimits:
    max_irrigation_time_seconds: int = int(os.getenv("MAX_IRRIGATION_TIME", "1800"))
    max_allowed_liters: float = float(os.getenv("MAX_ALLOWED_LITERS", "250"))
    no_flow_timeout_seconds: int = int(os.getenv("NO_FLOW_TIMEOUT", "60"))
    max_flow_rate_lpm: float = float(os.getenv("MAX_FLOW_RATE", "60"))

SAFETY = SafetyLimits()
ZONE_IDS = range(1, 25)
