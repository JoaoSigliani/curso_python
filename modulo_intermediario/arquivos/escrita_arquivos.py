produtos = [
    {'nome': input("Digite o nome do produto: "), 'preço': float(input("Digite o preço do produto: "))}
    for i in range(3)
]

# produtos = [
#     {'nome': 'Maçã', 'preço': 5},
#     {'nome': 'Banana', 'preço': 3},
#     {'nome': 'Laranja', 'preço': 4}
# ]

print(produtos)

with open("Produtos.txt", 'w+', encoding="utf8") as file:
    for dic in produtos:
        for chave, valor in dic.items():
            if chave == 'nome':
                file.write(f'{chave}: ')
                file.write(f'{valor}, ')
            else:
                file.write(f'{chave}: ')
                file.write(f'{valor}\n')
            