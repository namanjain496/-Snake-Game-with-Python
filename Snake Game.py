import turtle
import random

w = 500
h = 500
fs = 10
d = 100  # milliseconds

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def r():
    global snake, cross, sec, pen
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    cross = "up"
    sec = nun()
    food.goto(sec)
    hall()

def hall():
    global cross

    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[cross][0]
    new_head[1] = snake[-1][1] + offsets[cross][1]

    if new_head in snake[:-1]:
        r()
    else:
        snake.append(new_head)

        if not eat():
            snake.pop(0)

        if snake[-1][0] > w / 2:
            snake[-1][0] -= w
        elif snake[-1][0] < - w / 2:
            snake[-1][0] += w
        elif snake[-1][1] > h / 2:
            snake[-1][1] -= h
        elif snake[-1][1] < -h / 2:
            snake[-1][1] += h

        pen.clearstamps()
 #clears all the stamps

        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()

        screen.update()
 #updates the turtle.screen screen

        turtle.ontimer(hall, d)

def eat():
    global sec
    if dist(snake[-1], sec) < 20:
        sec = nun()
        food.goto(sec)
        return True
    return False

def nun():
    x = random.randint(- w / 2 + fs, w / 2 - fs)
    y = random.randint(- h / 2 + fs, h / 2 - fs)
    return (x, y)

def dist(poos1, poos2):
    x1, y1 = poos1
    x2, y2 = poos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

def mov():
    global cross
    if cross != "down":
        cross = "up"

def go_right():
    global cross
    if cross != "left":
        cross = "right"

def go_down():
    global cross
    if cross != "up":
        cross = "down"

def go_left():
    global cross
    if cross != "right":
        cross = "left"

screen = turtle.Screen()
screen.setup(w, h)
screen.title("Snake Game")
screen.bgcolor("green")
screen.setup(500, 500)
screen.tracer(0)

pen = turtle.Turtle("square")
pen.penup()

food = turtle.Turtle()
food.shape("circle")
food.color("white")
food.shapesize(fs / 20)
food.penup()

screen.listen()
screen.onkey(mov, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

r()
turtle.done()