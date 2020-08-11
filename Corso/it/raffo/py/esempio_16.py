'''
Created on 11 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

def funzione_imm(x):
    print(f"Prima {x}")
    x=10
    print(f"Dopo {x}")   
    
    
def funzione_mut(x):
    print(f"Prima {x}")
    x[0]=10
    print(f"Dopo {x}")    
 
  
a=15
funzione_imm(a)
print(a)   

a=[0,1,2,3]
funzione_mut(a)
print(a) 
