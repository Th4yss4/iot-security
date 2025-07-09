#include <WiFi.h>
#include <HTTPClient.h>

// Credenciais WiFi
const char* ssid = "UFPI";
const char* password = "";

// Token e Chat ID do Telegram
String botToken = "8105350995:AAFseuFyFmCcfIaQZZpAMas1fMX8WxHD-gw";
String chatID = "7793962721";

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
bool motionDetected = false;
bool wifiConnected = false;

unsigned long motionStartTime = 0;
unsigned long lastMotionTime = 0;

void setup() {
  pinMode(ledRed, OUTPUT);
  pinMode(ledYellow, OUTPUT);
  pinMode(ledGreen, OUTPUT);
  pinMode(pirPin, INPUT_PULLDOWN);  // Usar INPUT_PULLDOWN para PIR

  digitalWrite(ledRed, HIGH); // LED vermelho sempre ligado

  Serial.begin(115200);

  // Conectar ao WiFi
  WiFi.begin(ssid, password);
  Serial.print("Conectando ao WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConectado ao WiFi!");
  wifiConnected = true;

  // Enviar mensagem ao Telegram avisando que está online
  sendTelegramMessage("🔌 Sensor 01 conectado.");
}

void loop() {
  unsigned long currentTime = millis();
  int pirValue = digitalRead(pirPin);

  Serial.print("PIR Value: ");
  Serial.println(pirValue);

  // Checar status WiFi e reconectar mensagem
  if (WiFi.status() != WL_CONNECTED) {
    if (wifiConnected) {
      wifiConnected = false;
      Serial.println("WiFi desconectado!");
    }
  } else {
    if (!wifiConnected) {
      wifiConnected = true;
      Serial.println("WiFi reconectado!");
      sendTelegramMessage("🔌 ESP32 reconectado à internet.");
    }
  }

  if (pirValue == HIGH) {
    if (!motionDetected) {
      motionDetected = true;
      motionStartTime = currentTime;
      Serial.println("Movimento detectado.");
      sendTelegramMessage("🚨 Movimento detectado!");
    }
    lastMotionTime = currentTime;

    if (!yellowOn) {
      digitalWrite(ledYellow, HIGH);
      yellowOn = true;
      Serial.println("LED amarelo ligado.");
    }

    if (!greenOn && (currentTime - motionStartTime >= greenDelay)) {
      digitalWrite(ledGreen, HIGH);
      greenOn = true;
      Serial.println("Movimento persistente: LED verde ligado.");
    }

  } else {
    if (motionDetected && (currentTime - lastMotionTime >= noMotionDelay)) {
      motionDetected = false;

      if (yellowOn || greenOn) {
        digitalWrite(ledYellow, LOW);
        digitalWrite(ledGreen, LOW);
        yellowOn = false;
        greenOn = false;
        Serial.println("Sem movimento: LEDs amarelo e verde desligados.");
        sendTelegramMessage("✔️ Movimento cessou.");
      }
    }
  }

  delay(100);
}

void sendTelegramMessage(String message) {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    // Escapar caracteres para URL
    message.replace(" ", "%20");
    message.replace("\n", "%0A");

    String url = "https://api.telegram.org/bot" + botToken + "/sendMessage?chat_id=" + chatID + "&text=" + message;
    http.begin(url);
    int httpResponseCode = http.GET();
    if (httpResponseCode > 0) {
      Serial.print("Telegram enviado, código: ");
      Serial.println(httpResponseCode);
    } else {
      Serial.print("Erro ao enviar Telegram: ");
      Serial.println(httpResponseCode);
    } 
    http.end();
  } else {
    Serial.println("Não conectado ao WiFi, mensagem não enviada.");
  }
}
