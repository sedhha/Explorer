const int mot1f=5;//green//
const int mot1r=6;//black//
const int mot2f=10;//black//
const int mot2r=11;//green//
char mode;
void LEFT (void);
void RIGHT (void);
void FORWARD (void);
void REVERSE (void);

void setup()
{
  pinMode(mot1f,OUTPUT);
  pinMode(mot1r,OUTPUT);
  pinMode(mot2f,OUTPUT);
  pinMode(mot2r,OUTPUT);
  Serial.begin(9600);  
  
}

void loop() 
{
  
  while(Serial.available()>0)
  {
    mode=Serial.read();
  
  if((mode=='w')||(mode=='W'))
  FORWARD();
  else if((mode=='s')||(mode=='S'))
  REVERSE();
  else if((mode=='a')||(mode=='A'))
  LEFT();
  else if((mode=='d')||(mode=='D'))
  RIGHT();
  else if((mode=='x')||(mode=='X'))
  STOP();
  }
  delay(100);
}

void RIGHT (void)
{
  digitalWrite(5,LOW);
  digitalWrite(6,HIGH);
  digitalWrite(10,LOW);
  digitalWrite(11,HIGH);
   delay(100);
   
}

void LEFT (void)
{
   
  digitalWrite(5,HIGH);
  digitalWrite(6,LOW);
  digitalWrite(10,HIGH);
  digitalWrite(11,LOW);
  delay(100);
   
}

void FORWARD (void)
{
  digitalWrite(5,LOW);
  digitalWrite(6,HIGH);
  digitalWrite(10,HIGH);
  digitalWrite(11,LOW);
   delay(100);

}

void REVERSE (void)
{

  digitalWrite(5,HIGH);
  digitalWrite(6,LOW);
  digitalWrite(10,LOW);
  digitalWrite(11,HIGH);
   delay(100);

}

void STOP(void)
{
  
   digitalWrite(mot1f,LOW);
   digitalWrite(mot1r,LOW);
   digitalWrite(mot2f,LOW);
   digitalWrite(mot2r,LOW);
   delay(100);

}
