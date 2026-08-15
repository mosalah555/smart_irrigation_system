from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from raspberry.ml.inference import preprocess, predict_irrigation
from raspberry.lora.protocol import encode_packet, decode_packet, PacketError
from raspberry.irrigation.safety import violation
from raspberry.config import SAFETY
from raspberry.database.database import Database
from raspberry.utils import calculate_required_liters

class DummyModel:
    def predict(self,x): return [1]
    def predict_proba(self,x): return [[.1,.9]]

def test_model_order(): assert preprocess(1,2,3)==[1.0,2.0,3.0]
def test_model_result(): assert predict_irrigation([1,2,3],DummyModel())["confidence"]==.9
def test_packet_round_trip(): assert decode_packet(encode_packet("irrigate",13,target_liters=20))["zone_id"]==13
def test_invalid_packet():
    try: decode_packet(b"not-json")
    except PacketError: return
    assert False
def test_safety_limit(): assert violation(999,0,0,0,SAFETY)
def test_database_and_weekly_report(tmp_path):
    db=Database(tmp_path/"test.db"); db.event(1,20,"complete",20.1)
    data=db.weekly_report(tmp_path/"weekly.csv")
    assert data[0]["liters"]==20.1 and (tmp_path/"weekly.csv").is_file()
def test_missing_liters_formula_fails_safely():
    try: calculate_required_liters(20)
    except RuntimeError: return
    assert False
