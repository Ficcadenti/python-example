'''
Created on 18 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

# funzione lambda

def square(x):
    return x**2

sq2= lambda x : x**2

num=[1,2,3,4,5]
print(num)
print(square(5))


num_square=list(map(square,num))
print(num_square)

num_square=list(map(sq2,num))
print(num_square)
