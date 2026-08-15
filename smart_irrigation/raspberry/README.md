# Raspberry Pi gateway

Enable SPI (`raspi-config`), attach the SX1278 at 3.3 V, and supply a concrete `Radio` implementation with `send(bytes)` and `receive(timeout)` methods. The gateway does not drive valves: it stores sensor data, makes a model decision, calculates litres solely through `utils.calculate_required_liters`, then sends LoRa commands to an ESP32.

`DATABASE_PATH`, safety limits, LoRa retry values, and Telegram credentials are environment-configurable. Weekly CSV export is provided by `Database.weekly_report(output_path)`.
