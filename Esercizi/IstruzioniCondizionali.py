#
# <one line to give the program's name and a brief idea of what it does.>
# Copyright (C) 2019  Raffaele <email>
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

print('****************** Istruzioni condizionali *************************')
print('if-elif-else')
n=int(input("Inserisci un numero: "))
if(n%2==0):
    print(n,"è un numero pari")
elif(n%2==1):
    print(n,"è un numero dispari")
    
n = int(input('Inserisci un numero: '))
if n < 0:
    print(n, 'è negativo')
elif n > 0:
    print(n, 'è positivo')
else:
    print(n, 'è zero')
    

