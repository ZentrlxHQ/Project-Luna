// firmware/failsafe.ino
// Watchdog that cuts servo power if simulated spike rate goes pathological
// (e.g. runaway firing, disconnected bridge, NaN motor commands).

const unsigned long WATCHDOG_TIMEOUT_MS = 500;
unsigned long lastHeartbeat = 0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  // TODO: expect a periodic heartbeat from motor_decoder.py;
  // if it stops or values look pathological, cut servo power.
  if (millis() - lastHeartbeat > WATCHDOG_TIMEOUT_MS) {
    // cutServoPower();
  }
}
