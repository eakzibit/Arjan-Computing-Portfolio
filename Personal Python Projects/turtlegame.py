import turtle

turtle.penup()


def up():
    turtle.forward(40)


def down():
    turtle.backward(40)


def right():
    turtle.right(90)

def left():
    turtle.left(90)

def laser():
    laser=turtle.clone()
    laser.forward(1110000000001001100100)
    laser.ht()


turtle.onkey(up,'Up')
turtle.onkey(down,'Down')
turtle.onkey(right,'Right')
turtle.onkey(left,'Left')
turtle.onkey(laser,'space')
turtle.listen()

