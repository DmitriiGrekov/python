import turtle


pen = turtle.Turtle()
pen.up()
pen.setposition(-30,-30)
pen.down()

n=5
def rightMNOG(n,dlina):
    sumAngle=(n-2)*180
    if sumAngle%n==0:

        angle = sumAngle//n
        for i in range(n):
            pen.forward(dlina)
            pen.left(180-angle)




for i in range(3,11):
    rightMNOG(i,50)

input()
