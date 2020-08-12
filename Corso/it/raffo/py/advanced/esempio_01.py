'''
Created on 12 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

class MyClass:
    pass

myObj=MyClass()

print('MyClass :' + str(type(MyClass)))
print('MyClass :' + str(type(myObj)))

print(isinstance(myObj, MyClass))
print(isinstance(MyClass, object))
print(isinstance(myObj, object))
print(isinstance(MyClass, type))
print(isinstance(myObj, type))
print(isinstance(object, object))
print(isinstance(type, type))
print(isinstance(object, type))
print(isinstance(type, object))