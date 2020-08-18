'''
Created on 16 ago 2020

@author: raffa
'''
import string
import itertools as iter

if __name__ == '__main__':
    pass

def monkey_count(n):
    return list(range(1,n+1))

def valid_parentheses(string):
    pila = []
    for s in string:
        if(s == '('):
            pila.append(s)
        elif(s == ')'):
            try:
                pila.pop()
            except:
                return False

    if(len(pila) == 0):
        return True
    else:
        return False
    
def add_binary(a,b):
    return str(bin(a+b))[2:]

def is_divisible(n,x,y):
    return ( n%x==0 and n%y==0)

def sum_two_smallest_numbers(numbers):
    x=min(numbers)
    numbers.remove(x)
    y=min(numbers)
    return x+y
    
def count(string):
    d={}
    for c in string:
        if c in d:
            d[c]+=1
        else:
            d[c]=1
    return d


def extract_domain(url):
    try:
        print("index: ",url.index('//'))
        str=url[url.index('//')+2:]
        if('www' in str):
            str=url[url.index('www')+4:]
        str=str[:str.index('.')]
        return str  
    except Exception as e:
        if('www' in url):
            str=url[url.index('www')+4:]
            str=str[:str.index('.')]
        else:
            str=url[:url.index('.')]
        return str 
    
def high_and_low(numbers):
    nn = [int(s) for s in numbers.split(' ')]
    return '%i %i' % (max(nn),min(nn))

def camel_case(string):
    #your code here
    return ''.join([s.capitalize() for s in string.split(' ')])

def next_smaller(n):
    
    n = list(str(n))
    
    if len(n) == 1:
        return -1
    
    i = len(n) - 1
    while n[i-1] <= n[i]:
        i -= 1
        if i == 0:
            return -1
    
    primo, ultimo = n[:i-1], n[i-1:]
    
    cifra_da_muovere = max([x for x in n[i:] if x < n[i-1]])
    
    ultimo.remove(cifra_da_muovere)
    ultimo = sorted(ultimo, reverse=True)
    ultimo.insert(0, cifra_da_muovere)
    
    if (not len(primo) and ultimo[0] == '0'):
        return -1
    
    return int(''.join(primo + ultimo))

def solution(nums):
    if(nums != None):
        print(nums)
        nums.sort()
    return nums

def solve(s):
    up=sum(1 for c in s if c.isupper())
    down=sum(1 for c in s if c.islower())
    if(up>down):
        return s.upper()
    else:
        return s.lower()
    
def get_pins(observed):
    dict = {
            '0': ['0', '8'],
            '1': ['1', '2', '4'],
            '2': ['1', '2', '3', '5'],
            '3': ['2', '3', '6'],
            '4': ['1', '4', '5', '7'],
            '5': ['2', '4', '5', '6', '8'],
            '6': ['3', '5', '6', '9'],
            '7': ['4', '7', '8'],
            '8': ['5', '7', '8', '9', '0'],
            '9': ['6', '8', '9']
    }
    
    numeri = []
    
    for c in str(observed):
        numeri.append(dict[c])
    
    pins = [''.join(pin) for pin in list(iter.product(*numeri))]
    
    return sorted(pins)

    
print(monkey_count(20))
print(valid_parentheses('(())((()())())('))
print(add_binary(3,5))
print(bin(4))
print(is_divisible(5,1,4))


print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))
print(count('Raffaele'))

print("Dominio :",extract_domain("icann.org"))

print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
print(camel_case('ciao gabriele'))

print(next_smaller(21))




l=[1,3,7,5,4]
print(solution(None))

print(solve("CODe"))

print(get_pins('2'))
