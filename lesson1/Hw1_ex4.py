# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

var = int(input('Введите целое число: '))

maximum = var % 10
var = var // 10
while var > 0:
    if var % 10 > maximum:
        maximum = var % 10
    var = var // 10

print('Наибольшая цифра в числе -', maximum)
