'''
Created on 13 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

def somma(a,b,c):
    return a+b+c

def mul(a,/,b,c):
    return a*b*c

x=somma(1,2,3) #argomenti posizionali
print(x)

x=somma(b=1,c=2,a=3) #argomenti per key
print(x)

y=mul(1,c=10,b=20)
print(y)