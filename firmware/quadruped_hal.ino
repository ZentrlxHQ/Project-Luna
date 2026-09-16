// firmware/quadruped_hal.ino
// Hardware abstraction layer: servo + sensor I/O for the quadruped chassis.

#include <Servo.h>

Servo legs[8];

void setup() {
  Serial.begin(115200);
  // TODO: attach each leg servo to its pin per bridge/channel_map.yaml
}

void loop() {
  // TODO: read PWM commands from motor_decoder.py over serial,
  // drive servos, stream sensor data back.
}
