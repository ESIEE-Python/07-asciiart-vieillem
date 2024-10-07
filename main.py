"Aucun module à importer"
#### Imports et définition des variables globales


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de 
    caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # Liste qui va contenir le résultat final (les tuples)
    coded_list = []

    # Initialisation des variables de base
    if len(s) == 0:
        return coded_list

    current_char = s[0]  # Premier caractère de la chaîne
    count = 1  # Compteur pour les répétitions

    # Boucle à travers les caractères de la chaîne, en commençant au deuxième caractère
    for i in range(1, len(s)):
        if s[i] == current_char:
            # Si le caractère est le même que le précédent, on incrémente le compteur
            count += 1
        else:
            # Sinon, on ajoute le tuple (caractère, nombre de répétitions) à la liste
            coded_list.append((current_char, count))
            # On réinitialise pour le nouveau caractère
            current_char = s[i]
            count = 1

    # On ajoute le dernier groupe à la liste
    coded_list.append((current_char, count))

    return coded_list


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères
    passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # Cas de base : chaîne vide, on retourne une liste vide
    if len(s) == 0:
        return []

    # Initialisation pour trouver le premier groupe de caractères identiques
    first_char = s[0]
    count = 1

    # Parcourir la chaîne jusqu'à ce que le caractère change
    while count < len(s) and s[count] == first_char:
        count += 1

    # Appel récursif sur la sous-chaîne restante (à partir du premier caractère différent)
    return [(first_char, count)] + artcode_r(s[count:])


#### Fonction principale


def main():
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
