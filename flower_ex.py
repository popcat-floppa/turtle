
import turtle

def draw_flower():
    t = turtle.Turtle()
    t.speed(0)
    for _ in range(36):
        t.circle(50)
        t.right(10)

draw_flower()

turtle.done()
