from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

alunos_ordenados = sorted(alunos, key=lambda aluno: aluno['nota'])

alunos_agrupados = groupby(alunos_ordenados, key=lambda aluno : aluno['nota'])

for chave, grupo in alunos_agrupados:
    print(chave)
    for aluno in grupo:
        print(aluno)