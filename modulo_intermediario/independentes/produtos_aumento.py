import copy
from pprint import pprint

def imprimir_dicts(lista):
    for dict in lista:
        for chave, valor in dict.items():
            print(f'[{chave}: {valor}]')

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [
    {**dicionario, 'preco': round(dicionario['preco'] * 1.1, 2)}
    for dicionario in copy.deepcopy(produtos)
]

produtos_ordenados_por_nome = sorted(copy.deepcopy(novos_produtos), key=lambda item: item['nome'], reverse=True)

produtos_ordenados_por_preco = sorted(copy.deepcopy(novos_produtos), key=lambda item: item['preco'])

print("Lista inicial: ")
pprint(produtos)
print("Lista modificada: ")
pprint(novos_produtos)
print("Lista ordenada por nome decrescente: ")
pprint(produtos_ordenados_por_nome)
print("Lista ordenada por preço crescente: ")
pprint(produtos_ordenados_por_preco)
