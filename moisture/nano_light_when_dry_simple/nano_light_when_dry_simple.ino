
int sens_moist = 8;
int green = 13;
int value = 0;
// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  
  pinMode(8, INPUT);
  pinMode(13, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  value = digitalRead(sens_moist);
  if (value == HIGH) {
    // High read means low capacitive value
    digitalWrite(green, HIGH);
  } else {
    digitalWrite(green, LOW);
    delay(1000);
  }
  
}
