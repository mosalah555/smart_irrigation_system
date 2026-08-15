#include <ArduinoJson.h>
#include "config.h"
#include "sensors.h"
#include "lora.h"
#include "valve.h"
#include "flow_meter.h"
float target=0;unsigned long started=0,lastFlow=0,lastSend=0;
void sendSensor(){SensorData s=readSensors();StaticJsonDocument<256>d;d["type"]="sensor_data";d["zone_id"]=ZONE_ID;d["soil_moisture"]=s.soil;d["temperature"]=s.temperature;d["humidity"]=s.humidity;d["flow_rate"]=s.flow;d["total_liters"]=s.total;String o;serializeJson(d,o);loraSend(o);}
void stop(const char* reason){valveClose();StaticJsonDocument<192>d;d["type"]="irrigation_complete";d["zone_id"]=ZONE_ID;d["target_liters"]=target;d["actual_liters"]=totalLiters();d["reason"]=reason;String o;serializeJson(d,o);loraSend(o);}
void setup(){Serial.begin(115200);valveBegin();sensorsBegin();loraBegin();}
void loop(){String raw=loraReceive();if(raw.length()){StaticJsonDocument<256>d;if(!deserializeJson(d,raw)&&d["zone_id"]==ZONE_ID){const char*t=d["type"];if(!strcmp(t,"irrigate")){target=d["target_liters"];resetVolume();started=lastFlow=millis();valveOpen();}if(!strcmp(t,"stop_irrigation"))stop("remote_stop");StaticJsonDocument<96>a;a["type"]="ack";a["zone_id"]=ZONE_ID;a["message_id"]=d["message_id"];String o;serializeJson(a,o);loraSend(o);}}SensorData s=readSensors();if(valveIsOpen()){if(s.flow>0.01)lastFlow=millis();if(s.total>=target)stop("target_reached");else if(millis()-started>MAX_IRRIGATION_MS)stop("local_timeout");else if(millis()-lastFlow>NO_FLOW_TIMEOUT_MS)stop("no_flow");else if(s.flow>MAX_FLOW_LPM)stop("high_flow");}if(millis()-lastSend>60000){sendSensor();lastSend=millis();}}
