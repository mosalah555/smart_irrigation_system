from __future__ import annotations
import logging, requests
from ..config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
class TelegramNotifier:
    def send(self,text: str) -> None:
        if not (TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID): logging.getLogger(__name__).warning("Telegram not configured"); return
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",json={"chat_id":TELEGRAM_CHAT_ID,"text":text},timeout=10).raise_for_status()
    def started(self,z:int,l:float): self.send(f"🌱 Zone {z}\n💧 Irrigation started\n🎯 Target: {l:.1f} L")
    def completed(self,z:int,t:float,a:float): self.send(f"✅ Zone {z}\n💧 Irrigation completed\n🎯 Target: {t:.1f} L\n📊 Actual: {a:.1f} L")
