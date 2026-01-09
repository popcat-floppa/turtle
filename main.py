import turtle

colours = ["purple", "cyan", "green"]
t = turtle.Turtle()
t.speed (0.2)

for index in range(300):
    i = int(index % 3)
    print(index)
    t.color(colours[i])
    t.forward(10+index)
    t.rt(60)

turtle.done()
            
               
