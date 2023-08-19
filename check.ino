#define Bulb 6
int value=0;
float voltage;
int stoptime=100;

void setup() {
 Serial.begin(2400);
 pinMode(Bulb,OUTPUT);
}

void loop() {
  if (Serial.available()>0){
    String msg = Serial.readStringUntil('\n');
    
    value=msg.toInt();
    if(value < 26){
      value=26;
    }
    else if (value>200){
      value=200;
    }
    voltage= map(value,26,200,0,255);
    analogWrite(Bulb,voltage);
    }

}
