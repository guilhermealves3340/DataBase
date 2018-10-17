//#include <Wire.h>
//#include <LiquidCrystal_I2C.h>
#include <SPI.h>    //Carregamos a lib SPI incluida no IDE de Arduino
#include <MFRC522.h> // Carregando a lib da FilipeFLop
//#include <RC522_RFID.h>   //Carregamos a lib RC522_RFID de Paul Kourany

// Inicializa o display no endereco 0x27
//LiquidCrystal_I2C lcd(0x27,2,1,0,4,5,6,7,3, POSITIVE);
 
#define SS_PIN 10   // Declaramos o pino SDA do Arduino
#define RST_PIN 9   // Declaramos o pino RST do Arduino

MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance.
//RFID rfid(SS_PIN, RST_PIN);   //Iniciamos o objeto RFID
 
String cardID;      //Declaramos uma variável de tipo string
                    //para armazenar o valor dos dados obtidos da
                    // etiqueta RFID
                
// char st[20];

void LED(String cor){
    if(cor == 'azul'){
        digitalWrite(2,1);      // Led azul ON
        digitalWrite(3,0);      // Led verde OFF
        digitalWrite(4,0);      // led vermelho OFF
    }

    if(cor == 'verde'){
        digitalWrite(2,0);      // Led azul ON
        digitalWrite(3,1);      // Led verde OFF
        digitalWrite(4,0);      // led vermelho OFF
    }

    if(cor == 'vermelho'){
        digitalWrite(2,0);      // Led azul ON
        digitalWrite(3,0);      // Led verde OFF
        digitalWrite(4,1);      // led vermelho OFF
    }
}


void setup() {
    Serial.begin(9600); //Iniciamos a comunicação serie para ler as respostas do módulo
    SPI.begin();        //Iniciamos a comunicação SPI
    //rfid.init();        //Iniciamos o objeto RFID
    mfrc522.PCD_Init();   // Inicia MFRC522

    pinMode(2, OUTPUT); // Led azul -> procurando
    pinMode(3, OUTPUT); // Led verde -> 
    pinMode(4, OUTPUT); // Led vermelho -> acesso recusado    

    //lcd.begin (16,2);
    //lcd.setBacklight(HIGH);

    
}

void loop()
{
    int sinal = 0;
    int tempo = 1000;
    String azul = "azul";
    LED(azul);

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
  //Mostra UID na serial
  //Serial.print("UID da tag :");
  String conteudo= "";
  byte letra;
  for (byte i = 0; i < mfrc522.uid.size; i++) 
  {
     //Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
     //Serial.print(mfrc522.uid.uidByte[i], HEX);
     conteudo.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
     conteudo.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  //Serial.println();
  //Serial.print("Mensagem : ");
    conteudo.toUpperCase();

    String cardID = conteudo.substring(1);
    Serial.write(cardID);

    while(1){
            msg = Serial.read()

            String vermelho = 'vermelho';
            if(msg == 1){
                LED(vermelho);

                sinal++;
                delay(tempo);
            }

            if(msg == 2){
                String verde = 'verde';
                LED(verde);

                sinal++;
                delay(tempo);
            }

            if(msg== 3){
                String vermelho = 'vermelho';
                LED(vermelho);

                sinal++;
                delay(tempo);
            }

            if(sinal==1){
                sinal=0;
                break;
            }

        }

  /*if (conteudo.substring(1) == "ED 78 03 CA") //UID 1 - Chaveiro
  {
    Serial.println("Ola FILIPEFLOP !");
    Serial.println();
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Ola FILIPEFLOP !");
    lcd.setCursor(0,1);
    lcd.print("Acesso liberado!");
    delay(3000);
    mensageminicial();
  }
 
  if (conteudo.substring(1) == "BD 9B 06 7D") //UID 2 - Cartao
  {
    Serial.println("Ola Cartao !");
    Serial.println();
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Ola Cartao !");
    lcd.setCursor(0,1);
    lcd.print("Acesso Negado !");
    delay(3000);
    mensageminicial();
  }

    if (rfid.isCard()) {   //Se há um cartão perto do leitor...
        if (rfid.readCardSerial()) {     //Lemos a ID do cartão
        cardID = String(rfid.serNum[0]) + String(rfid.serNum[1]) + String(rfid.serNum[2]) + String(rfid.serNum[3]) + String(rfid.serNum[4]);  //Le damos una formato de cadena de carácteres
        Serial.write(cardID);       // Enviando para o Python a tag do card encontrada

        while(1){
            msg = Serial.read()

            if(msg == 1){
                LED('vermelho');

                sinal++;
                delay(tempo);
            }

            if(msg == 2){
                LED('verde');

                sinal++;
                delay(tempo);
            }

            if(msg== 3){
                LED('vermelho');

                sinal++;
                delay(tempo);
            }

            if(sinal==1){
                sinal=0;
                break;
            }

        }

        //rfid.halt();  //Finalizamos o objeto RFID
        //delay(1000);  //Pausa de 1 segundo para dar tempo a finalizar todas as ordens
        }
    }*/

    
}