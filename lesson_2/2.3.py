"""Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict."""

# метод решения list
val = int(input('Введите месяц в виде целого числа от 1 до 12: '))
calendar = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
print(str(val), 'месяц - это', calendar[val - 1])

# метод решения dict
val = int(input('Введите месяц в виде целого числа от 1 до 12: '))
calendar_dict = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень',
                 10: 'осень', 11: 'осень', 12: 'зима'}
print(str(val), 'месяц -  это', calendar_dict.get(val))
