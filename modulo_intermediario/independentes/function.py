def multiplica(*args):
    total = 1
    for i in args:
        total *= i
    return total

def parimpar(x):
    if x % 2 == 0:
        return 'Par'
    return 'Ímpar'

total = multiplica(1, 2, 3, 4, 5)
print(total)
print(parimpar(total))