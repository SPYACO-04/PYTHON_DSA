# Method 01 :

nums = [5, 6, 7, 7, 1, 9, 111, 1, 1, 5, 1, 1]
# freq = {}
# for i in range(0, len(nums)):
#     if nums[i] in freq:
#         freq[nums[i]] += 1
#     else:
#         freq[nums[i]] = 1
# print(freq)

# Method 02 :

hash_map = {}
n = len(nums)
for i in range(0, n):
    hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
print(hash_map)