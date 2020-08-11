'''
Created on 11 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

lista=[]

for i in range(10,30,1):
    if not(i % 2) and (i<25):
        lista.append(i)
        
print(lista)