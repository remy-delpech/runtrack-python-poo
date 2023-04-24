class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
    
    def vieillir(self):
        self.age += 1

    def nommer(self):
        self.prenom = "Luna"

animal = Animal()
print("L'age de l'animal", animal.age, "ans") # Affiche : L'age de l'animal 0 ans

animal.vieillir()
print("L'age de l'animal", animal.age, "ans") # Affiche : L'age de l'animal 1 ans

animal.nommer()
print("L'animal se nomme", animal.prenom)