'''
Created on 12 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

l=[1,2,3,4,5,6,7,8,9]
l1=[n*n for n in l if n%2 ==1]
print(l1)

newGen=(n*n for n in l if n%2 ==1)
print(type(newGen))
for i in newGen:
    print(i)
    
for i in newGen:
    print(i)