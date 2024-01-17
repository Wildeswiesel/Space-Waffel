#include <Adafruit_NeoPixel.h>
#define PIN 13
#define NUMPIXELS 300
Adafruit_NeoPixel strip(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  // put your setup code here, to run once:
  strip.begin();
}
void loop() {
  // rainbow();
  // farbe();
  // out();
  instant_rainbow();
}


void out() {
  bool out = 0;
  if (out = 1) {
    strip.clear();
    strip.show();
  }
}

void farbe() {
  bool blue_on = 0;
  bool green_on = 0;
  bool red_on = 0;
  bool white_on = 0;

  uint32_t blue = strip.Color(0, 0, 255);
  uint32_t green = strip.Color(0, 255, 0);
  uint32_t red = strip.Color(255, 0, 0);
  uint32_t white = strip.Color(255, 255, 255);


  if (blue_on == 1) {
    strip.fill((blue), 0, 300);
    strip.show();
    // blue_on = 0;
  } else if (green_on == 1) {
    strip.fill((green), 0, 300);
    strip.show();
    green_on = 0;
  } else if (red_on == 1) {
    strip.fill((red), 0, 300);
    strip.show();
    red_on = 0;
  } else if (white_on == 1) {
    strip.fill((white), 0, 300);
    strip.show();
    white_on = 0;
  }
}

void rainbow() {
  bool rainbow_on = 1;
  uint16_t number = 0;
  uint8_t green = 0;
  uint8_t red = 0;
  uint8_t blue = 255;
  unsigned long orange = 0xff8c00;
  int DelayTime = 10;
  for (; rainbow_on == 1;) {
    for (; number < 300; number++) {
      delay(DelayTime);
      if (blue > 0) {
        strip.setPixelColor(number, red, green, blue);
        blue -= 3;
        green += 3;
        strip.show();
      } else if (blue< 1, green> 150) {
        strip.setPixelColor(number, red, green, blue);
        green -= 2;
        strip.show();
      } else if (green< 150, green> 1, blue< 1, red > - 1) {
        strip.setPixelColor(number, red, green, blue);
        red++;
        green--;
        strip.show();
      } else {
        green = 0;
        strip.setPixelColor(number, red, green, blue);
        red++;
        strip.show();
      }
    }
  }
}


void instant_rainbow() {
  static uint16_t startHue = 0;  // Start mit Rot
  static uint8_t brightness = 255;

  for (int i = 0; i < strip.numPixels(); i++) {
    strip.setPixelColor(i, strip.ColorHSV(startHue + i * 65536L / strip.numPixels(), 255, brightness));
  }

  strip.show();

  // Erhöhe den Start-Hue-Wert für die nächste Iteration
  startHue++;

  // Füge eine kleine Verzögerung hinzu, um die Geschwindigkeit der Farbänderung zu steuern
  delay(20);
}

