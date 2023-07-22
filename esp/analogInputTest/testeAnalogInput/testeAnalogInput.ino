// Potentiometer is connected to GPIO 34 (Analog ADC1_CH6) 
const int potPin = 33;

// variable for storing the potentiometer value
int potValue = 0;
int sensorValue = 0;
int cmValue = 0;

void setup() {
  Serial.begin(115200);
  delay(1000);
}

void loop() {
  // Reading potentiometer value
  /*potValue = analogRead(potPin);
  Serial.println(potValue);
  delay(250);*/
//0.0048828125
//0.0001118012
  sensorValue = analogRead(potPin);
  //cmValue = 13*pow(sensorValue * 0.0048828125 , -1);
  //cmValue = 13.*pow(sensorValue * 0.0048828125 , -1);
  cmValue = 8944.44/(sensorValue+1)+3.6; //bom
  //Serial.print("Valor lido = ");
  Serial.print(cmValue);
  Serial.println("\n");
  delay(250);
}
