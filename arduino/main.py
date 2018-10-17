
import psycopg2 as pg
import serial
import time
from datetime import datetime

now = None
port = serial.Serial('/dev/ttyACM0', 9600)


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

    cardID = str(port.readline())

    sql = "SELECT userID, ativo, nome, sobreNome FROM proj.tb_funcionario WHERE idTag = "+cardID
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
                port.write(1)      # Enviando para o lcd (1): 'Volte amanha'
                sql = ''
                
            else:

                sql = "UPDATE proj.tb_pontos SET {} = {} WHERE userID = {} AND dia = {}".format(ponto(rows),hr,id,day)

                port.write(2)   # Enviando sinal para acesso liberado
                print('PONTO REGISTRADO')
                print(str(row[2])+" "+str(row[3]))
                print(str(hr))

        rows = None
        if sql:
            query(sql,rows)

    else:
   
        print(str(row[2])+" "+str(row[3]))
        print('REGISTRO RECUSADO')
        print('FUNCIONARIO NAO ATIVO')
        port.write(3)
    