#pragma once
#include <Arduino.h>
void flowBegin(); void IRAM_ATTR flowPulse(); float flowRateLpm(); float totalLiters(); void resetVolume();
