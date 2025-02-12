mage = "Mage"
paladin = "Paladin"
assassin = "Assassin"
batonfeu = "Bâton de feu"
batonfoudre = "Bâton de foudre"
batoneau = "Bâton d'eau"
epeelongue = "Épée longue"
epeebouclier = "Épée courte et bouclier"
lance = "Lance"
dagues = "Dagues"
poison = "Poison"
couteaulance = "Couteaux de lancer"
facile = "Facile"
moyen = "Moyen"
difficile = "Difficile"
donjon = "Donjon"
foret = "Forêt"
labyrinthe = "Labyrinthe"
homme = "Homme"
femme = "Femme"

# Choix valides pour chaque catégorie
choix_valides_mage = ["Bâton de feu", "Bâton de foudre", "Bâton d'eau"]
choix_valides_paladin = ["Épée longue", "Épée courte et bouclier", "Lance"]
choix_valides_assassin = ["Dagues", "Poison", "Couteaux de lancer"]
choix_valides_difficulte = ["Facile", "Moyen", "Difficile"]

# Demande du personnage 
Personnage = input(f"Choisissez votre personnage : {mage}, {paladin}, {assassin}\n: ")
while Personnage not in [mage, paladin, assassin]:
    print("Choix invalide. Essayez à nouveau.")
    Personnage = input(f"Choisissez votre personnage : {mage}, {paladin}, {assassin}\n: ")
# Demande du sexe 
for _ in range(4):  # Limite de 4 tentatives pour ce choix
    Sexe = input(f"Choisissez le sexe de votre personnage : {homme} ou {femme}\n: ")
    if Sexe in [homme, femme]:
        break  # Si le choix est valide, on sort de la boucle
    else:
        print("Choix de sexe invalide. Essayez à nouveau.")
# Choix de l'arme
armes_disponibles = {
    mage: choix_valides_mage,
    paladin: choix_valides_paladin,
    assassin: choix_valides_assassin
}


for personnage, armes in armes_disponibles.items():
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
while Difficulté not in choix_valides_difficulte:
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
