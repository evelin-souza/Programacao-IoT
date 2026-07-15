#include <DHT.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <WiFiClientSecure.h>


// PINOS ATUALIZADOS
#define DHTPIN 4       
#define DHTTYPE DHT22

#define LED_VERMELHO 21  
#define LED_AMARELO 19 
#define LED_AZUL 18      

// CONFIGURAÇÃO DO WIFI DO WOKWI
const char* ssid = "Wokwi-GUEST";
const char* password = "";

// URL DO NGROK QUE ESTÁ APONTANDO PARA O FLASK
const char* serverName = "http://sculpture-breeding-clamor.ngrok-free.dev/sensor-data";

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600); 
  dht.begin();

  pinMode(LED_VERMELHO, OUTPUT);
  pinMode(LED_AMARELO, OUTPUT);
  pinMode(LED_AZUL, OUTPUT);

  digitalWrite(LED_VERMELHO, LOW);
  digitalWrite(LED_AMARELO, LOW);
  digitalWrite(LED_AZUL, LOW);

  WiFi.begin(ssid, password);
  Serial.print("Conectando ao WiFi...");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi Conectado com sucesso!");
}

void loop() {
  float temperatura = dht.readTemperature();
  float umidade = dht.readHumidity();
  String estado = "FRIO";

  if (isnan(temperatura) || isnan(umidade)) {
    Serial.println("Falha ao ler o sensor DHT22!");
    delay(2000);
    return;
  }

  Serial.print("Temp: ");
  Serial.print(temperatura);
  Serial.print(" °C | Umidade: ");
  Serial.print(umidade);
  Serial.println(" %");

  // --- LÓGICA DOS LEDS ---
  if (temperatura >= 0 && temperatura <= 26) {
    estado = "FRIO";
    digitalWrite(LED_VERMELHO, LOW);
    digitalWrite(LED_AMARELO, LOW);
    digitalWrite(LED_AZUL, HIGH);
  }
  else if (temperatura >= 27 && temperatura <= 35) {
    estado = "MEDIO";
    digitalWrite(LED_VERMELHO, LOW);
    digitalWrite(LED_AMARELO, HIGH);
    digitalWrite(LED_AZUL, LOW);
  }
  else if (temperatura >= 36) {
    estado = "QUENTE";
    digitalWrite(LED_VERMELHO, HIGH);
    digitalWrite(LED_AMARELO, LOW);
    digitalWrite(LED_AZUL, LOW);
  }

  Serial.println("Estado atual: " + estado);

  // --- ENVIO DOS DADOS PARA O BACKEND (FLASK VIA NGROK) ---
  if (WiFi.status() == WL_CONNECTED) {
    
    // Cria um cliente seguro que ignora a validação SSL
    WiFiClientSecure client;
    client.setInsecure(); // <--- A mágica acontece aqui! Ignora o certificado do Ngrok

    HTTPClient http;
    
    // Iniciamos o HTTP usando o cliente seguro configurado acima
    http.begin(client, serverName); 
    
    http.addHeader("Content-Type", "application/json");
    http.addHeader("ngrok-skip-browser-warning", "true"); 

    String jsonPayload = "{\"temperatura\": " + String(temperatura) + 
                         ", \"umidade\": " + String(umidade) + 
                         ", \"estado\": \"" + estado + "\"}";

    int httpResponseCode = http.POST(jsonPayload);

    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.print("Resposta do Flask: ");
      Serial.println(response);
    } else {
      Serial.print("Erro no envio HTTP: ");
      Serial.println(httpResponseCode);
    }
    http.end();
  } else {
    Serial.println("Erro: WiFi Desconectado!");
  }

  Serial.println("--------------------------------");
  delay(2000); 
}