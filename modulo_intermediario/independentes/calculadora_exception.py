operacoes_validas = ('+', '-', '*', '/')

while True:
    a = input("Digite o primeiro numero: ")
    b = input("Digite o segundo numero: ")
    try:
        a = int(a)
        b = int(b)
        break
    except ValueError:
        print("Entradas inválidas!")
        
while True:
    op = input("Digite a operação (+, -, *, /): ")
    
    try:
        if op not in operacoes_validas:
            raise ValueError
        break
    except ValueError:
        print("Operador inválido!")
        
if op == '+':
    print(f'Soma = {a + b}')
elif op == '-':
    print(f'Subtração = {a - b}')
elif op == '*':
    print(f'Multiplicação = {a * b}')
else:
    try:
        print(f'Divisão = {a / b}')
    except ZeroDivisionError:
        print("Divisão por zero!")