# Поработайте с переменными, создайте несколько, выведите на экран, запросите у
# пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
num_1 = 3
num_2 = 7
str_1 = 'hello'
str_2 = 'world'
print(f'Имеются числа: {num_1} и {num_2}')
print(f'{num_1} + {num_2} =', num_1 + num_2)
print(f'{num_1} - {num_2} =', num_1 - num_2)
print(f'{num_1} * {num_2} =', num_1 * num_2)
print(f'{num_1} / {num_2} =', f'{num_1 / num_2:.4f}')
print(f'Имеются строки "{str_1}" и "{str_2}"')
print(str_1 + str_2)

print('Попробуйте ввести свои данные')
var_1 = input('Введите своё имя: ')
var_2 = input('Введите ваш возраст: ')
print(f'Вас зовут {var_1}, ваш возраст {var_2}')
