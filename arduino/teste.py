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

rows = query('SELECT * FROM proj.tb_pontos')

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


ids = []
for i in range(len(rows)):
        if existe(ids,rows[i][0]) == False:
                ids.append(rows[i][0])

print(len(ids))
horas = datetime.now()
horas = horas - horas
docs = []
sql = 'SELECT (nome,sobrenome,salario,cargaHoraria)'











sql = 'SELECT (nome,sobrenome,salario) FROM proj.tb_funcionario WHERE userID = {}'
rows = query('SELECT * FROM proj.tb_pontos')
print(len(rows))
for _id in ids:
        for i in range(len(rows)):
                if rows[i][0] == _id:
                        horas = horas + calcHoras(rows[i])

        aux = query(sql.format(_id))
        print(aux[0])

        """func = dict(_id=_id, nome=aux[0],sobrenome=aux[1],salario=aux[2],horas_comprimentos=str(horas))
        docs.append(func)
print(docs)
"""
