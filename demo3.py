import turtle  
# Creating turtle  
t = turtle.Turtle()  
  
c = t.clone()  
t.color("blue")  
c.color("red")  
t.circle(10)  
# c.circle(30)  
for i in range(20, 80, 10):  
    c.circle(i)  
for j in range(90,150,10):
    t.circle(j) 
turtle.mainloop()  