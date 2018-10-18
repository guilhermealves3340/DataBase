
import psycopg2 as pg
import serial
import time
from datetime import datetime

now = None

porta = str(input("[ACM... : ]"))
device = '/dev/ttyACM'+porta
port = serial.Serial(device, 9600)


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
        pass            # Tratar erro

while True:

    port.write('1')
    cardID = str(port.readline())
    print '[',cardID,']'

    sql = "SELECT userID, ativo, nome, sobreNome FROM proj.tb_funcionario WHERE idTag = "+cardID
    row = [True]
    query(sql,row)
    id = str(row[0])
    print row[2]
    print id

    

    time.sleep(5)
    