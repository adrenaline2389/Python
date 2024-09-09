# 第十章 文件和异常

# # 读取文件的全部内容
from pathlib import Path

path1 = Path('Pi.txt')
pi = path1.read_text()
print(pi)

 # # 访问文件中的各行
lines = pi.splitlines()
for line in lines:
    print(line)

# # 使用文件的内容
pi_string = ''
for line in lines:
    pi_string += line

print(pi_string)
print(len(pi_string))

# # 写入文件
path2 = Path('Guitar.txt')

contents = '1.Gibson Les Paul Standard 50s Cherry Burst\n'
contents += '2.Fender American Standard 7400 Apple Red\n'
contents += '3.Fernandes MG-120X Graphic on Black\n'
contents += '4.Steinberg GM-4T\n'

path2.write_text(contents)

# # 异常
print("Give me two numbers, and I'll divide them.")
print('Enter "q" to quit.')

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number =='q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
        # pass 静默失败
    else:
        print(answer)

# # 存储数据
import json
nums = [2, 3, 5, 7, 11, 13, 17, 19, 23]

path3 = Path('nums.json')
data = json.dumps(nums)
path3.write_text(data)

# # 读取数据
history = path3.read_text()
numbers = json.loads(history)
print(numbers)

# # 保存和读取用户生成的数据
path4 = Path('username.json')
if path4.exists():
    memory = path4.read_text()
    username = json.loads(memory)
    print(f'Welcome back, {username}!')
else:
    username = input('What is your name?')
    memory = json.dumps(username)
    path4.write_text(memory)
    print(f"We'll remember you when you come back, {username}!")