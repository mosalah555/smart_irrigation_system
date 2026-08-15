"""Shared domain calculations; controller code must import this function rather than reimplement it."""
from __future__ import annotations

def calculate_required_liters(soil_moisture: float, zone_area_m2: float | None = None) -> float:
    """Placeholder adapter because the supplied utils.py was empty.

    Replace this body with the validated agronomic calculation provided by the project owner.
    A non-positive result means no volume can be safely calculated.
    """
    if not 0 <= soil_moisture <= 100:
        raise ValueError("soil_moisture must be in percent [0, 100]")
    if zone_area_m2 is not None and zone_area_m2 <= 0:
        raise ValueError("zone_area_m2 must be positive")
    raise RuntimeError("Required-liters formula is unavailable: supplied utils.py was empty")
