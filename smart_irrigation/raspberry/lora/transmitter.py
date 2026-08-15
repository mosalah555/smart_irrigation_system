from __future__ import annotations
import logging, time
from typing import Protocol
from .protocol import encode_packet
from ..config import LORA_RETRIES, LORA_TIMEOUT_SECONDS

class Radio(Protocol):
    def send(self, payload: bytes) -> None: ...
    def receive(self, timeout: float) -> bytes | None: ...

class LoRaTransmitter:
    def __init__(self, radio: Radio): self.radio = radio; self.log = logging.getLogger(__name__)
    def command(self, message_type: str, zone_id: int, **data: object) -> str:
        raw = encode_packet(message_type, zone_id, **data)
        for attempt in range(LORA_RETRIES):
            self.radio.send(raw)
            response = self.radio.receive(LORA_TIMEOUT_SECONDS)
            if response and b'"type":"ack"' in response: return "acknowledged"
            self.log.warning("LoRa command retry %d zone %d", attempt + 1, zone_id)
            time.sleep(0.2)
        raise TimeoutError(f"zone {zone_id} did not acknowledge {message_type}")
