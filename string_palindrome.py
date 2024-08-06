def is_palindrome(string):
    return string == string[::-1]

string = input("Enter string: ")
if is_palindrome(string):
    print("Is palindrome")
else:
    print("Not palindrome")