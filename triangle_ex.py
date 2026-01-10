
import turtle

colours = ["blue", "red"]
t = turtle.Turtle()

t.speed (0.25)

for index in range(141):
    i = int(index % 2)
    print(index)
    t.color(colours[i])
    t.forward(50+index*4)
    t.rt(120)

turtle.done()
