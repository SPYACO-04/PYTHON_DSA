import array as arr

val = arr.array('i', [1, 2, 3, 4, 5])

for i in val :
    print(i, end = " ")

print('\n')

val.reverse()
print(val.typecode) 