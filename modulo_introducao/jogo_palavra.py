import os

palavra = 'amor'
letra_acertada = ''
tentativas = 0

while True:
    letra_adivinhada = input('Digite uma letra: ').lower()
    if letra_adivinhada.isdigit() or len(letra_adivinhada) < 1:
        print('Você não digitou uma letra.')
        continue
    elif len(letra_adivinhada) > 1:
        print('Digite apenas uma letra.')
        continue
    
    if letra_adivinhada in palavra:
        letra_acertada += letra_adivinhada

    palavra_formada = ''
    for i in palavra:
        if i in letra_acertada:
            palavra_formada += i
        else:
            palavra_formada += '*'
    
    print(palavra_formada)
    tentativas += 1
    
    if palavra_formada == palavra:
        break

os.system('cls')
print('Parabéns!!! Você acertou!!!')
print(f'A palavra era {palavra.capitalize()}!')
print(f'Você acertou em {tentativas} tentativas.')