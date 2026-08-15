#pragma once
#define ZONE_ID 1                 // Change before flashing each node (1..24)
#define SOIL_PIN 34
#define FLOW_PIN 27
#define VALVE_PIN 26
#define SHT_SDA 21
#define SHT_SCL 22
#define LORA_SS 5
#define LORA_RST 14
#define LORA_DIO0 33
#define FLOW_PULSES_PER_LITER 450.0f // CALIBRATE: measured pulses / known litres
#define MAX_IRRIGATION_MS 1800000UL
#define NO_FLOW_TIMEOUT_MS 60000UL
#define MAX_FLOW_LPM 60.0f
