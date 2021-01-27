#include <Arduino.h>
#include <Mouse.h>
#include <Keyboard.h>

char option[2] = {'0','0'};
int xVal;
int yVal;
float inc = 9.0;
int trigger;
int i=1;

void setup(){
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  Mouse.begin();
  Keyboard.begin();
}

void loop(){
  if(Serial.available()>0){
    option[0] = Serial.read();
    option[1] = Serial.read();
    xVal = Serial.read();
    yVal = Serial.read();
    Serial.println(xVal, yVal);
    //option[1]= Serial.read();
    //Serial.println("Option2:",option2[1]);
    inc = 9.0;
    i = 1;
  }

  //No Recoil
  if(option[0]=='1'){
    Mouse.move(0, i, 0);
    delay(7.3);
    inc-=0.07;
    if(inc<=0.0){
      i=0;
    }
  }

  //Trigger e No Recoil
  if(option[0]=='2'){
    if(option[1]=='1'){
      Mouse.press(MOUSE_LEFT);
      while(true){
        Mouse.move(0, i, 0);
        delay(7.3);
        inc-=0.24;
        if(inc<=0.0){
          i=0;
          Mouse.release();
          break;
        }
      }
    }else{
      Mouse.click(MOUSE_LEFT);
      delay(50);
      Mouse.click(MOUSE_LEFT);
      delay(50);
      Mouse.click(MOUSE_LEFT);
      delay(50);
    }
  }
  
  //Aimbot
  while(option[0]=='3'){
    xVal = Serial.read();
    yVal = Serial.read();
    Mouse.move(xVal, yVal, 0);
  }

}