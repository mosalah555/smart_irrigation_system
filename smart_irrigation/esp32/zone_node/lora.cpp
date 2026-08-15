#include "lora.h"
#include "config.h"
#include <SPI.h>
#include <LoRa.h>
void loraBegin(){SPI.begin();LoRa.setPins(LORA_SS,LORA_RST,LORA_DIO0);if(!LoRa.begin(433E6)) Serial.println("LoRa init failed");}
void loraSend(const String& s){LoRa.beginPacket();LoRa.print(s);LoRa.endPacket();}
String loraReceive(){int n=LoRa.parsePacket();if(!n)return "";String s;while(LoRa.available())s+=(char)LoRa.read();return s;}
