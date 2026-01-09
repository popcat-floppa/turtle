
import turtle

colours = ["blue", "red"]
t = turtle.Turtle()

t.speed (0.25)

for index in range(167):
    i = int(index % 2)
    print(index)
    t.color(colours[i])
    t.forward(2+index)
    t.rt(30)

turtle.done()
