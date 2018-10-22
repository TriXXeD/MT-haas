const int READ_NUM = 10;
int sens_moist = 8;
int green = 13;
int read_array[READ_NUM];
// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  
  pinMode(8, INPUT);
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop() {
  read_sens(sens_moist);
  delay(500);
  value = avg();
  //A High value means low capacitive value (i.e. dry soil)
  //Determine a threshold value and use ge, water has value ~250, dry soil should be 1k+
  if (value == HIGH) {
    // High read means low capacitive value
    digitalWrite(green, HIGH);
  } else {
    digitalWrite(green, LOW);
  }
  delay(5000);
  
}

void read_sens(int sens_read_pin){
  for (i=0; i < READ_NUM; i++){
    read_array[i] = analogRead(sens_read_pin);
    delay(100);
  }
}


int avg(){
  int sum = 0;
  for (int i; i < READ_NUM;i++){
    sum += read_array[i];
  }
  return (sum/READ_NUM);
}
