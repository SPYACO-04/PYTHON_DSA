lst = [54, 68, 54, 65, 23, 12, 34, 56, 78, 90]

lst.sort()
print(lst)


def binary_search(lst, target):
    l, r = 0, len(lst) - 1

    while l <= r:
        m = (l + r) // 2

        if lst[m] == target:
            return m

        elif lst[m] < target:
            l = m + 1

        else:
            r = m - 1

    return -1


print(binary_search(lst, 65))