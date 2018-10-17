#!/usr/bin/env python3

import RPi.GPIO as gpio

# Display LCD
import sys
sys.path.append("./lib")
import lcddriver
from time import *

# Driver Postgress
import psycopg2 as pg

# SENSOR RFID
import MFRC522
import signal
import time

from datetime import datetime
now = None

gpio.setmode(gpio.BOARD)        # Definindo GPIO como BOARD
gpio.setwarnings(False)         # Retirando os avisos de alerta
gpio.setup(11, gpio.OUT)        # Azul     -> Em operação
gpio.setup(12, gpio.OUT)        # Verde    -> Liberado
gpio.setup(13, gpio.OUT)        # Vermelho -> Barrado

gpio.output(11, gpio.HIGH)      # Led azul ON
gpio.output(12, gpio.LOW)       # Led verde OFF
gpio.output(13, gpio.LOW)       # Led vermelho OFF

# LCD
lcd = lcddriver.lcd()
lcd.lcd_clear()                 # Limpando o display LCD

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

        # Executando a query passada
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
    print("Ctrl+C captured, ending read.")
    continue_reading = False
    gpio.cleanup()

# Prenda o SIGINT
signal.signal(signal.SIGINT, end_read)

# Crie um objeto da classe MFRC522
MIFAREReader = MFRC522.MFRC522()

while continue_reading:

    # Procurar por cartões   
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # Se um cartão for encontrado
    if status == MIFAREReader.MI_OK:
        print("Card detected")

    # Obtenha o UID do cartão
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    now = datetime.now()
    hr = str(now.hour)+":"+str(now.minute)+":"+str(now.second)
    date = str(now.date())
    lcd.lcd_display_string(date,1)
    lcd.lcd_display_string(hr,2)

    # Se tivermos o UID, continue
    if status == MIFAREReader.MI_OK:

        tag = str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])

        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]

        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(tag)

        sql = "SELECT userID, ativo, nome, sobreNome FROM proj.tb_funcionario WHERE idTag = "+tag
        row = [True]
        query(sql,row)
        id = str(row[0])

        if row[1] == 1:
            now = datetime.now()
            hr = str(now.hour)+":"+str(now.minute)+":"+str(now.second)
            day = str(now.date())       # AAAA-MM-DD

            # Query de busca 
            sql = "SELECT entrada, almoco, retorno, saida FROM proj.tb_pontos WHERE userID = {} AND dia = {}".format(id,day)
            rows = [True]
            query(sql,rows)

            if not rows:
                sql = "INSERT INTO proj.tb_pontos(userID,dia,entrada) VALUES({},{},{});".format(id,day,hr)
            else:
                
                if rows[3]:
                    lcd.lcd_clear()
                    lcd.lcd_display_string('VOLTE AMANHA',1)
                    sql = ''
                
                else:

                    sql = "UPDATE proj.tb_pontos SET {} = {} WHERE userID = {} AND dia = {}".format(ponto(rows),hr,id,day)
                    gpio.output(11, gpio.LOW)       # Led azul OFF
                    gpio.output(12, gpio.HIGH)      # Led verde ON
                    lcd.lcd_clear()                 # Exibindo nome do funcionario no display
                    lcd.lcd_display_string(str(row[2])+" "+str(row[3]),1)
                    lcd.lcd_display_string(str(hr),2)


            rows = None
            if sql:
                query(sql,rows)

            # Aguardando 3s
            time.sleep(3)

            gpio.output(12, gpio.LOW)       # Led verde OFF
            lcd.lcd_clear                   # Limpando o display LCD

        else:
            gpio.output(12, 0)          # Led verde OFF
            gpio.output(13, 1)          # Led vermelho ON
            
            lcd.lcd_clear()
            lcd.lcd_display_string(str(row[2])+" "+str(row[3]),1)
            lcd.lcd_display_string('ENTRADA RECUSADA',2)

            # Aguardando 3s
            time.sleep(3)

            gpio.output(13, gpio.LOW)       # Led vermelho OFF

            lcd.lcd_clear()                 # Limpando o display LCD