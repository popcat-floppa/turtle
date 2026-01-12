
import turtle

screen = turtle.Screen()
screen.setup(600, 400)
screen.tracer(0)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()

dx, dy = 4, 3
WIDTH, HEIGHT = 600, 400
RADIUS = 10

def move():
    global dx, dy

    x, y = ball.position()

    if x + RADIUS >= WIDTH / 2 or x - RADIUS <= -WIDTH / 2:
        dx *= -1

    if y + RADIUS >= HEIGHT / 2 or y - RADIUS <= -HEIGHT / 2:
        dy *= -1

    ball.goto(x + dx, y + dy)
    screen.update()

    screen.ontimer(move, 16)  # ~60 FPS

move()
turtle.done()
