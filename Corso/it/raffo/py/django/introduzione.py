from dataclasses import dataclass


@dataclass(init=True, repr=True, order=True, frozen=False)
class Gatto:
    nome: str
    anni: int

@dataclass(init=True, repr=False, order=True, frozen=False)
class Persona:
    nome: str
    cognome: str
    anno: int
    residenza: str

    def profilo_personale(self):
        print(f"nome={self.nome} cognome={self.cognome} anno={self.anno} residenza={self.residenza}")

    def __str__(self):
        return f"nome={self.nome}\ncognome={self.cognome}\n";

@dataclass(init=True, repr=False, order=True, frozen=False)
class Sviluppatore(Persona):
    posizione: str
    paga_annua: int

    def __str__(self):
        return super().__str__() + f"posizione={self.posizione}\npaga_annua={self.paga_annua}\n";


def funzione_decoratore(f_param):
    def wrapper():
        print('...prima di f_param()')
        f_param();
        print('...dopo f_param()')
    return wrapper

@funzione_decoratore
def mia_func():
    print('Ciao Raffaele')

spam='spam! spam! spam!'
print(type(spam))

g=Gatto(nome='palla',anni=5)
g1=Gatto(nome='palla',anni=5)
g.nome='cssds'
print(id(g))
print(id(g1))

p=Persona('Raffaele','Ficcadenti',1976,'ROMA')
print(p)
p.profilo_personale()

s=Sviluppatore('Raffaele','Ficcadenti',1976,'ROMA','Python',40000)
print("Sviluppatore:\n",s)

#mia_func=funzione_decoratore(mia_func)
mia_func()