'''
Created on 16 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass


# dada science

# liste
print('Data science')
x=[1,2,3]
print(id(x))
print(type(x))
print(x*2)
print(dir(x))
x.extend([11,6,7,8,9])
print(x)

t=('a',1,'b',2.5)
print(type(t))
print(t[0])

# dizionario
dict1={'Raffaele':178,'Valeria':168}
print(type(dict1))
print(dict1)
print(dict1['Valeria'])
dict1['Gabriele']=120
dict1['Sofia']=160
dict1['Maria']=140


print(dict1)
print(dict1.keys())
print(dict1.values())

del(dict1['Raffaele'])
print(dict1)

print(len(dict1))
print(dir(dict1))

# set

set1={1,2,3,5,5}
print(type(set1))
print(set1)
print(len(set1))
# print(set1[0]) errore
print(2 in set1)
print(21 in set1)

set2={1,1,1,1,1,2,2,2,2,2}
print(set2)

# Stringhe
str1='Raffaele & Valeria'
str2=' ciao !!!'
print(type(str1))
print(str1)
print(str1+str2)
print(str1[0])
print(str1*2)

str3="""Raffaele
Valeria
Gabriele
Sofia
Maria"""
print(str3)
print(len(str3))
print(dir(str3))
print(str1[:5])
print(str1[-1])
print(str1.upper())
print(str1.find('Val'))
print(str1.replace('a', '-'))
print(str1)
print(str1.split())