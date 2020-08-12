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
   print(MyFun(11,2))
   print(MyFun(10,0))
except (ZeroDivisionError,IndexError,Exception) as e:
    print('Generata eccezione: '+str(e.args))
else:
    print('Eseguo la suite solo se non ci sono eccezioni !!!')
finally:
    print('Eseguo comunque la suite Finally !!!')
