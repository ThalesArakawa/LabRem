#include <WiFi.h>
#include <ESPAsyncWebServer.h>


// Coloque suas credenciais
const char* ssid = "TP-LINK_C4A51A";
const char* password = "";

// AsyncWebServer porta 80
AsyncWebServer server(80);

const uint8_t irPin = 33;
const uint8_t push=32;
uint16_t sensorValue = 0;
float cmValue = 0.0;
uint8_t i=0;
uint16_t maxI=0;
uint16_t minI=0;
uint16_t result=0;

//Função de leitura do sensor IR
String readIRSharp() {
  maxI=0;
  minI=0;
  result=0;
 for(i=0;i<10;i++){
    sensorValue=analogRead(irPin);
    if(maxI<sensorValue) maxI=sensorValue;
    if(minI>sensorValue) minI=sensorValue;
    result+=sensorValue;
  }
  cmValue = (result-maxI-minI)*0.125;
  cmValue=22.4-75750.02606848886*pow(cmValue+474.0,-1.182561933562975);

  if(cmValue >= 24){
    cmValue=24;
  }
  if(cmValue <= 0){
    cmValue=0;
  }
  return String(cmValue);
}
//Função de leitura do sensor IR
String start() {

  digitalWrite(push, HIGH);
  delay(200);
  digitalWrite(push, LOW);
  return String("push");
}

//Função de resposta à requisição HTTP
void distRequest(AsyncWebServerRequest *request){
  request->send_P(200,"text/plain",readIRSharp().c_str());
}
void startRequest(AsyncWebServerRequest *request){
  request->send_P(200,"text/plain",start().c_str());
}

void setup(){
  pinMode(push, OUTPUT);
  // Parametrização da porta serial para acompanhar o processamento do programa
  Serial.begin(115200);
  
  // Conectando ao Wi-Fi
  Serial.println("BUSCANDO WIFI");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando...");
  }

  //Envia para o monitor serial o IP obtido pelo ESP32
  Serial.println("IP");
  Serial.println(WiFi.localIP());

  //Inicializa o servidor WEB assíncrono para receber requisições HTTP do tipo GET
  server.on("/IRSharp", HTTP_GET, distRequest);
  server.on("/push", HTTP_GET, startRequest);
  DefaultHeaders::Instance().addHeader("Access-Control-Allow-Origin","*");
  DefaultHeaders::Instance().addHeader("Access-Control-Allow-Methods","GET,POST,OPTIONS");
  DefaultHeaders::Instance().addHeader("Access-Control-Allow-Headers","Content-Type");

  // Start server
  server.begin();
}
 
void loop(){
/*
  //Rotina para monitoramento via TelemetryView
  float cf;
  float sf;
  float ca;
  char cf_text[30];
  char sf_text[30];
  char ca_text[30];
  char text[94];

  int result=0;
  int i;
  int maxI=0;
  int minI=0;
  int aux;
  for(i=0;i<10;i++){
    aux=analogRead(irPin);
    if(maxI<aux) maxI=aux;
    if(minI>aux)minI=aux;
    result+=aux;
  }
  sf=float(aux);
  cf = (result-maxI-minI)*0.125;
  ca=75750.02606848886*pow(sf+474.0,-1.182561933562975);

  dtostrf(cf,10,10,cf_text);
  dtostrf(cf,10,10,sf_text);
  dtostrf(cf,10,10,ca_text);
  snprintf(text,94,"%s,%s,%s",sf_text,cf_text,ca_text);

  Serial.println(text);

  delay(20);*/
}
