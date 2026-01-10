import turtle
 
def draw_star():
    t = turtle.Turtle()
    t.color('gold')
    t.begin_fill()
    for _ in range(5):
        t.forward(100)
        t.right(144)
    t.end_fill()
    turtle.done()

draw_star()


