# python3 excersize_pong.py
# python3 -m excersize_pong.py

# Simple Pong in Python 3 for Beginners
# By @TokyoEdTech

# YouTube: https://www.youtube.com/watch?v=XGf2GcyHPhc

"""
Excerises:
(0) Color paddle_a and paddle_b and ball however you like
(1) The ball is way too fast, let's slow it down!
(2) paddle_b is in the center of the board. Put it on the far right.
(3) The score is not even in the beginning. No fair! Make it even.
(4) Player A is using 'w' for up and 'x' for down. Change to 'q' and 'a', repsectively
(5) After a point is scored, the ball starts from the winner's side. We want it to start from the center.
(6) What shape is the ball? Make it a circle.
(7) Make one of the players a circle
"""

import turtle
import os

PLAYER_A_NAME = 'אילן'
PLAYER_B_NAME = 'יקיר'

PADDLE_A_COLOR = 'red'
PADDLE_B_COLOR = 'white'

UP_A = 'w'
DOWN_A = 'x'

X_SPEED = 5
Y_SPEED = 5

X_POS_AFTER_RIGHT = -350
X_POS_AFTER_LEFT = +350

# ----------------------

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 50
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color(PADDLE_A_COLOR)
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color(PADDLE_B_COLOR)
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(0, 0)

# Ball
ball = turtle.Turtle()
#ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2 * X_SPEED
ball.dy = 2 * Y_SPEED

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"{PLAYER_B_NAME}: {score_b} {PLAYER_A_NAME}: {score_a}", align="center", font=("Courier", 24, "normal"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, f"{UP_A}")
wn.onkeypress(paddle_a_down, f"{DOWN_A}")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write(f"{PLAYER_B_NAME}: {score_b}  {PLAYER_A_NAME}: {score_a}", align="center", font=("Courier", 24, "normal"))
        ball.goto(X_POS_AFTER_RIGHT, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write(f"{PLAYER_B_NAME}: {score_b}  {PLAYER_A_NAME}: {score_a}", align="center", font=("Courier", 24, "normal"))
        ball.goto(X_POS_AFTER_LEFT, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1 
        os.system("afplay bounce.wav&")
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")
    