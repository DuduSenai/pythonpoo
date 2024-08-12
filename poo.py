class Caneca:
    formato = "cilíndrico"

    def __init__(self, nome, marca, capacidade):
        self.nome = nome
        self.marca = marca
        self.capacide = capacidade

canecal = Caneca("Top caneca", "Stanley", "700 ml")
print(canecal.capacide)
caneca2 = Caneca("Canequinha", "Pacco", "500 ml")
print(caneca2.nome)