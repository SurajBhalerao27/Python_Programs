num = int(input("Enter Number: "))
a,b = 0,1
cnt = 0

if(num < 0):
    print("Input should be a positive integer")
elif(num == 1 ):
    print("Fibonacci is ", num)
else:
    print("Fibonacci Series : ")
    while(cnt < num):
        print(a)
        a, b = b, a + b
        cnt += 1
        