import turtle
import os

# Das erstellen des Feldes des namens und der höhe und breite 

wn = turtle.Screen()
wn.title("Elio isch behindert")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Erstellen der Variablen für die Scores

score_a = 0
score_b = 0

# Erstellen der Schläger des Linken Spielers

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Erstellen der Schläger des Rechten Spielers

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Erstellen des Balles welcher auf dem screen rumfliegt

ball = turtle.Turtle()
ball.speed(200)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = 4

# Erstellen des Scoreboardes

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Alec: 0  Arjun: 0", align="center", font=("Courier", 24, "normal"))

# Alle Variablen zur bewegung der Schläger

def paddle_a_up():
    y = paddle_a.ycor()
    y += 40
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 40
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 40
    paddle_b.sety(y)

# Die Tasten zum spielen des Spieles

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

template = False

# Eigentlicher Start des Spieles mit der While schlaufe

while not template:
    counter = 1
    wn.update()
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay click.mp3&") # Das abspielen des soundes (welches nicht über github funktioniert da man keine audiodateien ablegen kann)
        ball.dx += 2
        ball.dy += 2
        counter + 1
       

    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay click.mp3&")
        ball.dx += 2
        ball.dy += 2
        counter + 1
        

    elif ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Alec: {}  Arjun: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        counter + 1
        if score_a == '10':
            template = True

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Alec: {}  Arjun: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        counter + 1
        if score_a == '10':
            template = True

    elif ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1 
        os.system("afplay click.mp3&")
        counter + 1
        if score_a== '10':
            template = True
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        os.system("afplay click.mp3&")
        counter + 1
        if score_a == '10':
            template = True

    elif score_a == 10:
        template = True

    elif score_b == 10:
        template = True
