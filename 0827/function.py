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
    c = a
    d = b
    return d, c

if __name__ == "__main__":
    print("加减乘除")
    print(pmmd())

    print("update")
    a = 100
    print(update(a))
    print(a)

    print("swap")
    print(swap(3, 4))
