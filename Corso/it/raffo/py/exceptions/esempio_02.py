'''
Created on 12 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

#eccezioni

def MyFun(a,b):
    return a //b


try:
   print(MyFun(10,2))
   print(MyFun(10,0))
except ZeroDivisionError as e:
    print('Generata eccezione: '+str(e))
except IndexError as e:
    print('Generata eccezione: '+str(e))