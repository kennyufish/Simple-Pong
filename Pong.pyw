# Simple Pong Game without pygame

import turtle
import time

wn = turtle.Screen()
wn.title("Simple Pong @TszKinYu")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Lines
line = turtle.Turtle()
line.speed(0)  # Animation Speed
line.shape("square")
line.color("white")
line.shapesize(stretch_wid=200, stretch_len=0.05)
line.penup()
line.goto(0, 0)

# Start Game / Pause Game
start_game = turtle.Turtle()
start_game.color("white")
start_game.penup()
start_game.hideturtle()
start_game.goto(0, -150)
start_game.write("Press Space to Start", align="center", font=("Courier", 35, "bold"))
start_game_bool = False
global pause_bool
pause_bool = False



# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # Animation Speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0
ball.dy = 0

# Score
score_a = 0
score_b = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 200)
pen.write("Player 1       Player 2 \n    {}              {}".format(score_a, score_b), align="center",
          font=("Courier", 24, "italic"))


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    if (paddle_a.ycor() <= +250):
        y += 40
        paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if (paddle_a.ycor() >= -200):
        y -= 40
        paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    if (paddle_b.ycor() <= 250):
        y += 40
        paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if (paddle_b.ycor() >= -200):
        y -= 40
        paddle_b.sety(y)


def start_game_enter():
    if not start_game_bool:
        start_game.clear()
        ball.dx = 0.20
        ball.dy = -0.20


def esc_pause():
    global temp_ball_dx
    global temp_ball_dy
    global pause_bool
    if not pause_bool:
        temp_ball_dx = ball.dx
        temp_ball_dy = ball.dy
        ball.dx = 0
        ball.dy = 0
        start_game.goto(0, 0)
        start_game.write("PAUSE", align="center", font=("Courier", 35, "bold"))
        pause_bool = True
    else:
        start_game.clear()
        ball.dx = temp_ball_dx
        ball.dy = temp_ball_dy
        pause_bool = False


# Keyboard Binding
wn.listen()
wn.onkeypress(start_game_enter, "space")
wn.onkeypress(esc_pause, "Escape")
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

try:
    # Main Game Loop
    while True:
        wn.update()



        # Move The Ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border Checking
        if abs(ball.ycor()) > 300:
            ball.dy *= -1
        if abs(ball.xcor()) > 390:
            pen.goto(0, 0)
            if ball.xcor() < 0:
                score_b += 1
                pen.write("Player 2 Scores!", align="center", font=("Courier", 36, "bold"))
            else:
                score_a += 1
                pen.write("Player 1 Scores!", align="center", font=("Courier", 36, "bold"))
            time.sleep(0.75)
            if (score_b >= 7 or score_a >= 7):
                pen.clear()
                pen.goto(0, 200)
                if (score_b >=7):
                    pen.write("Player 2 Wins!", align="center", font=("Courier", 36, "bold"))
                else:
                    pen.write("Player 1 Wins!", align="center", font=("Courier", 36, "bold"))
                score_a = 0
                score_b = 0
                time.sleep(1)
            ball.goto(0, 0)
            ball.dx = (ball.dx / abs(ball.dx)) * 0.20
            ball.dy *= 1
            pen.clear()
            pen.goto(0, 200)
            pen.write("Player 1       Player 2 \n    {}              {}".format(score_a, score_b), align="center",
                      font=("Courier", 24, "italic"))



        # Paddle and Ball Collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (
                ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1.1
        if (ball.xcor() < -340 and ball.xcor() > -350) and (
                ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1.1
except:
    print("An exception occurred")