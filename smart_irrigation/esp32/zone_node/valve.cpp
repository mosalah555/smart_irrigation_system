#include <Arduino.h>
#include "valve.h"
#include "config.h"
bool openState=false; void valveBegin(){pinMode(VALVE_PIN,OUTPUT);valveClose();} void valveOpen(){digitalWrite(VALVE_PIN,HIGH);openState=true;} void valveClose(){digitalWrite(VALVE_PIN,LOW);openState=false;} bool valveIsOpen(){return openState;}
