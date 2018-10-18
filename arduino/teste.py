# -*- coding: utf-8 -*-

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
        if rows[0] != None:
            rows = cur.fetchall()
        conn.commit()
        cur.close()
        print "[INFO]: CONEXÃO POSTGRES OK"

    except:
        print("[INFO]: FALHA CONEXÃO COM POSTGRES")            # Tratar erro

while True:

    print('teste')

    port.write('1')
    tag = str(port.readline())
    cardID = ''
    for i in range(11):
        cardID = cardID + tag[i]
    print cardID

    if cardID:

        sql = "SELECT userID, nome, sobreNome FROM proj.tb_funcionario WHERE idTag = '"+cardID+"';"
        
        conn = pg.connect("dbname=Engenharia user=postgres password=1997")
        cur = conn.cursor()
        cur.execute(sql)
        row = = cur.fetchall()
        conn.commit()
        cur.close()
        id = row[0][0]

        if id:

            now = datetime.now()
            hr = str(now.hour)+":"+str(now.minute)+":"+str(now.second)
            day = str(now.date())       # AAAA-MM-DD

            # Query de busca 
            sql = "SELECT entrada, almoco, retorno, saida FROM proj.tb_pontos WHERE userID = {} AND dia = '{}';".format(id,day)
            conn = pg.connect("dbname=Engenharia user=postgres password=1997")
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            conn.commit()
            cur.close()

            sql = ''

            if not rows[0]:
                sql = "INSERT INTO proj.tb_pontos(userID,dia,entrada) VALUES({},'{}','{}');".format(id,day,hr)
            else:
                
                if rows[3]:
                    port.write('2')      # Enviando para o lcd (1): 'Volte amanha'
                    sql = ''
                
                else:

                    sql = "UPDATE proj.tb_pontos SET {} = '{}' WHERE userID = {} AND dia = '{}'".format(ponto(rows),hr,id,day)

                    port.write('3')   # Enviando sinal para acesso liberado
                    print('PONTO REGISTRADO')
                    print(str(row[1])+" "+str(row[2]))
                    print(str(hr))

            
            if sql:
                conn = pg.connect("dbname=Engenharia user=postgres password=1997")
                cur = conn.cursor()
                cur.execute(sql)
                conn.commit()
                cur.close()

        else:
   
            print(str(row[1])+" "+str(row[2]))
            print('REGISTRO RECUSADO')
            print('FUNCIONARIO NAO ATIVO')
            port.write('2')"""

    time.sleep(1.8)
    