'''
Created on 11 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

print("List comprehension")
l=[1,2,3,4,5,6,7,8,9,10,11]

le=[n*n for n in l if n % 2 ==1]

print(le)