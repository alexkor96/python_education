# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким
# финансовым результатом работает фирма. Например, прибыль — выручка больше издержек,
# или убыток — издержки больше выручки. Выведите соответствующее сообщение.

revenue = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
if revenue > costs:
    print ('У компании есть прибыль')
elif revenue < costs:
    print('Компания работает в убыток')
else:
    print('Компания работает в ноль')
