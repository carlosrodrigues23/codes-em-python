# programas-em-python

class Retangulo:
    def _init_(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
    
    def calcular_perimetro(self):
        return 2 * (self.comprimento + self.largura)
    
    def calcular_area(self):
        return self.comprimento * self.largura
        
comprimento = float(input("Digite o comprimento: "))
largura = float(input("Digite a largura: "))
retangulo = Retangulo(comprimento, largura)
perimetro = retangulo.calcular_perimetro()
area = retangulo.calcular_area()
print("O perímetro do retângulo é:", perimetro)
print("A área do retângulo é:", area)
