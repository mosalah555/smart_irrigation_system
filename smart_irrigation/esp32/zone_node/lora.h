#pragma once
#include <Arduino.h>
void loraBegin(); void loraSend(const String& json); String loraReceive();
