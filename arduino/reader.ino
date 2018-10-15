#include<>
#include <spi.h>    //Carregamos a livraria SPI incluida no IDE de Arduino
#include <RC522_RFID.h>   //Carregamos a livraria RC522_RFID de Paul Kourany
 
#define SS_PIN 10   // Declaramos o pino SDA do Arduino
#define RST_PIN 9   // Declaramos o pino RST do Arduino
RFID rfid(SS_PIN, RST_PIN);   //Iniciamos o objeto RFID
 
String cardID;      //Declaramos uma variável de tipo string
                    //para armazenar o valor dos dados obtidos da
                    // etiqueta RFID
 
void setup() {
    Serial.begin(9600); //Iniciamos a comunicação serie para ler as respostas do módulo
    SPI.begin();        //Iniciamos a comunicação SPI
    rfid.init();        //Iniciamos o objeto RFID

    pinMode(2, OUTPUT); // Led azul -> procurando
    pinMode(3, OUTPUT); // Led verde -> 
    pinMode(4, OUTPUT); // Led vermelho -> acesso recusado    
}

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



void loop()
{
    LED('azul');

    if (rfid.isCard()) {   //Se há um cartão perto do leitor...
        if (rfid.readCardSerial()) {     //Lemos a ID do cartão
        cardID = String(rfid.serNum[0]) + String(rfid.serNum[1]) + String(rfid.serNum[2]) + String(rfid.serNum[3]) + String(rfid.serNum[4]);  //Le damos una formato de cadena de carácteres
        Serial.write(cardID);

        rfid.halt();  //Finalizamos o objeto RFID
        delay(1000);  //Pausa de 1 segundo para dar tempo a finalizar todas as ordens
        }
    }

    
}


