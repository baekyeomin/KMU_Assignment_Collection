int PINLED = 7;  // GPIO 7번 핀에 LED 연결
int period = 10000;  // 초기 주기 설정
int duty = 0;  // 초기 듀티 사이클: 0

// PWM 주기 설정 함수
void set_period(int newPeriod) {
  period = newPeriod;  // 주기 설정
}

// 듀티 사이클 설정 함수
void set_duty(int newDuty) {
  duty = newDuty;  // 듀티 설정
}

// PWM 제어 함수
void pwm() {
  int onTime = period * duty / 100;  // 켜짐 시간 계산
  int offTime = period - onTime;     // 꺼짐 시간 계산

  // LED ON
  digitalWrite(PINLED, 1);
  delayMicroseconds(onTime);  // 켜짐 시간 유지

  // LED OFF
  digitalWrite(PINLED, 0);
  delayMicroseconds(offTime);  // 꺼짐 시간 유지
}

// 밝기 제어 삼각형 패턴 함수
void trianglePattern() {
  // 최소 -> 최대 -> 최소로 듀티 사이클 변화 (101단계)
  for (int i = 0; i <= 100; i++) {  // 밝기 증가
    set_duty(i);
    pwm();
    delay(10);  
  }
  for (int i = 100; i >= 0; i--) {  // 밝기 감소
    set_duty(i);
    pwm();
    delay(10); 
  }
}

void setup() {
  pinMode(PINLED, OUTPUT);  // GPIO 7번 핀을 출력 모드로 설정
}

void loop() {
  set_period(10000);  // 10ms,1ms,0.1ms 주기설정
  trianglePattern();  // 삼각형 패턴 실행
}
