
import turtle
def draw_checkerboard():
    t = turtle.Turtle()
    t.speed(0)
    square_size = 30

    for row in range(8):
        for col in range(8):
            t.penup()
            t.goto(col * square_size, row * square_size)
            t.pendown()

            if (row + col) % 2 == 0:
                t.begin_fill()
            for _ in range(4):
                t.forward(square_size)
                t.right(90)
            if (row + col) % 2 == 0:
                t.end_fill()

draw_checkerboard()

turtle.done()
