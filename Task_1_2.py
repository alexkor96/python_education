# 2. Пользователь вводит время в секундах. Переведите время в часы,
# минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

user_sec_input = int(input('Введите количество секунд: '))
hour = user_sec_input//(60*60)
minute = (user_sec_input - hour*(60*60))//60
second = user_sec_input - hour*(60*60) - minute*60
print(f" {hour}:{minute}:{second}")