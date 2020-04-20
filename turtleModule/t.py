import turtle



joe = turtle.Turtle()
joe.speed(20)
def sq(a):

    for i in range(4):
        joe.color(colors[i%4])
        joe.forward(a)
        joe.left(90)


dlina = 30
colors = ['red','brown','green','blue']

for i in range(60):
#    sq(dlina)
    joe.circle(dlina)
    joe.right(10)
    dlina+=4
input()

