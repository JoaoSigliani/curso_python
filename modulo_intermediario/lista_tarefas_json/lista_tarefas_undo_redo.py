from os import system
import json

loop = True
arquivo = "lista.json"
lista = []
buffer = []

# CARREGA O ARQUIVO JSON SE EXISTIR
try:
    with open(arquivo, 'r+', encoding="utf8") as file:
        lista = json.load(file)
except FileNotFoundError:
    print('Arquivo não carregado!')
    
# DEFINIÇÃO DOS COMANDOS 
def print_list(lista):
    print('TAREFAS:')
    for i in lista:
        print(i)
    print()
    
def undo(lista, buffer):
    try:
        buffer.append(lista.pop())
        print_list(lista)
    except IndexError:
        print("Nada a desfazer!")
        
def redo(lista, buffer):
    try:
        lista.append(buffer.pop())
        print_list(lista)
    except IndexError:
        print("Nada a refazer!")
        
def add(tarefa, lista):
    lista.append(tarefa)
    
def exit():
    global loop
    loop = False

#REALIZA OS COMANDOS DIGITADOS PELO USUÁRIO
while loop:
    print("Comandos: list, undo, redo, clear, exit")
    tarefa = input("Digite uma tarefa ou um comando:\n")
    print()
    
    comandos = {
        'list': lambda: print_list(lista),
        'undo': lambda: undo(lista, buffer),
        'redo': lambda: redo(lista, buffer),
        'add': lambda: add(tarefa, lista),
        'clear': lambda: system('cls'),
        'exit': lambda: exit()
    }
    
    comandos['add']() if tarefa not in comandos else comandos[tarefa]()

#ESCREVE A LISTA NO JSON
with open(arquivo, 'w+', encoding='utf8') as file:
    json.dump(lista, file, indent=2)


# FORMA SEM DICIONÁRIO DE RECEBER OS COMANDOS DO USUÁRIO
# while True:
#     print("Comandos: list, undo, redo")
#     op = input("Digite uma tarefa ou um comando:\n")
#     print()
    
#     match op.lower():
#         case 'list':
#             imprimir_lista(lista)
#         case 'undo':
#             try:
#                 buffer.append(lista.pop())
#                 imprimir_lista(lista)
#             except IndexError:
#                 print("Nada a desfazer!")
#         case 'redo':
#             try:
#                 lista.append(buffer.pop())
#                 imprimir_lista(lista)
#             except IndexError:
#                 print("Nada a refazer!")
#         case _:
#             lista.append(op)