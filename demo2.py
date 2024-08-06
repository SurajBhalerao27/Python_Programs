import turtle  
# Creating turtle turtle  
t = turtle.Turtle()  

# Setting title to turtle
turtle.title("Mr Suraj")  

# turtle.screensize()  
turtle.screensize(500,1000)  
# turtle.screensize()  
  

# t.shapesize(3,3,3)  
t.color("Red", "Green")
t.begin_fill()  
t.speed(3) 
t.fd(100)  
t.lt(120)  
t.fd(100) 
t.speed(0.7)  
t.rt(120)  
t.fd(100)  
t.rt(120)  
t.fd(100) 
t.rt(120) 
t.fd(100)
t.lt(120)  
t.fd(100) 
t.circle(-60) 
t.end_fill() 

turtle.mainloop()  