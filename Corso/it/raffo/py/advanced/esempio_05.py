'''
Created on 12 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

def get_doppio_gen():
    e=2
    while(True):
        yield e
        e*=2
        if(e>=300):
            return
        

gen=get_doppio_gen()
print(gen)        

for i in gen:
    print(i)
    