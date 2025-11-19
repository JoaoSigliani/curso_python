from contas import Conta

class Pessoa:
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade
        
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def idade(self) -> int:
        return self._idade
    
    def __repr__(self):
        return f'Pessoa(nome={self._nome}, idade={self._idade})'
        
class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, conta: Conta | None = None):
        super().__init__(nome, idade)
        self.conta = conta
        
    def __repr__(self):
        return super().__repr__()[:-1] + f', conta={self.conta})'