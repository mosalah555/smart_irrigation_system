#pragma once
#include <Arduino.h>
struct SensorData { float soil,temperature,humidity,flow,total; }; void sensorsBegin(); SensorData readSensors();
