'''
Created on 12 ago 2020

@author: raffa
'''

class Conto:        
    def __init__(self, nome=None,conto=None):
        self.__priv_nome=nome
        self.__priv_conto=conto

    @property    
    def nome(self):
        return self.__priv_nome
    
    @nome.setter
    def nome(self,nome):
        self.__priv_nome=nome
        
    @property    
    def conto(self):
        return self.__priv_conto
    
    @conto.setter
    def conto(self,conto):
        self.__priv_conto=conto

class ContoCorrente(Conto):
    def __init__(self, nome=None,conto=None,saldo=None):
        super().__init__(nome, conto)
        self.__priv_saldo=saldo
    
    def preleva(self,importo):
        self.__priv_saldo -= importo
        
    def deposita(self,importo):
        self.__priv_saldo += importo
        
    def descrizione(self):
        print(f"Nome={self.nome}, conto={self.conto}, saldo={self.saldo}")
    
    @property    
    def saldo(self):
        print('Sono nel getter')
        return self.__priv_saldo
    
    @saldo.setter
    def saldo(self,importo):
        print('Sono nel setter')
        self.preleva(self.__priv_saldo)
        self.deposita(importo)
        
class GestoreContiCorrenti:
    @staticmethod
    def bonifico(sorgente,destinazione,importo):
        sorgente.preleva(importo)
        destinazione.deposita(importo) 