#Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

# Словарь соотношения десятичной системы и шестнадцатиричнойсистем исчисления
conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c',
                    13: 'd', 14: 'e', 15: 'f'}
 
decimal_number = 10 # Цифра в десятичной системе
print(hex(decimal_number)) # Проверка результата встроенной функцтей

hexadecimal = ''
while(decimal_number > 0):
    remainder = decimal_number % 16
    hexadecimal = conversion_table[remainder] + hexadecimal
    decimal_number = decimal_number // 16

print('')
print('0x%s' %hexadecimal) #Вывод результата

