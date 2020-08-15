'''
Created on 15 ago 2020

@author: raffa
'''

import json
import pymongo as pm
from pymongo import MongoClient
import pprint
from pprint import pprint as bprint

if __name__ == '__main__':
    pass

def pprint(obj):
    print(json.dumps(obj,sort_keys=True, indent=4))

# connessione a mongo
client = MongoClient('localhost',27017)
print(client)

# accediamo al database per crearlo
db = client.testdb

# accedo alla collection in testdb
persone = db.persone

filtro={"nome":{"$gt":"Raffaele"}}
pprint(filtro)

p=persone.find_one(filtro)
bprint(p)