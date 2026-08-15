from .water_calculation import calculate_required_water
from .safety import violation
from ..config import SAFETY
class IrrigationController:
 def __init__(self,transmitter,database,notifier):self.tx,self.db,self.notify=transmitter,database,notifier
 def decide(self,packet,prediction,context):
  if not prediction["irrigate"]:return False
  deficit=max(0,context["target_moisture_pct"]-packet["soil_moisture"]);litres=calculate_required_water(context["area_m2"],deficit,context["demand_index"])
  reason=violation(litres,packet["flow_rate"],0,0,SAFETY)
  if reason:raise RuntimeError(reason)
  self.tx.command("irrigate",packet["zone_id"],target_liters=litres);self.db.event(packet["zone_id"],litres,"started");self.notify.started(packet["zone_id"],litres);return True
 def completed(self,packet):self.db.event(packet["zone_id"],packet["target_liters"],"complete",packet["actual_liters"]);self.notify.completed(packet["zone_id"],packet["target_liters"],packet["actual_liters"])
