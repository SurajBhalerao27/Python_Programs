a,b = 88,10
print(f'addition of {a} and {b} is {a+b}') 

# x = int(input("Enter number: "))
# print(f'Square of {x} is {x**2}')

# y = float(input("Enter number: "))
# print(f'the floor division of {y} is {y//2}')

if a > b:
    print("Greater")
else: 
    print("Smaller")
    
str = input("Enter string: ")
print(f'Revered of {str} : {str[::-1]}')

def fact(x):
    if x == 0:
        return 1
    else: 
        return x * fact(x - 1)
    
num = int(input("Enter number: "))
print(f'Factorial of {num} : {fact(num)}')   