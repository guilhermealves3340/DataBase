#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

import sys
sys.path.append("./lib")
import lcddriver
from time import *

import psycopg2 as pg

import MFRC522
import signal

from datetime import datetime
now = None

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)        # Azul     -> Em operação
GPIO.setup(20, GPIO.OUT)        # Verde    -> Liberado
GPIO.setup(21, GPIO.OUT)        # Vermelho -> Barrado

GPIO.output(16, 1)

# LCD
lcd = lcddriver.lcd()
lcd.lcd_clear()

def ponto(row):
    x = 0
    for i in row:
        if i:
            x = x +1

    if x == 0:
        return 'entrada'
    if x == 1:
        return 'almoco'
    if x == 2:
        return 'retorno'
    if x == 3:
        return 'saida'
        

# Postgres
def query(sql, rows):
    try:
        # Conectando com a nossa base de dados
        conn = pg.connect("dbname=Engenharia user=postgres password=1997")

        # Criando o nosso cursor
        cur = conn.cursor()

        cur.execute(sql)
        if rows != None:
            rows = cur.fetchall()
        conn.commit()
        cur.close()

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

        tag = int(str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3]))

        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]

        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(tag)

        sql = "SELECT userID, ativo, nome, sobreNome FROM proj.tb_funcionario WHERE idTag = " + str(tag)
        row = True
        query(sql,row)
        id = str(row[0])

        if row[1] == 1:
            GPIO.output(16, 0)      # Led azull OFF
            GPIO.output(20, 1)      # Led verde ON

            lcd.lcd_clear()         # Exibindo nome do funcionario no display
            lcd.lcd_display_string(str(row[2])+" "+str(row[3]),1)
            now = datetime.now()
            hr = str(now.hour)+":"+str(now.minute)+":"+str(now.second)
            day = str(now.date())       # AAAA-MM-DD
            lcd.lcd_display_string(str(hr),2)

            # Query de busca 
            sql = "SELECT entrada, almoco, retorno, saida FROM proj.tb_pontos WHERE userID = {} AND dia = {}".format(id,day)
            rows = 1
            query(sql,rows)

            if not rows:
                sql "INSERT INTO proj.pontos(userID,dia,entrada) VALUES({},{},{});".format(id,day,hr)
            else:
                sql = "UPDATE proj.pontos SET {} = {} WHERE userID = {} AND dia = {}".format(pontos(rows,hr,id,day))

            rows = None
            query(sql,rows)

            # Aguardando 3s
            time.sleep(3)

        else:
            GPIO.output(20, 0)
            GPIO.output(21, 1)
            
            lcd.lcd_clear()
            lcd.lcd_display_string(str(row[2])+" "+str(row[3]),1)
            lcd.lcd_display_string('ENTRADA RECUSADA',2)

            # Aguardando 3s
            time.sleep(3)


        

