# 第七章 while循环

# # 选择退出，使用break，使用标志flag
prompt = '\nTell me something, and I will repeat it back to you: '
prompt += '\nEnter "quit" to end the programme.'
active = True
while active:
    message = input(prompt)

    if message =='quit':
        # active = False
        break
    else:
        print(message)

# # 在循环中使用continue
cur = 0
while cur < 10:
    cur += 1
    if cur % 2 == 0:
        continue

    print(cur)

# # 在列表之间移动元素
unfinished = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
finished = []
while unfinished:
    finishing = unfinished.pop()

    print(f'{finishing.title()} is finishing...')
    finished.append(finishing)

print('\nThe followings have been finished:')
for i in finished:
    print(i.title())
print()

# # 删除为特定值的所有列表元素
A = ['1', '1', '1', '2', '2', '3', '4']
print(A)
while '1' in A:
    A.remove('1')
print(A)
print()

# # 使用用户输入填充字典
responses = {}
polling_active = True
while polling_active:
    name = input('what is your name?')
    response = input('How old are you?')
    responses[name] = response
    repeat = input('Keep going on?(yes/no)')
    if repeat == 'no':
        break
        # polling_active = False
print('\n---Polling Results---')
for name, response in responses.items():
    print(f'{name} is {response} years old.')
print(responses)