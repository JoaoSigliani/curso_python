from pathlib import Path

class MyOpen:
    def __init__(self, caminho, modo):
        self.caminho = caminho
        self.modo = modo
        self._arquivo = None
    
    def __enter__(self):
        self._arquivo = open(self.caminho, self.modo, encoding="utf8")
        return self._arquivo
    
    def __exit__(self, *args):
        return self._arquivo.close()
    
CAMINHO = Path(__file__).parent / 'arquivo.txt'
    
with MyOpen(CAMINHO, 'w') as arquivo:
    arquivo.write("Linha 1 \n")
    arquivo.write("Linha 2 \n")
    arquivo.write("Linha 3 \n")