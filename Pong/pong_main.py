
# import
import turtle

# Window Information
window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

def pad0():
    pad_0 = turtle.Turtle()
    pad_0.speed(0)
    pad_0.shape("square")
    pad_0.color("green")
    pad_0.shapesize(stretch_wid=5, stretch_len=1)
    pad_0.penup()
    pad_0.goto(-350, 0)

def pad1():
    pad_1 = turtle.Turtle()
    pad_1.speed(0)
    pad_1.shape("square")
    pad_1.color("green")
    pad_1.shapesize(stretch_wid=5, stretch_len=1)
    pad_1.penup()
    pad_1.goto(350, 0)

def ball():
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("yellow")
    ball.penup()
    ball.goto(0, 0)


# Pad 0 information
pad0()
# Pad 1 information
pad1()
# Ball
ball()


# Main game information
while True:
    window.update()