# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте
# модуль fractions.

from fractions import Fraction

first_fraction = '4/273'  # Первая дробь
second_fraction = '2/23' # Вторая дробь

numerator_first, denominator_first = map(int, first_fraction.split('/'))   #Извлечение числителя и знаменателя из первой дроби 
numerator_second, denominator_second = map(int, second_fraction.split('/')) #Извлечение числителя и знаменателя из второй дроби

#Функция нахождения НОД
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

#Функция сокращения дроби
def simplifyFraction(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    numerator /= common_divisor
    denominator /= common_divisor
    return int(numerator), int(denominator)

numerator_first, denominator_first = simplifyFraction(numerator_first, denominator_first)
numerator_second_fraction, denominator_second_fraction = simplifyFraction(numerator_second, denominator_second)

# Функция суммы дробей
def sum_fraction(numerator_first, denominator_first, numerator_second, denominator_second):
      numerator_sum = numerator_first * denominator_second_fraction + numerator_second * denominator_first
      denominator_sum = denominator_first * denominator_second
      numerator_sum, denominator_sum =  simplifyFraction(numerator_sum, denominator_sum)
      return f'{int(numerator_sum)}/{int (denominator_sum)}'

# Функция произведения дробей
def product_fraction (numerator_first, denominator_first, numerator_second, denominator_second):
      numerator_product = numerator_first * numerator_second
      denominator_product = denominator_first * denominator_second
      numerator_product, denominator_product = simplifyFraction(numerator_product, denominator_product)
      return f'{int(numerator_product)}/{int (denominator_product)}'

print ('Мой метод сложения и произведения дробей')
print(f'{sum_fraction(numerator_first, denominator_first, numerator_second, denominator_second)}')
print(f'{product_fraction(numerator_first, denominator_first, numerator_second, denominator_second)} \n')

print ('Встроенный метод Fraction')
print(Fraction(numerator_first, denominator_first) + 
      Fraction(numerator_second, denominator_second))
print(Fraction(numerator_first, denominator_first) *
      Fraction(numerator_second, denominator_second))
