import turtle
t = turtle.Turtle()
turtle.Screen().bgcolor("black")
t.speed(0)
c = ["yellow", "red", "pink", "light green", "cyan", "blue"]
for i in range(200):
    t.pencolor(c[i % 6])
    t.circle(190-i/2, 90)
    t.left(90)
    t.circle(190-i/3, 90)
    t.left(60)
turtle.done()
