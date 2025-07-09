// Pinos dos LEDs
const int ledRed = 23;     // LED vermelho
const int ledYellow = 22;  // LED amarelo
const int ledGreen = 21;   // LED verde

// Pino do PIR
const int pirPin = 25;     // GPIO do PIR

// Configurações de tempo (ms)
const unsigned long greenDelay = 5000;    // Tempo para ligar LED verde após movimento persistente
const unsigned long noMotionDelay = 2000; // Tempo para desligar LEDs após ausência de movimento

bool yellowOn = false;
bool greenOn = false;
unsigned long motionStartTime = 0;
unsigned long lastMotionTime = 0;

void setup() {
  pinMode(ledRed, OUTPUT);
  pinMode(ledYellow, OUTPUT);
  pinMode(ledGreen, OUTPUT);
  pinMode(pirPin, INPUT); // PIR geralmente usa entrada simples

  digitalWrite(ledRed, HIGH); // LED vermelho sempre ligado

  Serial.begin(9600);
}

void loop() {
  int pirValue = digitalRead(pirPin);
  Serial.print("PIR: ");
  Serial.println(pirValue);

  unsigned long currentTime = millis();

  if (pirValue == HIGH) {
    // Movimento detectado
    lastMotionTime = currentTime;

    if (!yellowOn) {
      digitalWrite(ledYellow, HIGH);
      yellowOn = true;
      motionStartTime = currentTime;
      Serial.println("Movimento detectado: LED amarelo ligado");
    }

    if (!greenOn && currentTime - motionStartTime >= greenDelay) {
      digitalWrite(ledGreen, HIGH);
      greenOn = true;
      Serial.println("Movimento persistente: LED verde ligado");
    }

  } else {
    // Sem movimento, checa tempo de ausência
    if ((currentTime - lastMotionTime) > noMotionDelay) {
      if (yellowOn || greenOn) {
        digitalWrite(ledYellow, LOW);
        digitalWrite(ledGreen, LOW);
        yellowOn = false;
        greenOn = false;
        Serial.println("Sem movimento: LEDs amarelo e verde desligados");
      }
    }
  }

  delay(100);
}
