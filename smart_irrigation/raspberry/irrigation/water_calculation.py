"""Shared transparent volume conversion; crop coefficients stay in model/context, not duplicated formulas."""
def calculate_required_water(area_m2: float, moisture_deficit_pct: float, demand_index: float, application_efficiency: float=.80) -> float:
    if area_m2<=0 or not 0<=moisture_deficit_pct<=100 or not 0<application_efficiency<=1: raise ValueError("invalid water-calculation inputs")
    # Field-calibration input: 1% deficit over 1 m² equals 0.06 L in the chosen effective root zone.
    return round(area_m2*moisture_deficit_pct*.06*demand_index/application_efficiency,1)
