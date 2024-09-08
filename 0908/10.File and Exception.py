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

