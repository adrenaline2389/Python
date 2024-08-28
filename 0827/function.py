def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiple(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else :
        return 'ERROR'

def pmmd():
    a = plus(10, 1)
    b = minus(10, 1)
    c = multiple(10, 1)
    d = divide(10, 0)
    return a, b, c, d

def update(a):
    a *= 2
    return a

def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

def rectangle(a, b):
    return a * b

def circle(c):
    return c**2*3.14

def sort(nums):
    n = len(nums)
    for i in range(0, n):
        for j in range(i + 1,n):
            if nums[i] > nums[j]:
                # nums[i], nums[j] = swap(nums[i], nums[j])
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
    return nums

if __name__ == "__main__":
    print("加减乘除")
    print(pmmd())

    print("update")
    a = 100
    print(update(a))
    print(a)

    print("swap")
    a = 3
    b = 4
    a, b = swap(a, b)
    print(a, b)

    print(rectangle(3, 4))
    print(circle(5))

    nums = [4, 3, 2, 1]
    print(nums)
    print(sort(nums))
    nums.sort()
