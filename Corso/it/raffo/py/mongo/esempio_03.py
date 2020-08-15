'''
Created on 15 ago 2020

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

# accedo alla collection in testdb
persone = db.persone

filtro={"nome":"Raffaele"}
update={"$set" :{"eta":34}}
print(type(filtro))
print(type(update))

print(filtro)
print(update)

# update document
res = persone.update_one(filtro,update)
print(res)

print('***')
p=persone.find_one(filtro)
print(p)




