
import psycopg2
import serial
import time
from datetime import datetime
now = None

port = serial.Serial('/dev/ttyACM0', 9600)

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

while True:

    cardID = port.readline()

    if cardID:
        
