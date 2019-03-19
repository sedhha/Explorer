#include <dht.h>
dht DHT;
#define DHT11 7
const int mqp=3;
String mq135,temp,hum;
void setup() {
  // put your setup code here, to run once:
 pinMode(mqp,OUTPUT);
 Serial.begin(9600);
}

void loop() {
digitalWrite(mqp,HIGH); 
int c= DHT.read11(DHT11);
temp=String(DHT.temperature);
hum=String(DHT.humidity);
mq135=String(analogRead(A0));
Serial.print("(*)");
Serial.print(temp);
Serial.print(',');
Serial.print(hum);
Serial.print(',');
Serial.print(mq135);
Serial.print("*v*");
Serial.println(' ');
delay(1000);

}
