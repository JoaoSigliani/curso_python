perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0

for pergunta in perguntas:
    print(pergunta.get('Pergunta'))
    
    opcoes = pergunta.get('Opções')
    
    for i, o in enumerate(opcoes):
        print(f'{i}) {o}')
    
    resposta_certa = pergunta.get('Resposta')
    resposta_usuario = int(input('Resposta:'))
    
    if opcoes[resposta_usuario] == resposta_certa:
        print('Acertou!')
        acertos+=1
    else:
        print('Errou!')
        
print(f'Você acertou {acertos} de {len(perguntas)} perguntas!')