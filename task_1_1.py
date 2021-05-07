SEC_IN_1HOUR = 3600  # 60s * 60m
SEC_IN_1DAY = SEC_IN_1HOUR * 24
SEC_IN_1MONTH = SEC_IN_1DAY * 30 # cчитаем, что в месяце 30 дней
SEC_IN_1YEAR = SEC_IN_1MONTH * 12

duration = int(input('Введите продолжительность промежутка времени в секундах: '))

year = duration // SEC_IN_1YEAR # считаем количество полных лет
duration = duration - year * SEC_IN_1YEAR # отбрасываем количество лет
month = duration // SEC_IN_1MONTH # кол-во полных месяцев
duration = duration - month * SEC_IN_1MONTH # отбрасываем кол-во месяцев и так далее
day = duration // SEC_IN_1DAY
duration = duration - day * SEC_IN_1DAY
hour = duration // SEC_IN_1HOUR
duration = duration - hour * SEC_IN_1HOUR
minute = duration // 60
sec = duration % 60

if year > 0:
    print(year,"г",month, "мес",day,"дн",hour,"час",minute,"мин",sec,"сек")
elif month > 0:
    print(month, "мес",day,"дн",hour,"час",minute,"мин",sec,"сек")
elif day > 0:
    print(day,"дн",hour,"час",minute,"мин",sec,"сек")
elif hour > 0:
    print(hour,"час",minute,"мин",sec,"сек")
elif minute > 0:
    print(minute,"мин",sec,"сек")
else:  print(sec, "сек")

