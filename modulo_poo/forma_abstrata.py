from abc import ABC, abstractmethod
import math

class FormaGeometrica(ABC):
    @abstractmethod
    def area(self): ...
    
    @abstractmethod
    def perimetro(self):...
    
class Retangulo(FormaGeometrica):
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
        
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return (2 * self.base) + (2 * self.altura)
    
class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
        
    def area(self):
        return (math.pi * math.pow(self.raio, 2))
    
    def perimetro(self):
        return 2 * math.pi * self.raio
    
    
r1 = Retangulo(10, 5)
print(r1.area(), r1.perimetro())
c1 = Circulo(5)
print(c1.area(), c1.perimetro())
