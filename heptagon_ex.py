
import turtle

t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)

length = 5
angle = 360 / 7

for i in range(400):
    t.pencolor((i*3) % 255, (i*5) % 255, (i*7) % 255)
    t.forward(length)
    t.left(angle)
    length += 0.8  

turtle.done()
