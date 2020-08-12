'''
Created on 12 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

class MyClass():
    def __init__(self,my_attr=None):
        self.__priv_attr=my_attr
    
    @property    
    def attr(self):
        return self.__priv_attr
    
    @attr.setter
    def attr(self,attr):
        self.__priv_attr=attr


c=MyClass('Python')
print(type(c))

print(c.attr)
c.attr='Ciao'
print(c.attr)
#print(c.priv_attr)
print(c._MyClass__priv_attr)