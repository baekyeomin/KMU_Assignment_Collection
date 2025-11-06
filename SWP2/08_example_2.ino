// Arduino pin assignment
#define PIN_LED  9
#define PIN_TRIG 12   // sonar sensor TRIGGER
#define PIN_ECHO 13   // sonar sensor ECHO

// configurable parameters
#define SND_VEL 346.0     // sound velocity at 24 celsius degree (unit: m/sec)
#define INTERVAL 25      // sampling interval (unit: msec)
#define PULSE_DURATION 10 // ultra-sound Pulse Duration (unit: usec)
#define _DIST_MIN 100.0   // minimum distance to be measured (unit: mm)
#define _DIST_MAX 300.0   // maximum distance to be measured (unit: mm)

#define TIMEOUT ((INTERVAL / 2) * 1000.0) // maximum echo waiting time (unit: usec)
#define SCALE (0.001 * 0.5 * SND_VEL) // coefficent to convert duration to distance

unsigned long last_sampling_time;   // unit: msec

void setup() {
  // initialize GPIO pins
  pinMode(PIN_LED, OUTPUT);
  pinMode(PIN_TRIG, OUTPUT);  // sonar TRIGGER
  pinMode(PIN_ECHO, INPUT);   // sonar ECHO
  digitalWrite(PIN_TRIG, LOW);  // turn-off Sonar 
  
  // initialize serial port
  Serial.begin(57600);
}

void loop() { 
  float distance;

  // wait until next sampling time. // polling
  if (millis() < (last_sampling_time + INTERVAL))
    return;

  distance = USS_measure(PIN_TRIG, PIN_ECHO); // read distance

  // Adjust LED brightness based on distance
  int led_brightness = calculateLEDBrightness(distance);

  analogWrite(PIN_LED, led_brightness); // set LED brightness

  // output the distance and brightness to the serial port
  Serial.print("Min:");        Serial.print(_DIST_MIN);
  Serial.print(", Distance:");  Serial.print(distance);
  Serial.print(", Max:");       Serial.print(_DIST_MAX);
  Serial.print(", LED Brightness:"); Serial.print(led_brightness);
  Serial.println("");
  
  // update last sampling time
  last_sampling_time += INTERVAL;
}

// get a distance reading from USS. return value is in millimeter.
float USS_measure(int TRIG, int ECHO)
{
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(PULSE_DURATION);
  digitalWrite(TRIG, LOW);
  
  return pulseIn(ECHO, HIGH, TIMEOUT) * SCALE; // unit: mm
}

// Calculate LED brightness based on distance
int calculateLEDBrightness(float distance) {
  int brightness = 255;  // Default is off

  // If distance is out of range, keep LED off
  if (distance > _DIST_MAX || distance == 0.0) {
    brightness = 255;  // LED OFF
  } 
  else if (distance < _DIST_MIN) {
    brightness = 255;  // LED OFF
  }
  else {
    // Map the distance to the brightness
    if (distance <= 150) {
      // Brightness range: 200mm (max) -> 100mm (min)
      brightness = map(distance, 100, 200, 255, 0); // closer, brighter
    } 
    else if (distance <= 250) {
      // 50% brightness range: 150mm -> 250mm
      brightness = map(distance, 150, 250, 0, 128); // 50% brightness at these ranges
    }
    else {
      // Brightness range: 200mm (max) -> 300mm (min)
      brightness = map(distance, 250, 300, 128, 255); // farther, dimmer
    }
  }

  return brightness;
}
