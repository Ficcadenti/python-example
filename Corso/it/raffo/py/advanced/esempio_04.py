'''
Created on 12 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass

class MyIterator:
    def __iter__(self):
        self.myattr=2
        return self;
    
    def __next__(self):
        if self.myattr < 300:
            n=self.myattr
            self.myattr*=2
            return n
        else:
            raise StopIteration
        

myclass=MyIterator()
myiter=iter(myclass)


for i in myiter:
    print(i)
    
