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
# but WITHOUT ANY WARRATY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

lista_vuota=[]
print(lista_vuota)

lista_piena=[1,23,11,4,5,'python']
print(lista_piena)
lista_piena.pop()
print('Lista ordinata')
lista_piena.sort()
print(lista_piena)
print('Lista invertita')
lista_piena.reverse()
print(lista_piena)
print('Primo elemento della lista')
print(lista_piena[0])
print(lista_piena[-1])
print(lista_piena[0:])
print(lista_piena[:-1])
print(lista_piena[0:-1])
print('python' in lista_piena)
print(lista_piena*2)

lista_piena=lista_piena+['b','b','c','d',1]
print(lista_piena.count(1))

print(type(lista_piena))
