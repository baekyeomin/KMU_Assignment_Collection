#define PIN_LED 13
unsigned int count, toggle;

void setup() {
  pinMode(PIN_LED, OUTPUT);
  // Initialize serial and wait for port to open
  Serial.begin(115200); //baud를 맞춰줘야 원하는 결과가 나옴
  while(!Serial){
    ;//wait for serial port to connect. Needed for native USB
  }
  Serial.println("Hello World!");
  count = toggle = 0; //대부분의 코드는 우측에서 좌측으로 실행(toggle >> count)
  digitalWrite(PIN_LED, toggle); // turn off LED.
}

void loop() {
  Serial.println(++count); //선행 연산자(알아볼것)
  toggle = toggle_status(toggle); //toggle LED value
  digitalWrite(PIN_LED, toggle); //update LED status
  delay(1000); //값의 단위는 밀리초 (= 1초 기다림)
}

int toggle_status(int toggle){
  return !toggle;
}

