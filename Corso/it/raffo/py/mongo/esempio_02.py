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

p = persone.find_one()
print(type(p))
print(p)
print(p['_id'])
print(p['nome'])
print(p['cognome'])

print('***')
p=persone.find({"computer":"Apple"})
for e in p:
    print(e)



