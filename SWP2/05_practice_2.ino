#define PIN_LED 7

void setup(){
  pinMode(PIN_LED, OUTPUT);
}

void loop() {
  // 1초 동안 LED 켜기
  digitalWrite(PIN_LED, 1);

  delay(1000);

  //1초 동안 LED 5번 깜빡이기
  for (int i = 0; i<5; i++){
    digitalWrite(PIN_LED, 0);
    delay(100);
    digitalWrite(PIN_LED, 1);
    delay(100);
  }
  
  //LED 끄고 무한루프 
  digitalWrite(PIN_LED, 0);
  while(1){
    //아무 동작도 하지 않는 대기 상태
  }
}

