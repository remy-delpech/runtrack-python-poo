class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Instanciation de la classe
op = Operation(12, 3)

# Impression de l'objet en console
print("Le nombre1 est", op.nombre1)
print("Le nombre2 est", op.nombre2)