'''
Created on 11 ago 2020

@author: raffa
'''
import _struct

if __name__ == '__main__':
    pass


def stampa(str1,str2):
    print(f"str1={str1};str2={str2}")
    
def stampa_opt(str1,str2="Raffo"):
    print(f"str1={str1};str2={str2}")

stampa('Ciao','raffo')
stampa(str2='raffo',str1='Ciao')
stampa_opt('Ciao')
stampa_opt('Ciao','Valeria')