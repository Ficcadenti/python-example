import turtle
#--------------------------
turtle.shape('turtle')
turtle.pencolor('red')
turtle.pensize(3)
turtle.speed(0)
turtle.penup()
turtle.sety(-280)
turtle.pendown()
turtle.left(90)
#--------------------------
def albero(n,d):
    if(n > 0):
        d2=d/RATIO
        turtle.forward(d)
        turtle.left(45)
        albero(n-1,d2)
        turtle.right(90)
        albero(n-1,d2)
        turtle.left(45)
        turtle.backward(d)
#--------------------------
RICORSIONE=9
DISTANZA=250
RATIO=1.65
albero(RICORSIONE,DISTANZA)
turtle.done()