import turtle

window = turtle.Screen()
window.bgcolor('black')
turtle.color('red')
turtle.penup()
speed = 1
LASER_LENGTH = 20
LASER_SPEED = 10
lasers = []

window.onkey(turtle.forward(40), 'Up')
window.onkey(turtle.left(90), 'Left')
window.onkey(turtle.right(90), 'Right')
window.onkey(turtle.backward(40), 'Down')
window.listen()


window.mainloop()




























             
