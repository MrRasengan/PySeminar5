# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

n = int(input("Введите число: "))
 
def simple(n, i = 2):
    if i < n:
        if n % i != 0:
            return simple(n, i + 1)
        return print(f'Число "{n}" не является простым')
    return print(f'Число "{n}" является простым')

simple(n)