
#include <SPI.h>
#include <MFRC522.h>
#include <LiquidCrystal.h>
 
#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance.
 
LiquidCrystal lcd(6, 7, 5, 4, 3, 2); 
 
char st[20];
 
void setup() 
{
  Serial.begin(9600);   // Inicia a serial
  SPI.begin();      // Inicia  SPI bus
  mfrc522.PCD_Init();   // Inicia MFRC522 
  lcd.begin(16, 2);
}

char opc;

void loop() 
{
  if(Serial.available()>0){
  // Look for new cards
    if ( ! mfrc522.PICC_IsNewCardPresent()) 
    {
      return;
    }
    // Select one of the cards
    if ( ! mfrc522.PICC_ReadCardSerial()) 
    {
      return;
    }
    String conteudo= "";
    byte letra;
    for (byte i = 0; i < mfrc522.uid.size; i++) 
    {
       conteudo.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
       conteudo.concat(String(mfrc522.uid.uidByte[i], HEX));
    }
    conteudo.toUpperCase();    
    String cardID="";
    cardID = conteudo.substring(1);
    
    opc = Serial.read();       
    if(opc == '1'){
      Serial.println(cardID);
    }

    if(opc == '2'){
        led('m');
    }

    if(opc == '3'){
        led('v');
    }

    if(opc == '4'){
        led('a');
    }
  
  }
}

void led(char cor){
    if(cor == 'a'){
        digitalWrite(2,1);      // Led azul ON
        digitalWrite(3,0);      // Led verde OFF
        digitalWrite(4,0);      // led vermelho OFF
    }

    if(cor == 'v'){
        digitalWrite(2,0);      // Led azul ON
        digitalWrite(3,1);      // Led verde OFF
        digitalWrite(4,0);      // led vermelho OFF
    }

    if(cor == 'm'){
        digitalWrite(2,0);      // Led azul ON
        digitalWrite(3,0);      // Led verde OFF
        digitalWrite(4,1);      // led vermelho OFF
    }
}