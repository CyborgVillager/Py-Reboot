# import
import turtle

# Window Information
window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)


# Score
score_a = 0
score_b = 0

# Pad 0 Info Start
pad_0 = turtle.Turtle()
pad_0.speed(0)
pad_0.shape("square")
pad_0.color("green")
pad_0.shapesize(stretch_wid=5, stretch_len=1)
pad_0.penup()
pad_0.goto(-350, 0)
# Pad 0 Info End

# Pen ScoreBoard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1: 0 Player 2: 0", align="center", font=("Courier",24,"normal"))

# Pad 1 Info Start
pad_1 = turtle.Turtle()
pad_1.speed(0)
pad_1.shape("square")
pad_1.color("green")
pad_1.shapesize(stretch_wid=5, stretch_len=1)
pad_1.penup()
pad_1.goto(350, 0)
# Pad 1 Info End

# Ball Info Start
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.changex = .3 # ball speed moves by 2 pixels on x cord
ball.changey = -.3 # ball speed moves by 2 pixels on y cord

# Ball Info End


# MOVEMENT INFORMATION BEGINS
# Pad 0 Movement
def pad0_up():
    y = pad_0.ycor()
    if y > 260:
        y = -240
    else:
        y += 30
    # print(y)
    pad_0.sety(y)
def pad_0_down():
    y = pad_0.ycor()
    if y < -240:
        y = 260
    else:
        y -= 30
    # print(y)
    pad_0.sety(y)
# Pad 0 Movement End
# Pad 1 Movement Start
def pad_1_up():
    y = pad_1.ycor()
    if y > 260:
        y = -240
    else:
        y += 30
    pad_1.sety(y)

def pad_1_down():
    y = pad_1.ycor()
    if y < -240:
        y = 260
    else:
        y -= 30
    pad_1.sety(y)
# Pad 1 Movement End
# MOVEMENT INFORMATION ENDS


# Keyboard Binds
window.listen()
window.onkeypress(pad0_up, "w")
window.onkeypress(pad_0_down, 's') # When user presses s, call pad
window.onkeypress(pad_1_up, 'Up')
window.onkeypress(pad_1_down, 'Down')

# Main game information
while True:
    window.update()
    # ball movement
    ball.setx(ball.xcor() + ball.changex)
    ball.sety(ball.ycor() + ball.changey)

    # Game Border Check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.changey *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.changey *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.changex *= -1
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.changex *= -1



    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.changex *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.changex *= -1

    # Pads / Ball Collision
    # Pad 0
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < pad_0 .ycor() + 40 and ball.ycor() > pad_0 .ycor() - 40):
        ball.setx(-340)  # if ball ends up behind paddle, put it in front right away to prevent getting stuck
        ball.changex *= -1
    # Pad 1
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pad_1.ycor() + 40 and ball.ycor() > pad_1.ycor() - 40):
        ball.setx(340)  # if ball ends up behind paddle, put it in front right away to prevent getting stuck
        ball.changex *= -1





