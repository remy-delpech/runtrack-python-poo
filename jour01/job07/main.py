class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
    
    def get_titre(self):
        return self.__titre
    
    def set_titre(self, titre):
        self.__titre = titre
    
    def get_auteur(self):
        return self.__auteur
    
    def set_auteur(self, auteur):
        self.__auteur = auteur
    
    def get_nb_pages(self):
        return self.__nb_pages
    
    def set_nb_pages(self, nb_pages):
        if isinstance(nb_pages, int) and nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            print("Erreur : le nombre de pages doit être un entier positif.")

livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 100)
print("Titre :", livre.get_titre()) # Affiche : Titre : Le Petit Prince
print("Auteur :", livre.get_auteur()) # Affiche : Auteur : Antoine de Saint-Exupéry
print("Nombre de pages :", livre.get_nb_pages()) # Affiche : Nombre de pages : 100

livre.set_titre("Harry Potter à l'école des sorciers")
livre.set_auteur("J.K. Rowling")
livre.set_nb_pages(300)
print("Nouveau titre :", livre.get_titre()) # Affiche : Nouveau titre : Harry Potter à l'école des sorciers
print("Nouvel auteur :", livre.get_auteur()) # Affiche : Nouvel auteur : J.K. Rowling
print("Nouveau nombre de pages :", livre.get_nb_pages()) # Affiche : Nouveau nombre de pages : 300

livre.set_nb_pages(-50) # Affiche : Erreur : le nombre de pages doit être un entier positif.
print("Nombre de pages après erreur :", livre.get_nb_pages()) # Affiche : Nombre de pages après erreur : 300