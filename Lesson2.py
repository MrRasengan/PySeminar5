# Рекурсия
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1


def rekursia (num, i):
    if i == len(num):
        return num
    if num[i] == max(num):
        num[i] = min(num)
    rekursia(num, i + 1)




x = [1, 3, 4, 3, 4]
rekursia(x, 0)
print(x)

        