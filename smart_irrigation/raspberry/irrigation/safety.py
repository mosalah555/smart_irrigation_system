from __future__ import annotations
from ..config import SafetyLimits

def violation(target_liters: float, flow_rate: float, elapsed_seconds: float, seconds_without_flow: float, limits: SafetyLimits) -> str | None:
    if target_liters <= 0 or target_liters > limits.max_allowed_liters: return "target volume outside safety limit"
    if elapsed_seconds > limits.max_irrigation_time_seconds: return "maximum irrigation time exceeded"
    if seconds_without_flow > limits.no_flow_timeout_seconds: return "no-flow timeout"
    if flow_rate > limits.max_flow_rate_lpm: return "abnormal high flow"
    return None
