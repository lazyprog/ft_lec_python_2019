print('What is your name?')
name = input()
print('Glad to see you,', name)
age = int(input('How old are you, ' + name + '?\n'))
x = age + 1
print('Seems that you are ', x)
if x >= 11 and x <= 19:
    print('let')    
elif x % 10 == 1:
    print('god')
elif x % 10 >= 2 and x % 10 <= 4:
    print('goda')
else:
    print('let')
print('!')
