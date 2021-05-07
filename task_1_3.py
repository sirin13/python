number = int(input('Введите число в промежутке от 0 до 20: '))

if 5 <= number <= 20 or number == 0:
    print(number, 'процентов')
elif 2 <= number <= 4:
    print(number, 'процента')
elif number == 1:
    print(number, 'процент')
else: print('Введенное число не входит в заданный промежуток')

print('Проверка:')
i = 0
while i < 21:
    if 5 <= i <= 20 or i == 0:
        print(i, 'процентов')
    elif 2 <= i <= 4:
        print(i, 'процента')
    elif i == 1:
        print(i, 'процент')
    i += 1