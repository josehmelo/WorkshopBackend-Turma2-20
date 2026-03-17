class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def get_nome(self):
        return self.nome

    def get_especie(self):
        return self.especie

    def emitirSom(self):
        return ""

    def apresentar(self):
        return f"Animal {self.especie}, chamado {self.nome}, som: {self.emitirSom()}"


class lobo(Animal):
    def __init__(self, nome):
        super().__init__(nome, "Lobo")

    def emitirSom(self):
        return "Auuuu"


class gato_do_mato(Animal):
    def __init__(self, nome):
        super().__init__(nome, "Gato do mato")

    def emitirSom(self):
        return "Miau"


class zoologico:
    def __init__(self, nome):
        self.nome = nome
        self.animais = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animais.append(animal)
            print(f"{animal.get_nome()} adotado pelo zoologico!")

    def listar_animais(self):
        if not self.animais:
            print("Nenhum animal no zoologico.")
        else:
            print(f"\n=== Zoologico {self.nome} ===")
            for animal in self.animais:
                print(f"  {animal.apresentar()}")


lobo1 = lobo("joaquim")
gato1 = gato_do_mato("gato de botas")

zo = zoologico("Bica")

zo.add_animal(lobo1)
zo.add_animal(gato1)

zo.listar_animais()