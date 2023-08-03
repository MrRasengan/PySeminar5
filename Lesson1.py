# Рекурсия
# Последовательностью Фибоначчи называется последовательность чисел 
# a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

def Fib_rec(N):
    if N == 0 or N == 1:
        return N
    return Fib_rec(N - 2) + Fib_rec(N - 1)

num = int(input("Введите число: "))
print(Fib_rec(num))