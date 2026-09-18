n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

haslist =[0]*11

for num in n :
    haslist[num] += 1

for num in m :
    if num < 1 or num > 10:
        print(f"Number {num} is out of range.")
    else :
        print(f"Frequency of {num} is {haslist[num]}") 