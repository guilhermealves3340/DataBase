from pymongo import MongoClient
import psycopg2 as pg
from datetime import datetime
import json


def convert(y,x):
    x = datetime.strptime(x,'%Y-%m-%d %H:%M:%S')
    y = datetime.strptime(y,'%Y-%m-%d %H:%M:%S')
    return y - x


# Conect Postgres
conn = pg.connect("dbname=Engenharia user=postgres password=1997")
cur = conn.cursor()

# Conect MongoDB
myclient = MongoClient("mongodb://localhost:27017/")

db = myclient["tesla"]
col = db['horas']

sql = 'SELECT * FROM proj.tb_pontos'
cur.execute(sql)
rows = cur.fetchall()
conn.commit()
cur.close()

def existe(lista, _id):
        try:
                lista.index(_id)
        except:
                return False

def calcHoras(lista):
        p1 = comvert(lista[3],lista[2])
        p2 = convert(lista[5],lista[4])
        return p1+p2

ids = []
for i in range(len(rows)):
        if existe(ids,rows[i][0]) == False:
                ids.append(rows[i][0])

horas = 
for _id in ids:
        for i in range(len(rows)):
                if rows[i][0] == _ids:
                        horas += calcHoras(rows[i])