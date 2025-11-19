from contas import Conta 
from pessoas import Cliente

class Banco:
    def __init__(self, clientes: list[Cliente]=[], contas: list[Conta]=[], agencias: list[int]=[]):
        self.clientes = clientes
        self.contas = contas
        self.agencias = agencias
        
    def _checar_agencia(self, nro_agencia: int) -> bool:
        return nro_agencia in self.agencias
    
    def _checar_cliente(self, cliente: Cliente) -> bool:
        return cliente in self.clientes
    
    def _checar_conta(self, conta: Conta) -> bool:
        return conta in self.contas
    
    def _checar_conta_cliente(self, cliente: Cliente, conta: Conta) -> bool:
        if not self._checar_cliente(cliente):
            return False
        if not self._checar_conta(conta):
            return False
        return conta in cliente.contas
    
    def autenticar(self, cliente: Cliente, conta: Conta) -> bool:
        return self._checar_agencia(conta.nro_agencia) and self._checar_conta_cliente(cliente, conta)