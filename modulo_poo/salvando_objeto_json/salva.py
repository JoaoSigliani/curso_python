import json

class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        
p1 = Pessoa("João", "Sigliani", 20)
p2 = Pessoa("Luísa", "Hammes", 19)
banco = [p1.__dict__, p2.__dict__]

if __name__ == "__main__":
    with open ("banco.json", "w+", encoding='utf8') as file:
        json.dump(banco, file, indent=2)