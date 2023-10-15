/*
* Arduino Application to control an AIMOS 8 port KVM by wire rather than IR LED.
* Copyright (C) 2023  Syco54645
*
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
*
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

#include <IrSenderNonMod.h>

static constexpr pin_t outPin = 2;

static const microseconds_t btn1Data[] = {
  9034, 4466, 596, 1644, 596, 538, 592, 540, 590, 544, 596, 536, 592, 540, 590, 544, 596, 536, 594, 540, 590, 1650, 590, 1676, 564, 1650, 590, 1650, 590, 1650, 590, 1650, 590, 1652, 590, 544, 596, 1644, 596, 1644, 596, 1644, 596, 1644, 596, 538, 592, 542, 588, 544, 596, 1644, 596, 538, 592, 542, 588, 544, 594, 538, 592, 1648, 594, 1646, 594, 1646, 594
};
static const IrSequence btn1(btn1Data, sizeof(btn1Data) / sizeof(microseconds_t));

static const microseconds_t btn2Data[] = {
  9026, 4470, 592, 1648, 592, 542, 588, 544, 596, 536, 592, 540, 590, 542, 596, 536, 594, 540, 590, 542, 598, 1644, 596, 1642, 598, 1642, 598, 1642, 598, 1644, 596, 1644, 596, 1644, 596, 536, 594, 538, 590, 1650, 590, 1650, 590, 1650, 650, 482, 596, 536, 594, 538, 590, 1650, 590, 1650, 590, 542, 598, 534, 594, 538, 592, 1648, 592, 1648, 592, 1648, 592
};
static const IrSequence btn2(btn2Data, sizeof(btn2Data) / sizeof(microseconds_t));

static const microseconds_t btn3Data[] = {
  9028,4470,592,1648,592,542,588,546,594,538,592,540,588,544,596,536,594,540,590,544,596,1644,596,1642,598,1642,598,1642,598,1668,572,1668,572,1670,570,1670,570,1670,570,538,592,540,590,542,596,536,594,540,590,544,596,536,594,540,590,1650,590,1648,592,1648,592,1650,592,1674,566,1676,564
};
static const IrSequence btn3(btn3Data, sizeof(btn3Data) / sizeof(microseconds_t));

static const microseconds_t btn4Data[] = {
  9032,4468,644,1596,594,540,590,542,596,536,594,540,590,542,596,536,594,540,590,542,596,1668,562,1652,590,1650,590,1650,590,1650,590,1650,590,1648,592,542,596,536,594,540,590,542,596,536,594,538,592,542,588,546,594,1670,570,1644,598,1642,598,1642,598,1642,598,1642,588,1652,590,1650,590
};
static const IrSequence btn4(btn4Data, sizeof(btn4Data) / sizeof(microseconds_t));

static const microseconds_t btn5Data[] = {
  9032,4468,594,1646,594,540,590,542,598,534,596,538,592,542,588,544,596,538,592,540,590,1650,590,1650,590,1650,590,1650,590,1650,590,1650,590,1652,588,1652,590,1650,590,1650,590,544,596,536,592,540,590,542,598,536,594,540,590,542,598,534,594,1646,594,1646,596,1644,596,1644,596,1644,596
};
static const IrSequence btn5(btn5Data, sizeof(btn5Data) / sizeof(microseconds_t));

static const microseconds_t btn6Data[] = {
  9036,4464,598,1642,588,544,596,538,592,540,588,544,596,536,594,540,590,542,598,536,594,1646,596,1644,596,1644,596,1644,596,1642,598,1642,598,1642,598,536,594,540,590,1674,566,540,588,544,596,538,592,540,590,544,596,1642,598,1642,598,534,596,1644,596,1642,598,1642,598,1642,590,1650,590
};
static const IrSequence btn6(btn6Data, sizeof(btn6Data) / sizeof(microseconds_t));

static const microseconds_t btn7Data[] = {
  9030,4470,592,1646,594,540,590,542,598,536,594,540,590,544,596,536,594,540,590,542,598,1642,598,1644,586,1652,588,1652,598,1644,598,1644,596,1644,596,1642,598,1642,588,544,594,1644,596,536,594,540,590,544,596,536,594,538,592,542,588,1650,590,544,596,1642,598,1642,598,1642,588,1652,588
};
static const IrSequence btn7(btn7Data, sizeof(btn7Data) / sizeof(microseconds_t));

static const microseconds_t btn8Data[] = {
  9030,4468,596,1670,570,538,592,540,588,544,596,536,594,540,590,542,596,536,594,538,592,1648,592,1648,592,1648,592,1648,592,1648,592,1648,592,1646,594,540,590,544,596,536,594,1646,594,538,592,540,590,542,598,536,594,1646,596,1644,596,1644,598,536,594,1646,594,1646,594,1646,596,1644,596
};
static const IrSequence btn8(btn8Data, sizeof(btn8Data) / sizeof(microseconds_t));

static IrSenderNonMod sender(outPin, true);

void setup() {
  Serial.begin(9600);
}

void loop() {
  sender.sendNonModulated(btn1, 2);
  Serial.println("Sending btn1");
  delay(2000);
  
  sender.sendNonModulated(btn2, 2);
  Serial.println("Sending btn2");
  delay(2000);
  
  sender.sendNonModulated(btn3, 2);
  Serial.println("Sending btn3");
  delay(2000);
  
  sender.sendNonModulated(btn4, 2);
  Serial.println("Sending btn4");
  delay(2000);
  
  sender.sendNonModulated(btn5, 2);
  Serial.println("Sending btn5");
  delay(2000);
  
  sender.sendNonModulated(btn6, 2);
  Serial.println("Sending btn6");
  delay(2000);
  
  sender.sendNonModulated(btn7, 2);
  Serial.println("Sending btn7");
  delay(2000);
  
  sender.sendNonModulated(btn8, 2);
  Serial.println("Sending btn8");
  delay(2000);
}
