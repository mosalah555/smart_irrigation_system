from functools import lru_cache
from pathlib import Path
import joblib,pandas as pd
VALID_CROPS={"tomato","potato","cucumber","pepper","onion"}
@lru_cache(maxsize=5)
def get_model(crop):
 if crop not in VALID_CROPS:raise ValueError("Unsupported crop: "+crop)
 return joblib.load(Path(__file__).resolve().parents[1]/"models"/f"{crop}_model.joblib")
def predict(crop,features):
 m=get_model(crop);x=pd.DataFrame([features]);r={"prediction":int(m.predict(x)[0])};r["irrigate"]=bool(r["prediction"])
 if hasattr(m,"predict_proba"):r["confidence"]=float(max(m.predict_proba(x)[0]))
 return r
