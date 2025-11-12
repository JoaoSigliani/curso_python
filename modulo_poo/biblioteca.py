class Livro:
    disponivel = True
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
class Biblioteca:
    acervo = []
    
    def adicionar_livro(self, livro):
        self.acervo.append(livro)
    
    def emprestar(self, livro):
        for i in self.acervo:
            if i == livro:
                i.disponivel = False
    
    def devolver(self, livro):
        for i in self.acervo:
            if i == livro:
                i.disponivel = True
                
    def listar_disp(self):
        titulos = [
            (livro.titulo, livro.autor)
            for livro in self.acervo
            if livro.disponivel == True
        ]       
        return titulos
    
l1 = Livro("Senhor dos anéis", "Tolkien")
l2 = Livro("O Hobbit", "Tolkien")
l3 = Livro("A Metamorfose", "Kafka")

b1 = Biblioteca()

b1.adicionar_livro(l1)
b1.adicionar_livro(l2)
b1.adicionar_livro(l3)

print(b1.listar_disp())
b1.emprestar(l1)
print(b1.listar_disp())
b1.devolver(l1)
print(b1.listar_disp())

    