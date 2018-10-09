# 

import RPi.GPIO as GPIO
import time

import sys
sys.path.append("./lib")
import lcddriver
from time import *

import psycopg2 as pg

import MFRC522
import signal

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)        # Azul     -> Em operação
GPIO.setup(20, GPIO.OUT)        # Verde    -> Liberado
GPIO.setup(21, GPIO.OUT)        # Vermelho -> Barrado

GPIO.output(16, 1)

# LCD
lcd = lcddriver.lcd()
lcd.lcd_clear()

# Parametros: String, linha
lcd.lcd_display_string("TEMPERATURA", 1)

# Postgres
conn = ''
cur = ''
def conect_db():
    try:
        # Conectando com a nossa base de dados
        global conn = pg.connect("dbname=Engenharia user=postgres password=SENHA")

        # Criando o nosso cursor
        global cur = conn.cursor()

    except:
        pass

continue_reading = True

# Capture o SIGINT para limpeza quando o script for abortado
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Prenda o SIGINT
signal.signal(signal.SIGINT, end_read)

# Crie um objeto da classe MFRC522
MIFAREReader = MFRC522.MFRC522()

while continue_reading:

    # Procurar por cartões   
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # Se uma carta for encontrada
    if status == MIFAREReader.MI_OK:
        print "Card detected"

    # Obtenha o UID do cartão
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # Se tivermos o UID, continue
    if status == MIFAREReader.MI_OK:

        userID = int(str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3]))

        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]

        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(userID)

        conect_db()

        
