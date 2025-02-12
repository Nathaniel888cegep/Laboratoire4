mage = "Mage"  #Constante du personnage
paladin = "Paladin"  #Constante du personnage
assassin = "Assassin"  #Constante du personnage
batonfeu = "Bâton de feu"  #Constante de l'arme du personnage mage
batonfoudre = "Bâton de foudre" #Constante de l'arme du personnage mage
batoneau = "Bâton d'eau"  #Constante de l'arme du personnage mage
epeelongue = "Épée longue"  #Constante de l'arme du personnage paladin
epeebouclier = "Épée courte et bouclier"  #Constante de l'arme du personnage paladin
lance = "Lance"  #Constante de l'arme du personnage paladin
dagues = "Dagues"  #Constante de l'arme du personnage assassin
poison = "Poison"  #Constante de l'arme du personnage assassin
couteaulance = "Couteaux de lancer"  #Constante de l'arme du personnage assassin
facile = "Facile"  #Constante de la difficulté
moyen = "Moyen"  #Constante de la difficulté
difficile = "Difficile"  #Constante de la difficulté
donjon = "Donjon"  #Constante du niveau
foret = "Forêt"  #Constante du niveau
labyrinthe = "Labyrinthe"  #Constante du niveau
homme = "Homme"  #Constante du sexe
femme = "Femme"  #Constante du sexe

# Choix valides pour chaque catégorie
choix_valides_mage = ["Bâton de feu", "Bâton de foudre", "Bâton d'eau"]
choix_valides_paladin = ["Épée longue", "Épée courte et bouclier", "Lance"]
choix_valides_assassin = ["Dagues", "Poison", "Couteaux de lancer"]
choix_valides_difficulte = ["Facile", "Moyen", "Difficile"]

# Demande du personnage 
Personnage = input(f"Choisissez votre personnage : {mage}, {paladin}, {assassin}\n: ")
while Personnage not in [mage, paladin, assassin]:  # Boucle du choix du personnage qui retourne le joueur au choix si son choix n'est pas bon
    print("Choix invalide. Essayez à nouveau.")
    Personnage = input(f"Choisissez votre personnage : {mage}, {paladin}, {assassin}\n: ") # Le joueur choisi son personnage ici
# Demande du sexe 
for _ in range(4):  # Limite de 4 tentatives pour ce choix
    Sexe = input(f"Choisissez le sexe de votre personnage : {homme} ou {femme}\n: ")  # Le joueur choisi le sexe son personnage ici
    if Sexe in [homme, femme]:
        break  # Si le choix est valide, on sort de la boucle
    else:
        print("Choix de sexe invalide. Essayez à nouveau.")
# Choix de l'arme
armes_disponibles = {  # Défini quelles armes est à quelle personnage
    mage: choix_valides_mage,
    paladin: choix_valides_paladin,
    assassin: choix_valides_assassin
}


for personnage, armes in armes_disponibles.items():  # Boucle qui ramène le joueur si son choix d'arem n'est pas dans les choix
    if Personnage == personnage:
        print(f"Choisissez votre arme parmi : {', '.join(armes)}")
        weapon_choice = input(": ")
        while weapon_choice not in armes:
            print("Choix invalide. Essayez à nouveau.")
            weapon_choice = input(f"Choisissez votre arme parmi : {', '.join(armes)}\n: ")
        arme_choisi = weapon_choice
        break



# Choix de la difficulté 
Difficulté = input(f"Choisissez la difficulté que vous désirez : {facile}, {moyen}, {difficile}\n: ")
while Difficulté not in choix_valides_difficulte:  # Le joueur doit choisir une difficulté selon la sélection sinon il indicte invalide
    print("Choix de difficulté invalide. Essayez à nouveau.")
    Difficulté = input(f"Choisissez la difficulté que vous désirez : {facile}, {moyen}, {difficile}\n: ")

# Attribution du niveau en fonction de la difficulté choisi
if Difficulté == facile:
    niveau_requis = donjon
elif Difficulté == moyen:
    niveau_requis = foret
elif Difficulté == difficile:
    niveau_requis = labyrinthe

# Affichage du récapitulatif du personnage
print("\nRÉCAPITULATIF DU PERSONNAGE :")
print(f"Personnage choisi : {Personnage}")
print(f"Sexe choisi : {Sexe}")
print(f"Arme choisie : {arme_choisi}")
print(f"Difficulté choisie : {Difficulté} - Niveau : {niveau_requis}")
