from salva import Pessoa
import json

with open("banco.json", "r+", encoding='utf8') as file:
    banco = json.load(file)
    
p1 = Pessoa(**banco[0])
# p2 = Pessoa(**banco[1])

print(p1.nome)
# print(p2.nome)