from pymongo import MongoClient
import psycopg2 as pg
from datetime import datetime
import json


def difHoras(y,x):
    return y - x


# Conect Postgres
conn = pg.connect("dbname=Engenharia user=postgres password=1997")

def query(sql):
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.commit()
        cur.close()
        return rows

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

def drop():
    db = myclient["tesla"]
    col = db['horas']
    col.drop()
g=True
while g:

#    drop()

    db = myclient["tesla"]
    col = db['horas']



    rows = query('SELECT * FROM proj.tb_pontos')

    # Listando todos os ids da tb pontos
    ids = []
    for i in range(len(rows)):
            if existe(ids,rows[i][0]) == False:
                    ids.append(rows[i][0])

    horas = datetime.now()
    horas = horas - horas
    docs = []

    for _id in ids:

        # Somar as horas de cada id
        pontos = query('select * from proj.tb_pontos where userID = {}'.format(_id))

        for i in pontos:
            horas += calcHoras(i)

            info = query('select nome,sobrenome,salario,cargaHoraria from proj.tb_funcionario where userID = {} '.format(_id))
            print(info[0][0])
            func = dict(nome=info[0][0],sobrenome=info[0][1],salario=float(info[0][2]),cargaHoraria=float(info[0][3]),horas_compridas=str(horas))
        docs.append(func)

    #ol.insert_many(docs)
    #print(docs)

    d = myclient["tesla"]
    c = db['horas']
    for i in docs:
        c.insert_one(i)
















""
