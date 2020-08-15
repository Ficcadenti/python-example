'''
Created on 15 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

  
def generatorFun(): 
    yield 1
    yield 2
    yield 3

def fibonacciFun():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b       
  
for num in fibonacciFun(): 
    if num > 100: 
        break    
    print(num) 
    
for value in generatorFun():  
    print(value) 
    
    
    