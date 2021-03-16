
# import
import turtle

# Window Information
window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Pad 0 information
pad_0 = turtle.Turtle()
pad_0.speed(0)
pad_0.shape("square")
pad_0.color("green")
pad_0.penup()
pad_0.goto(-350,0)

# Pad 1 information
pad_1 = turtle.Turtle()
pad_1.speed(0)
pad_1.shape("square")
pad_1.color("green")
pad_1.penup()
pad_1.goto(350,0)

# Ball
pad_0 = turtle.Turtle()
pad_0.speed(0)
pad_0.shape("circle")
pad_0.color("yellow")
pad_0.penup()
pad_0.goto(0,0)


# Main game information
while True:
    window.update()