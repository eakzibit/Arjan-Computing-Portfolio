from turtle import*
import random


body=random.randint(10,100) #This chooses a random size for the body

pensize(25)     # This draws the stickman
right(90)
forward(body)
left(45)
forward(100)
backward(100)
right(90)
forward(100)
backward(100)
left(45)
backward(body)
right(90)
forward(100)
backward(200)
forward(100)
right(180)
left(90)
forward(40)
right(90)
circle(50)
