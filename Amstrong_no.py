n = 153
num = n
total = 0
nod = len(str(n))

while num > 0 :
    id = num % 10
    total += id ** nod
    num = num // 10
print(f'Total : {total} is Armstrong: {total == n}')