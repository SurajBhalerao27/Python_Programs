## Fibonacci series - 0 1 1 2 3 5 8 13 so on 

a,b = 0,1
while a<50:
    # print(a) # This prints the element in order 
    print(a, end = ", ") # By the use of this 'end= ' it will print the elements with the end with semicolon at end.
    a,b = b, a+b