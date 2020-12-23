num = input('Введите положительное число: ')
x = 0
for i in num:
    while int(i) > x:
        x = int(i)
print(x)
