'''
Created on 12 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

class MyClass:
    def __new__(cls,messae):
        istanza=super().__new__(cls)
        print('__new__')
        return istanza
        
    def __init__(self,message):
        self.message=message
        print('__init__: '+str(self.message))
        
        
obj=MyClass('Python')
        