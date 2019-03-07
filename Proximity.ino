int triggerPin=9;
int risingPin=3;
int fallingPin=2;
int LEDPin=10;
int movePin=11;
int indicatorPin=13;
int recording=0;
int limit=5;
int brightness=0;
int cap=20000;
int db=0;
int input=0;
int base=64;
long average=0;
volatile long boop=0;
double b=0;
char output=0;
bool up=false;
String test="";

void setup() {
  // setup code here, to run once:
  //Setting up the pins on the microcontroller
  pinMode(triggerPin, OUTPUT);
  pinMode(risingPin, INPUT);
  pinMode(fallingPin, INPUT);
  pinMode(LEDPin, OUTPUT);
  pinMode(movePin, OUTPUT);
  pinMode(indicatorPin, OUTPUT);
  //Adding interrupts to two pins, to detect changes in voltage
  attachInterrupt(digitalPinToInterrupt(risingPin), rising, RISING);
  attachInterrupt(digitalPinToInterrupt(fallingPin), falling, FALLING);
  //Outputting to the computer
  Serial.begin(9600);
}

void loop() {
  // main code here, to run repeatedly:
  //Send trigger signal
  digitalWrite(triggerPin, HIGH);
  //Moving average
  //digitalWrite(indicatorPin, LOW);
  if(recording>=limit){
    average/=limit;
    //-------LED Brightness stuff------
    //if(average>cap){
    //  brightness=0;
    //  db=0;
    //}else{
    //  if(brightness != (int)(255-(double)(255*pow((double)average/(double)cap,0.4)))){
    //    db = (int)(255-(double)(255*pow((double)average/(double)cap,0.4))) - brightness;
    //  }else{
    //    db = 0;
    //  }
    //  b = (double)average/(double)cap;
    //  //Finding brightness to emit LED
    //  brightness = 255-(double)(255*pow(b,0.4));
      if(input==174){
        limit=5;
        Serial.print(average);
        Serial.print("μs\n");
        //Serial.print("Brightness:");
        //Serial.print(brightness);
        //Serial.print("\n");
        //Serial.print("Delta brightness:");
        //Serial.print(db);
        //Serial.print("\n");
      }
    //}
    //analogWrite(movePin, abs(db));
    //analogWrite(LEDPin, brightness);
    //--------Binary input stuff-------
    //if(input!=174){
    //  if(base<1){
    //    base=128;
    //    output=input;
    //    digitalWrite(indicatorPin, HIGH);
    //    Serial.print(" ");
    //    Serial.print(output);
    //    Serial.print(" < ");
    //    Serial.print(input);
    //    Serial.print("\n");
    //    input=0;
    //    test+=output;
    //    if(output==0){
    //    Serial.print(test);
    //      Serial.print("\n");
    //      test="";
    //    }
    //  }else{
    //    if(up){
    //    input+=base;
    //      Serial.print(1);
    //    }else{
    //      input+=0;
    //      Serial.print(0);
    //   }
    //   digitalWrite(indicatorPin, HIGH);
    //   base/=2;
    //  }
    //  if(input==174){
    //    Serial.print("Switching functions! \n");
    //  }
    //}
    recording=0;
    average=0;
    //up=false;
  }
  delayMicroseconds(10);
  //End of trigger sequence
  digitalWrite(triggerPin, LOW);
  delay(50);//Waiting for interrupt
  average+=boop;//Adding to average
  //up=up||boop<5000;
  
  recording++;
}
//Interrputs: letting the program know when the pins have changed
void falling(){
  //Serial.print("Falling\n");
  boop=micros()-boop;
}

void rising(){
  //Serial.print("Rising\n");
  boop=micros();
}

