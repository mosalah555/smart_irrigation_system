"""Crop-model inference adapter. The model manager preserves metadata-defined feature order."""
from __future__ import annotations
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from ml.model_manager import predict
def predict_irrigation(crop: str, sensor: dict, context: dict) -> dict:
    features={"soil_moisture_pct":float(sensor["soil_moisture"]),"temperature_c":float(sensor["temperature"]),"humidity_pct":float(sensor["humidity"]),"flow_rate_lpm":float(sensor["flow_rate"]),"growth_stage":context["growth_stage"],"soil_type":context["soil_type"],"recent_irrigation_l":float(context.get("recent_irrigation_l",0))}
    return predict(crop,features)
