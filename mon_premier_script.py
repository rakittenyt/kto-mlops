import unittest
'''message = "C'est mon premier script !!!"
print(message)

je_change_de_type = 1
print(type(je_change_de_type))
je_change_de_type = "coucou"
print(type(je_change_de_type))

# Définition de la liste des prénoms
prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]

# Initialisation du compteur pour les prénoms ayant plus de 7 lettres
more_than_seven = 0

# Boucle pour parcourir chaque prénom dans la liste
for prenom in prenoms:
    # Vérification si le prénom a plus de 7 lettres
    if len(prenom) > 7:
        # Incrémentation du compteur si la condition est vraie
        more_than_seven += 1
        # Affichage du prénom avec un message approprié
        print(prenom + " est un prénom avec un nombre de lettres supérieur à 7")
    else:
        # Affichage du prénom si le nombre de lettres est inférieur ou égal à 7
        print(prenom + " est un prénom avec un nombre de lettres inférieur ou égal à 7")

# Affichage du nombre total de prénoms ayant plus de 7 lettres
print("Nombre de prénoms dont le nombre de lettres est supérieur à 7 : " + str(more_than_seven))

def saluer(nom: str) -> str:
    return "Bonjour " + nom

print(saluer("Alice"))  # Affiche : Bonjour Alice

"""
Count names with more than seven letters
"""
# Définition de la fonction `names` pour compter les prénoms avec plus de 7 lettres
def names(prenoms):
    # Initialisation du compteur pour les prénoms ayant plus de 7 lettres
    more_than_seven = 0
    
    # Boucle pour parcourir chaque prénom dans la liste fournie en argument
    for prenom in prenoms:
        # Vérification si le prénom a plus de 7 lettres
        if len(prenom) > 7:
            # Incrémentation du compteur si la condition est vraie
            more_than_seven += 1
            # Affichage du prénom avec un message approprié
            print(prenom + " est un prénom avec un nombre de lettres supérieur à 7")
        else:
            # Affichage du prénom si le nombre de lettres est inférieur ou égal à 7
            print(prenom + " est un prénom avec un nombre de lettres inférieur ou égal à 7")
    
    # Retourne le nombre total de prénoms avec plus de 7 lettres
    return more_than_seven

# Définition de la liste des prénoms à analyser
prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]

# Appel de la fonction `names` avec la liste des prénoms et affichage du résultat
print("Nombre de prénoms dont le nombre de lettres est supérieur à 7 : " + str(names(prenoms=prenoms)))'''

def count_long_names(prenoms, length_threshold=7):
    """
    Count names with more than the specified number of letters.
    
    Parameters:
        prenoms (list): List of names to evaluate.
        length_threshold (int): Minimum number of letters to count a name as "long". Default is 7.
        
    Returns:
        int: Number of names with more than 'length_threshold' letters.
    """
    long_names_count = 0
    
    for prenom in prenoms:
        name_length = len(prenom)
        if name_length > length_threshold:
            long_names_count += 1
            print(f"{prenom} est un prénom avec un nombre de lettres supérieur à {length_threshold}")
        else:
            print(f"{prenom} est un prénom avec un nombre de lettres inférieur ou égal à {length_threshold}")
    
    return long_names_count


class TestNamesMethod(unittest.TestCase):
    def test_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seven = count_long_names(prenoms=prenoms)
        self.assertEqual(more_than_seven, 4)

if __name__ == '__main__':
    unittest.main()
