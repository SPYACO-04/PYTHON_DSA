nums = [5,1,6,8,2,4,9]

n = len(nums)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print(nums)