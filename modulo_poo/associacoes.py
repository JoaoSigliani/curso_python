class Carro:
    def __init__(self, nome,):
        self.nome = nome
        self._motor = None
        self._fabricante = None
        
    @property
    def motor(self):
        return self._motor
    @motor.setter
    def motor(self, nome):
        self._motor = nome
        
    @property
    def fabricante(self):
        return self._fabricante
    @fabricante.setter
    def fabricante(self, nome):
        self._fabricante = nome
        
    def imprimir_carro(self):
        print(f'{self.fabricante.nome} {self.nome} {self.motor.nome}')
    
class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        
class Motor:
    def __init__(self, nome):
        self.nome = nome
      
      
hyundai = Fabricante("Hyundai")
volkswagen = Fabricante("Volkswagen")
turbo = Motor("1.0 Turbo")
motor_1_6 = Motor("1.6")

creta = Carro("Creta")
tcross = Carro("T-Cross")
gol = Carro("Gol")

creta.fabricante = hyundai
creta.motor = turbo

tcross.fabricante = volkswagen
tcross.motor = turbo

gol.fabricante = volkswagen
gol.motor = motor_1_6

creta.imprimir_carro()
tcross.imprimir_carro()
gol.imprimir_carro()


        