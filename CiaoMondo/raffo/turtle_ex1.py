'''
Created on 15 nov 2019

@author: raffa
'''

from turtle import Turtle, Screen

tartaruga = Turtle()
sfondo = Screen()


sfondo.colormode(255)

R = 255
G = 0
B = 0
sfondo.bgcolor((0, 0, 255))

tartaruga.speed(10)

colours = []

while G < 255:
    colours.append((R, G, B))
    G += 1
while R >= 0:
    colours.append((R, G, B))
    R -= 1
while B < 255:
    colours.append((R, G, B))
    B += 1
while G > 0:
    colours.append((R, G, B))
    G -= 1
while R < 255:
    colours.append((R, G, B))
    R += 1

for i in range(3000):
    # La riga seguente fa cambiare di continuo il colore, anche se i e maggiore del numero di colori presenti nella lista
    tartaruga.color(colours[i % len(colours)])
    tartaruga.forward(i/3)
    tartaruga.right(119)
