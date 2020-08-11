'''
Created on 11 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

def sum(a,b):
    return a+b

def none(*args):
    return

def none_def(*args):
    print(args)
    
print(sum(1,2))
print(none(1,2,3,4,5,6,7))
print(none_def(0,0,0,0))