
import turtle

colours = ["orange", "red", "green"]
t = turtle.Turtle()

t.speed (0.25)

for index in range(141):
    i = int(index % 3)
    print(index)
    t.color(colours[i])
    t.forward(10+index*4)
    t.rt(90)

turtle.done()
