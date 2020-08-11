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

print('Dizionari')
d={'a':1, 'b':2 , 'c':3}
print(type(d))
print('Dizionario       d =',d)
d_vuoto={}
print('Dizionario d_vuoto =',d_vuoto)

d2={(0,10):'Primo intervallo',(11,20):'Secondo intervallo'}
print('Dizionario      d2 =',d2)
print('Dizionario      (0,10) in d2 ?',(0,10) in d2)
print('Dizionario      (1,9) in d2 ?',(1,9) in d2)
print('Dizionario      d2[(0,10)] =',d2[(0,10)])

t=d2.items()
print(type(t))
print

k=d2.keys()
print(type(k))
print(k)

v=d2.values()
print(type(v))
print(v)
