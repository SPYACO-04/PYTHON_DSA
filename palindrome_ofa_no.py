n = 121
num = n 
result = 0

while num > 0:
    id = num % 10
    result  = result * 10 + id
    num = num // 10

print(f'Result : {result} is Palindrome: {result == n}')