from pymongo import MongoClient
import psycopg2 as pg
from datetime import datetime
import json


def difHoras(y,x):
    return y - x

# Conect Postgres
conn = pg.connect("dbname=Engenharia user=postgres password=1997")

def query(sql,op):
        cur = conn.cursor()
        cur.execute(sql)
        if op == 1:
            rows = cur.fetchall()
        else:
            rows = cur.fetchone()
        conn.commit()
        cur.close()
        return rows

rows = query('SELECT * FROM proj.tb_pontos',1)

# Conect MongoDB
myclient = MongoClient("mongodb://localhost:27017/")

db = myclient["tesla"]
col = db['horas']

def existe(lista, _id):
        try:
                lista.index(_id)
        except:
                return False

def calcHoras(lista):
        p1 = difHoras(datetime.combine(lista[1],lista[3]),datetime.combine(lista[1],lista[2]))
        p2 = difHoras(datetime.combine(lista[1],lista[5]),datetime.combine(lista[1],lista[4]))
        return p1+p2

# Listando todos os ids da tb pontos
ids = []
for i in range(len(rows)):
        if existe(ids,rows[i][0]) == False:
                ids.append(rows[i][0])

horas = datetime.now()
horas = horas - horas
docs = []
sql = 'SELECT nome,sobrenome,salario,cargaHoraria FROM proj.tb_funcionario WHERE userID = {} '

for _id in ids:
    # Somando a carga horaria de cada userID
    for i in rows:
        if _id == i[0]:
            horas += calcHoras(i)

    # Montando o json

    info = query(sql.format(_id),2)

    print(info[0][0])

class Informacoes(self,_id):
    
