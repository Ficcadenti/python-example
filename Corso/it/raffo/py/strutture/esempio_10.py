'''
Created on 11 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

l=[x for x in range(10,30) if not(x % 2) and (x<25)]

print(l)

my_list = []
 
for x in range(10):
    my_list.append(x**2)
 
my_list2 = [x**2 for x in range(10)]
print(my_list)
print(my_list2)