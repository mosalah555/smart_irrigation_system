# Model installation

The supplied `model.joblib` was 0 bytes and cannot be inspected or loaded. The supplied data-generation script indicates three columns in this exact order: `capacitive_soil_moisture`, `sht31_temperature`, `hall_effect_water_flow`. Accordingly the adapter passes `[capacitive, temperature, hall]`; humidity is recorded but is not sent to this current three-feature model.

Place a valid, inspected joblib estimator at `model/model.joblib`. It must expose `predict`. `predict_proba` is used only when present. If the replacement model expects a different schema or contains preprocessing, update and test `raspberry/ml/inference.py` explicitly—never silently reorder data.
