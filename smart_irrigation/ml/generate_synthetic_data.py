"""Simulate sensor/context data governed by soil depletion, Kc demand, and retention."""
import csv, random
from pathlib import Path
from research_config import CROPS, SOIL, SOURCE
SEED=20260814
def generate_crop(crop, output, n=12000):
 rng=random.Random(SEED+sum(map(ord,crop)));cfg=CROPS[crop];output.parent.mkdir(parents=True,exist_ok=True)
 fields=["soil_moisture_pct","temperature_c","humidity_pct","flow_rate_lpm","growth_stage","soil_type","recent_irrigation_l","irrigation_required"]
 with output.open("w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
  for _ in range(n):
   stage,kc=rng.choice(cfg["stages"]);soil=rng.choice(list(SOIL));s=SOIL[soil];moisture=max(5,min(95,rng.gauss(55,18)));temp=rng.uniform(*cfg["temp"]);hum=rng.uniform(*cfg["humidity"]);recent=max(0,rng.gauss(10*kc*s["retention"],7));flow=0 if recent==0 else max(0,rng.gauss(4,1.1));demand=kc*(1+(temp-24)*.018+(55-hum)*.004);required=int(moisture<s["trigger"]-recent*.25 and demand>.55 and flow<.35);w.writerow(dict(soil_moisture_pct=round(moisture,2),temperature_c=round(temp,2),humidity_pct=round(hum,2),flow_rate_lpm=round(flow,2),growth_stage=stage,soil_type=soil,recent_irrigation_l=round(recent,2),irrigation_required=required))
if __name__=="__main__":
 root=Path(__file__).resolve().parents[1]
 for crop in CROPS: generate_crop(crop,root/"data"/f"{crop}_synthetic.csv")
 print("Generated research-informed crop-specific data; source: "+SOURCE)
