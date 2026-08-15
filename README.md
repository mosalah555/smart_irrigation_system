# Smart Irrigation — 24-zone LoRa system

This project manages 24 independent zones through wired sensors → ESP32 → SX1278 LoRa → Raspberry Pi → crop-specific ML decision → LoRa command → ESP32 valve driver. No Bluetooth or Wi-Fi is used between zones and the gateway; the main pump is outside scope.

## Contents

| Folder / file | Purpose |
|---|---|
| `esp32/` | Firmware, local flow measurement and valve safety stop. |
| `raspberry/` | LoRa protocol, SQLite, alerts, reporting, gateway logic. |
| `ml/` | Reproducible research-informed synthetic generation/training pipeline. |
| `data/` | Generated crop-specific synthetic CSVs (not real field data). |
| `models/` | One cached pipeline and metadata per crop. |
| `model_results/` | Held-out test metrics and confusion matrices. |
| `simulation.html` | Browser-only interactive prototype. |

## Train five crop models

Do **not** use the earlier legacy `agriculture_10000_balanced.csv`: the revised system generates separate records for tomato, potato, cucumber, pepper and onion. In a virtual environment, run:

```bash
pip install pandas scikit-learn joblib
python irrigation_detection_model.py
```

The pipeline uses a 70/15/15 stratified train/validation/test split and compares logistic regression, random forest, and histogram gradient boosting by validation F1. Each model receives this explicit order: `soil_moisture_pct`, `temperature_c`, `humidity_pct`, `flow_rate_lpm`, `growth_stage`, `soil_type`, `recent_irrigation_l`. The first four are sensors; stage/soil/recent water are zone/database context, not invented physical sensors.

## Cost estimate — 1 feddan / 24 zones

Estimated hardware cost: **≈ 66,300 EGP** (≈ 66,000 EGP), excluding the existing main pump. The 24 zones total 58,776 EGP; the central Raspberry Pi, LoRa, storage, PSU, fittings and basic filter/pressure components are about 7,500 EGP.
