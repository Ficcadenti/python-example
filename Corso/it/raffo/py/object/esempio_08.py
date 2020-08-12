'''
Created on 12 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

class MyClass():
    def __init__(self,my_attr=None):
        self.__priv_attr=my_attr
        
    def get_attr(self):
        return self.__priv_attr

    def set_attr(self,attr):
        self.__priv_attr=attr

    attr = property(get_attr,set_attr)
    
c=MyClass('Python')
print(type(c))

print(c.attr)
c.attr='Ciao'
print(c.attr)
#print(c.priv_attr)
print(c._MyClass__priv_attr)
