void setup() {
  pinMode(13, OUTPUT);
}
void loop() {  
  int min = -500;
  int max = 1000;
  digitalWrite(13, HIGH);   
  delay(1000 + random(min,max));   
  digitalWrite(13, LOW);   
  delay(1000 + random(min,max));   
}
