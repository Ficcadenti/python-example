'''
Created on 12 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass


ls=[1,2,3]

e = 6 in ls
print(e)

e = 3 in ls
print(e)

it_ls=iter(ls)
print(type(ls))
print(type(it_ls))

print(next(it_ls))
print(next(it_ls))
print(next(it_ls))
print(next(it_ls))
