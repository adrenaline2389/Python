nums = [4, 3, 2, 1]
def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = swap(nums[i],nums[j])
    print(nums)
print(nums)