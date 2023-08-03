# Рекурсия, сумма чисел от 1 до N

def Summ_rec(N):
    if N == 0:
        return 0
    return N + Summ_rec(N-1)

print(Summ_rec(4))