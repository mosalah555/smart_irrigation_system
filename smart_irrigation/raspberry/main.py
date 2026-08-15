"""Gateway entry point. Inject a tested SX1278 Radio implementation before field use."""
import logging
from .database.database import Database
from .lora.receiver import LoRaReceiver
from .ml.inference import preprocess, predict_irrigation, ModelUnavailable
def process_packet(packet, db, controller):
    if packet["type"] != "sensor_data": return
    db.sensor_reading(packet)
    try: prediction=predict_irrigation(preprocess(packet["soil_moisture"],packet["temperature"],packet["flow_rate"]))
    except ModelUnavailable as exc: logging.error("No decision: %s",exc); return
    controller.decide(packet,prediction)
