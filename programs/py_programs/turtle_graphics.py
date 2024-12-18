import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.pencolor('green')
t.speed(0)
t.penup()
t.goto(0, 200)
t.pendown()
a = 0
b = 0

while True:
    t.forward(a)
    t.right(b)
    a += 3
    b += 1
    if b == 50000:
        break
    t.hideturtle()

turtle.done()