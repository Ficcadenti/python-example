'''
Created on 15 ago 2020

@author: raffa
'''

if __name__ == '__main__':
    pass


def alternateCase(s):
    # your code here
    return s.swapcase()

def open_or_senior(data):
    lo=[]
    for e in data:
        if(e[0]>=55 and e[1]>7):
            print(e)
            lo.append("Senior")
        else:
            lo.append("Open")
    return lo
        
def persistence(n):
    # your code
    count=0
    while(n//10>0):
        count+=1
        s=str(n)
        tot=1;
        for c in s:
            tot=tot*int(c)
            
        n=tot 
    
    return count

def solution(string, ending):
    return string.endswith(ending)

def filter_list(l):
    lo=[]
    for e in l:
        if(isinstance(e,int)):
            lo.append(e);
    return lo

def even_or_odd(number):
    if (number % 2) == 1:
        return 'Even';
    else:
        return 'Odd'   

def high_lambda(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
    
def high(x):
    listaStr = x.split(" ")
    tot = 0;
    max = 0;
    s ='';
    for s in listaStr:
        for ch in s:
            print(ch,':',ord(ch),',',ord('a'),((ord(ch)-ord('a'))+1) )
            tot=tot+((ord(ch)-ord('a'))+1)
            
        print("parola: ",s," tot: ",tot)
        if(tot>max):
            max=tot
            str=s
        
        tot=0    
    
    print("max: ",max," parola: ",str)
    return str
    
print("Data Science")
print(alternateCase('Ciao'))

l=[[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]

print(open_or_senior(l))

print(persistence(999))
print(solution('Raffaele','le'))

print(filter_list([1,2,'a','b']))

print(high('gabriele ficcadenti w'))
print(high_lambda('gabriele ficcadenti w'))