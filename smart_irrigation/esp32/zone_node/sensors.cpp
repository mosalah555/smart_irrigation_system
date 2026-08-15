#include "sensors.h"
#include "config.h"
#include "flow_meter.h"
#include <Wire.h>
#include <Adafruit_SHT31.h>
Adafruit_SHT31 sht; void sensorsBegin(){Wire.begin(SHT_SDA,SHT_SCL);sht.begin(0x44);analogReadResolution(12);flowBegin();}
SensorData readSensors(){return {(float)analogRead(SOIL_PIN),sht.readTemperature(),sht.readHumidity(),flowRateLpm(),totalLiters()};}
