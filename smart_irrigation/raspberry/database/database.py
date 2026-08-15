from __future__ import annotations
import csv, sqlite3
from datetime import datetime, timedelta, timezone
from pathlib import Path
from ..config import DATABASE_PATH

class Database:
    def __init__(self, path: Path = DATABASE_PATH):
        self.conn = sqlite3.connect(path); self.conn.row_factory = sqlite3.Row
        self.conn.executescript((Path(__file__).with_name("schema.sql")).read_text()); self.conn.commit()
        self.conn.executemany("INSERT OR IGNORE INTO zones(zone_id) VALUES(?)", [(i,) for i in range(1,25)]); self.conn.commit()
    def sensor_reading(self, p: dict) -> None:
        self.conn.execute("INSERT INTO sensor_readings(zone_id,timestamp,soil_moisture,temperature,humidity,flow_rate,total_liters) VALUES(?,?,?,?,?,?,?)", (p["zone_id"], datetime.now(timezone.utc).isoformat(),p["soil_moisture"],p["temperature"],p.get("humidity"),p["flow_rate"],p["total_liters"])); self.conn.commit()
    def event(self, zone_id: int, target: float, status: str, actual: float | None = None) -> None:
        now=datetime.now(timezone.utc).isoformat(); self.conn.execute("INSERT INTO irrigation_events(zone_id,start_time,end_time,target_liters,actual_liters,status) VALUES(?,?,?,?,?,?)",(zone_id,now,now,target,actual,status)); self.conn.commit()
    def weekly_report(self, output: Path) -> list[dict]:
        since=(datetime.now(timezone.utc)-timedelta(days=7)).isoformat()
        rows=self.conn.execute("SELECT zone_id,COALESCE(SUM(actual_liters),0) liters,COUNT(*) events,AVG(actual_liters) avg_liters,SUM(status!='complete') failures FROM irrigation_events WHERE start_time>=? GROUP BY zone_id",(since,)).fetchall()
        data=[dict(r) for r in rows]; output.parent.mkdir(parents=True,exist_ok=True)
        with output.open("w",newline="") as f: csv.DictWriter(f,fieldnames=["zone_id","liters","events","avg_liters","failures"]).writeheader(); csv.DictWriter(f,fieldnames=["zone_id","liters","events","avg_liters","failures"]).writerows(data)
        return data
