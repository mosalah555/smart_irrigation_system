#include "flow_meter.h"
#include "config.h"
volatile uint32_t pulses=0; uint32_t lastPulses=0,lastMs=0;
void IRAM_ATTR flowPulse(){ pulses++; }
void flowBegin(){ pinMode(FLOW_PIN,INPUT_PULLUP); attachInterrupt(digitalPinToInterrupt(FLOW_PIN),flowPulse,RISING); lastMs=millis(); }
float totalLiters(){ noInterrupts(); uint32_t p=pulses; interrupts(); return p/FLOW_PULSES_PER_LITER; }
float flowRateLpm(){ uint32_t now=millis(); if(now-lastMs<1000) return 0; noInterrupts(); uint32_t p=pulses; interrupts(); float rate=(p-lastPulses)*60000.0f/(FLOW_PULSES_PER_LITER*(now-lastMs)); lastPulses=p;lastMs=now;return rate; }
void resetVolume(){ noInterrupts();pulses=0;interrupts();lastPulses=0;lastMs=millis(); }
