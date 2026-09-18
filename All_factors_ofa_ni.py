
# num = 102
# result = []
# for i in range(1, num + 1):
#     if num % i == 0:
#         result.append(i)
# print(f'Factors of {num} are: {result}')

# Better solution

# result = []
# num = 102
# for i in range (1, num + 1):
#     if num % i == 0:
#         result.append(i)
# result.append(num)
# print(f'Factors of {num} are: {result}')

#  optimal solution 

import math 
import sys
result = []
num = 102
for i in range(1, int(math.sqrt(num)) + 1):
    if num % i == 0:
        result.append(i)
        if i != num // i:
            result.append(num // i)
print(f'Factors of {num} are: {sorted(result)}')