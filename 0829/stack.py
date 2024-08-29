import sys

stack = []

for line in sys.stdin:
    line = line.strip()
    if line == "q":
        if len(stack) != 0:
            print(stack.pop())
        break
    # print(line)
    if line.isdigit():
        num = int(line)
        stack.append(num)
        print(stack)
    else:
        a = stack.pop()
        b = stack.pop()
        if line == "+":
            stack.append(b + a)
            print(stack)
        if line == "-":
            stack.append(b - a)
            print(stack)
        if line == "*":
            stack.append(b * a)
            print(stack)
        if line == "/":
            stack.append(b / a)
            print(stack)
