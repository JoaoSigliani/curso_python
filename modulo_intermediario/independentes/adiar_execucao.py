def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(func, x):
    def interna(y):
        return func(x, y)
    return interna

soma_cinco = criar_funcao(soma, 5)
multiplica_10 = criar_funcao(multiplica, 10)

print(soma_cinco(10))
print(multiplica_10(5))