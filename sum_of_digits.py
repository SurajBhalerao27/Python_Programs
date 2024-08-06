num = int(input("Enter Number: "))
digit_cnt = 0
sum_of_digits = 0

if num < 0:
    print("Enter positive number")
while num > 0:
    digit = num % 10
    digit_cnt += 1
    sum_of_digits += digit
    num = num // 10

print(f'Digit count of {num} is "{digit_cnt}" and sum of digits is "{sum_of_digits}"')