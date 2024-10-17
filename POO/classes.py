class Animal:
    def __init__(self, nome, cor):
        self.nome=nome
        self.cor=cor

    def comer(self):
        print(f"{self.nome} foi comer.")

class Gato(Animal):
    def __init__(self, nome, cor, patas):
        super().__init__(nome, cor)
        self.patas=patas

    def miar(self):
        print(f"O {self.nome} foi miar")

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
        self.mugindo=False

    def muge(self):
        if self.mugindo==False:
            self.mugindo==True
            print("UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")