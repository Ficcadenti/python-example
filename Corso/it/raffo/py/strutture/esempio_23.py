'''
Created on 11 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

k = 50
def outer():
    k = 20
    def inner():
        nonlocal k
        k = 10
    inner()
    print(k)
outer()