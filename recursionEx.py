# def greet():
#     print('hello')
#     greet()
# greet()

# Head Recursion

# def ex(count):
    
#     if count == 4:
#         return

#     print("suraj")
    
#     ex(count + 1)

# ex(0)

# Tail Recursion

# def ex2(count):
#     if count == 4:
#         return

#     ex2(count + 1)
    
#     print("suraj")
    
# ex2(0) 

# Recursion using parameters

# def ex3(x, n):
#     if n == 0:
#         return
#     print(x)
#     ex3(x, n - 1)
    
# ex3(15, 4)

def func(i, n):
    if i > n:
        return
    print(i)
    func(i + 1, n)
    
func(1, 4)