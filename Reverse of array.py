# Base Case :

# nums = [2,23,45,7,56,2,3,42,2,34,6,7]

# left = 0
# right = len(nums) - 1

# while left < right :
#     nums[left], nums[right] = nums[right], nums[left]
#     left += 1
#     right -= 1
# print(nums)

# Using Recursion :

def func(nums, left, right):
    if left >= right:
        return nums

    nums[left], nums[right] = nums[right], nums[left]

    return func(nums, left + 1, right - 1)


nums = [1, 2, 3, 4, 5]

print(func(nums, 0, len(nums) - 1))