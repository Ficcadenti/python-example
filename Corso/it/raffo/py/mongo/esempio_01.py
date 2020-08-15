'''
Created on 14 ago 2020

@author: raffa
'''
import pymongo as pm
from pymongo import MongoClient

if __name__ == '__main__':
    pass

# connessione a mongo
client = MongoClient('localhost',27017)
print(client)

# accediamo al database per crearlo
db = client.testdb

# creo la collection in testdb
persone = db.persone

# creazione degli indici
persone.create_index([("nome",pm.ASCENDING)])
persone.create_index([("cognome",pm.ASCENDING)])
persone.create_index([("computer",pm.ASCENDING)])

# creazione documento
p1={"nome":"Raffaele","cognome":"Ficcadenti","eta":44,"computer":["Acer","Asus"]}

# inserimento documento
persone.insert_one(p1)

# inserimento documento
p2={"nome":"Vaeria","cognome":"Greco","eta":44,"computer":["Apple"]}

# inserimento documento
persone.insert_one(p2)


