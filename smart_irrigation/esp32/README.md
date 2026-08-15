# ESP32 zone node

Install Arduino libraries: `LoRa`, `ArduinoJson`, `Adafruit SHT31`, and `Adafruit BusIO`. Set `ZONE_ID` in `zone_node/config.h` to 1–24 before flashing each board.

The flow interrupt increments pulses. `total_liters = pulses / FLOW_PULSES_PER_LITER`; flow rate is pulses since the last sample converted to L/min. Calibrate by passing a measured 10 L, recording pulses, and setting pulses/10.

The node accepts only commands with its own zone ID, ACKs every valid command, closes the valve on target, no flow, high flow, timeout, or stop command. It intentionally remains safe if the gateway disappears.
