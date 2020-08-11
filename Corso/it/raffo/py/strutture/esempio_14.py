'''
Created on 11 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

def stampa(*args):
    print(type(args))
    print(args)
    
def stampa_pos(a,b,*args):
    print(type(a))
    print(type(b))
    print(type(args))
    print(a,b,args)
    

def stampa_dict(**kargs):
    print(type(kargs))
    print(kargs)
    
stampa(1,2,3,4,5,6)
stampa_pos(1,2,3,4,5,6)
stampa_dict(a=1,b=2,c=3)
