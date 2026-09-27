# s = 'adsdffdsda'
# n= len(s)
# l = 0
# r = n - 1

# while l < r:
#     if s[l] != s[r]:
#         print("Not a palindrome")
#         break
#     l += 1
#     r -= 1
# else :
#     print("Palindrome")
    
# Using Recursion

s = 'adsdffdsda'

def func(s, l, r):
    if l >= r:
        return True
    if s[l] != s[r]:
        return False
    return func(s, l + 1, r - 1)

function_result = func(s, 0, len(s) - 1)
if function_result:
    print("Palindrome") 
else:
    print("Not a palindrome")