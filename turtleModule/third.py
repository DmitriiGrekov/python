import turtle




joe = turtle.Turtle()


def startFILL(n,dlina):
    joe.begin_fill()
    star(n,dlina)
    joe.end_fill()




def star(n,dlina):
    if n%2!=0:
        for i in range(n):
            joe.forward(dlina)
            angle=n//2*360/n
            joe.left(angle)



joe.color('yellow')
startFILL(5,50)
input()