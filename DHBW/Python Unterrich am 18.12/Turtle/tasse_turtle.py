import turtle

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Turtle")
t = turtle.Turtle()
t.speed(10)
t.hideturtle

def tasse():
    t.right(90)
    t.forward(40)
    for i in range(18):
        t.right(5)
        t.forward(2)

    t.forward(30)

    for j in range(18):
        t.right(5)
        t.forward(2)

    t.forward(40)


def henkel():
    t.right(180)
    t.forward(10)
    t.right(90)
    for i in range(62):
        t.forward(1)
        t.left(3)
    







tasse()
henkel()
turtle.done()