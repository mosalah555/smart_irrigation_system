from __future__ import annotations
from .protocol import decode_packet, PacketError

class LoRaReceiver:
    def __init__(self, radio): self.radio = radio
    def receive_one(self, timeout: float = 1.0):
        raw = self.radio.receive(timeout)
        if raw is None: return None
        try: return decode_packet(raw)
        except PacketError: return None
