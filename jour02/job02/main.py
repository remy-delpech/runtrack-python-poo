class Personne:
    def __init__(self, age=14): # Initialisation de la classe avec l'âge par défaut à 14
        self.age = age # Attribut "age"

    def afficherAge(self): # Méthode pour afficher l'âge
        print(f"J'ai {self.age} ans.")

    def bonjour(self): # Méthode pour afficher "Hello"
        print("Hello")

    def modifierAge(self, age): # Méthode pour modifier l'âge
        self.age = age


class Eleve(Personne): # La classe Eleve hérite de la classe Personne
    def allerEnCours(self): # Méthode pour afficher "Je vais en cours"
        print("Je vais en cours")

    def affichageAge(self): # Méthode pour afficher l'âge de l'élève
        print(f"J'ai {self.age} ans.")


class Professeur(Personne): # La classe Professeur hérite de la classe Personne
    def __init__(self, matiereEnseignee): # Initialisation de la classe avec l'attribut "matiereEnseignee"
        super().__init__() # Appel du constructeur de la classe parente
        self.__matiereEnseignee = matiereEnseignee # Attribut "matiereEnseignee"

    def enseigner(self): # Méthode pour afficher "Le cours va commencer"
        print("Le cours va commencer")


# Instanciation d'un objet de la classe Personne avec l'âge par défaut
personne1 = Personne()

# Instanciation d'un objet de la classe Eleve avec l'âge modifier a 15 ans
eleve1 = Eleve(age=15)

# Instanciation d'un objet de la classe Professeur avec la matière enseignée "Physique" et l'âge de 40 ans
prof1 = Professeur(matiereEnseignee="Physique")
prof1.modifierAge(age=40)

# Appel de la méthode bonjour pour faire dire "Bonjour" à l'élève
eleve1.bonjour() # Résultat : Hello
# Affichage de l'âge de l'élève en utilisant la méthode "affichageAge"
eleve1.affichageAge() # Résultat : J'ai 15 ans.
# Appel de la méthode allerEnCours pour afficher "Je vais en cours"
eleve1.allerEnCours() # Résultat : Je vais en cours

# Appel de la méthode bonjour pour faire dire "Bonjour" au professeur
prof1.bonjour() # Résultat : Hello
# Appel de la méthode enseigner pour commencer le cours
prof1.enseigner() # Résultat : Le cours va commencer