"""Small, explicit JSON protocol for SX1278 point-to-point packets."""
from __future__ import annotations
import json, time, uuid
from dataclasses import dataclass
from typing import Any

SENSOR_DATA = "sensor_data"; IRRIGATE = "irrigate"; STOP = "stop_irrigation"; ACK = "ack"; COMPLETE = "irrigation_complete"; ERROR = "error"
VALID_TYPES = {SENSOR_DATA, IRRIGATE, STOP, ACK, COMPLETE, ERROR}

class PacketError(ValueError): pass

def encode_packet(message_type: str, zone_id: int, **payload: Any) -> bytes:
    if message_type not in VALID_TYPES or not 1 <= zone_id <= 24: raise PacketError("invalid type or zone_id")
    packet = {"type": message_type, "zone_id": zone_id, "message_id": uuid.uuid4().hex[:12], "timestamp": int(time.time()), **payload}
    raw = json.dumps(packet, separators=(",", ":"), allow_nan=False).encode()
    if len(raw) > 220: raise PacketError("packet exceeds conservative LoRa payload limit")
    return raw

def decode_packet(raw: bytes) -> dict[str, Any]:
    try: packet = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc: raise PacketError("malformed JSON packet") from exc
    required = {"type", "zone_id", "message_id", "timestamp"}
    if not isinstance(packet, dict) or not required <= packet.keys(): raise PacketError("missing packet fields")
    if packet["type"] not in VALID_TYPES or not isinstance(packet["zone_id"], int) or not 1 <= packet["zone_id"] <= 24: raise PacketError("invalid packet values")
    return packet
