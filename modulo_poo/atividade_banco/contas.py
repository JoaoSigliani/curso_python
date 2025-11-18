from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, nro_agencia, nro_conta, saldo=0):
        self.nro_agencia = nro_agencia
        self.nro_conta = nro_conta
        self.saldo = saldo
    
    @abstractmethod    
    def sacar(self, valor): ...
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('Valor de depósito inválido.')
            
    def imprimirSaldo(self):
        print(f'Saldo de R${self.saldo:.2f}')        
            
class ContaCorrente(Conta):
    def __init__(self, nro_agencia, nro_conta, saldo=0, limite=0):
        super().__init__(nro_agencia, nro_conta, saldo)
        self.limite = limite
        
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo + self.limite:  # Limite adicional conta corrente
            self.saldo -= valor
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
        elif valor <= 0:
            print("Valor inválido")
        else:
            print('Tentativa de saque ultrapassou o limite da conta.')
            
class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('Saldo insuficiente ou valor inválido para saque.')
