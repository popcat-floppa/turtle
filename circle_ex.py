
import turtle
def draw_circle():
    t = turtle.Turtle()
    t.circle(50)
    #turtle.done()

def concentric_circles():
    t = turtle.Turtle()
    t.speed(0)

    for i in range(10):
        t.penup()
        t.goto(0, 0 * i)
        t.pendown()
        t.circle(20 * i)
        
draw_circle()
concentric_circles()

turtle.done()
