import json

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open("pessoa.json", 'w+', encoding='utf8') as file:
    json.dump(pessoa, file, indent=2, ensure_ascii=False)
    
with open("pessoa.json", 'r', encoding="utf8") as file:
    pessoa_importada = json.load(file)
    for chave, valor in pessoa_importada.items():   
        print(f'{chave}: {valor}')
    