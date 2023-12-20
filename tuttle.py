def drawSpiral(how_far,how_much):
    if how_far>0:
        t.forward(how_far)
        t.right(how_much)
        drawSpiral(how_far-5,how_much)
import turtle        
turtle.Screen().bgcolor("black")
t=turtle.Turtle()
t.reset()
t.pencolor('green')
c = ["yellow", "red", "pink", "light green", "cyan", "blue"]
t.pen(speed=15)
turtle.delay(10)
lenght=500
turn_by=121
t.penup()
t.setpos(-lenght/2,lenght/2)
t.pendown()

drawSpiral(lenght,turn_by)
