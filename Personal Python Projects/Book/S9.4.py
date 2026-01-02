from turtle import*


def drawpolygon(sides):  #This draws the polygon
    for i in range(sides):
          forward(100)
          left(360/sides)


def drawstar(points):   #This draws the star and asks how many points you want.
    for i in range(points):
        forward(100)
        left(360/points)
        forward(100)
        right(720/points)





pensize(10)

print("Choose a shape to see:\n1.polygon\n2.Star\n3.circle" )
shape=int(input("input number of shape ")) 
if shape==1:                # This runs the functions based on the users input
 sides=int(input("how many sides? "))
 drawpolygon(sides)  
if shape==2:
  points=int(input("how many points do you want? "))
  drawstar(points)
if shape==3: #This draws the circle
   circle(100)
    
  
