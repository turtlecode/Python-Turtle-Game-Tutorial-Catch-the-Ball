import turtle
import random

wn = turtle.Screen()
wn.title("Catch the Ball Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

score = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 260)
pen.color("white")
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

player = turtle.Turtle()
player.shape("square")
player.color("yellow")
player.shapesize(stretch_wid=2, stretch_len=5)  
player.penup()
player.goto(0, -250)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(random.randint(-280, 280), 250)
ball_speed = 5 * 1.10 

def move_left():
    x = player.xcor() - 20
    if x < -280: x = -280
    player.setx(x)

def move_right():
    x = player.xcor() + 20
    if x > 280: x = 280
    player.setx(x)

wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

def game_loop():
    global score, ball_speed
    ball.sety(ball.ycor() - ball_speed)

    if (player.xcor() - 50 < ball.xcor() < player.xcor() + 50) and \
       (player.ycor() - 20 < ball.ycor() < player.ycor() + 20):
        score += 1
        ball_speed *= 1.01  
        pen.clear()
        pen.goto(0, 260)
        pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
        ball.goto(random.randint(-280, 280), 250)

    if ball.ycor() < -300:
        pen.goto(0, 0)
        pen.write("Game Over! Press Q to Restart", align="center", font=("Courier", 24, "normal"))
        return

    wn.update()  
    wn.ontimer(game_loop, 30) 

def restart():
    global score, ball_speed
    score = 0
    ball_speed = 5 * 1.10
    pen.clear()
    pen.goto(0, 260)
    pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))
    ball.goto(random.randint(-280, 280), 250)
    game_loop()

wn.onkeypress(restart, "q")

game_loop()
wn.mainloop()