from pymongo import MongoClient
import psycopg2 as pg
import serial
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
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

db = myclient["tesla"]

col = db['horas']

sql = 'SELECT * FROM proj.tb_pontos'
cur.execute(sql)
rows = cur.fetchall()
conn.commit()
cur.close()


month = str(datetime.now())[5:7]
for i in rows:
    if  month == i[1][5:7]:
        id_ = i[0]
        p1 = i[1] + ' '+ i[2]
        p2 = i[1] + ' '+ i[3]
        p3 = i[1] + ' '+ i[4]
        p4 = i[1] + ' '+ i[5]

        hr = str(convert(p1,p2) + convert(p3,p4))
        doc = {'_id': id_, 'qtd': hr}
        col.insert_one(doc)


