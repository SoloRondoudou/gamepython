from player import player
from arme import arme

print("Bonjour a tous jouez a 2 a un jeu de combat")
print()
nameplayer1 = input("Quel est le nom du jouer 1 : ")
nameplayer2 = input("Quel est le nom du jouer 2 : ")

player1 = player(nameplayer1, 100)
player2 = player(nameplayer2, 100)

armegrenade = arme("grenade", 30, 2)
armemitrail = arme("mitraillette", 24, 3)
armepistolet = arme("pistolet", 15, 5)

commence = player1.get_nom()


while player1.get_vie() > 0 and player2.get_vie() > 0:
    if armegrenade.get_utilisation() == 0:
        print("vous ne pouvez plus utilisé de", armegrenade.get_nom())

    if armemitrail.get_utilisation() == 0:
        print("vous ne pouvez plus utilisé de", armemitrail.get_nom())

    if armepistolet.get_utilisation() == 0:
        print("vous ne pouvez plus utilisé de", armepistolet.get_nom())
    #               joueur 1
    print(player1.get_nom(), "c'est a vous")
    print()

    print(commence, "vous devez choisir une arme")
    print("1 =", armegrenade.get_nom(), "qui inflige", armegrenade.get_degats(), "dégat et a encore",
          armegrenade.get_utilisation(), "possibilite d'utilisation")
    print("2 =", armemitrail.get_nom(), "qui inflige", armemitrail.get_degats(), "dégat et a encore",
          armemitrail.get_utilisation(), "possibilite d'utilisation")
    print("3 =", armepistolet.get_nom(), "qui inflige", armepistolet.get_degats(), "dégat et a encore",
          armepistolet.get_utilisation(), "possibilite d'utilisation")

    choicearme = int(input("votre attaque : "))

    if choicearme == 1:
        armegrenade.utilise(1)
        player2.degats(armegrenade.get_degats())
        print(player2.get_nom(), "vous avez perdue", armegrenade.get_degats(), "% de vie")
        print("Il vous reste que", player2.get_vie(), "% de vie")

    elif choicearme == 2:
        armemitrail.utilise(1)
        player2.degats(armemitrail.get_degats())
        print(player2.get_nom(), "vous avez perdue", armemitrail.get_degats(), "% de vie")
        print("Il vous reste que", player2.get_vie(), "% de vie")

    elif choicearme == 3:
        armepistolet.utilise(1)
        player2.degats(armepistolet.get_degats())
        print(player2.get_nom(), "vous avez perdue", armepistolet.get_degats(), "% de vie")
        print("Il vous reste que", player2.get_vie(), "% de vie")

    print()
    print()

    if armegrenade.get_utilisation() == 0:
        print("vous ne pouvez plus utilisé de", armegrenade.get_nom())

    if armemitrail.get_utilisation() == 0:
        print("vous ne pouvez plus utilisé de", armemitrail.get_nom())

    if armepistolet.get_utilisation() == 0:
        print("vous ne pouvez plus utilisé de", armepistolet.get_nom())

    #               joueur 2
    print(player2.get_nom(), "c'est a vous")
    print("1 =", armegrenade.get_nom(), "qui inflige", armegrenade.get_degats(), "dégat et a encore", armegrenade.get_utilisation(), "possibilite d'utilisation")
    print("2 =", armemitrail.get_nom(), "qui inflige", armemitrail.get_degats(), "dégat et a encore", armemitrail.get_utilisation(), "possibilite d'utilisation")
    print("3 =", armepistolet.get_nom(), "qui inflige", armepistolet.get_degats(), "dégat et a encore", armepistolet.get_utilisation(), "possibilite d'utilisation")
    choicearme = int(input("votre attaque : "))

    if choicearme == 1:
        armegrenade.utilise(1)
        player1.degats(armegrenade.get_degats())
        print(player1.get_nom(), "vous avez perdue", armegrenade.get_degats(), "% de vie")
        print("Il vous reste que", player1.get_vie(), "% de vie")

    elif choicearme == 2:
        armemitrail.utilise(1)
        player1.degats(armemitrail.get_degats())
        print(player1.get_nom(), "vous avez perdue", armemitrail.get_degats(), "% de vie")
        print("Il vous reste que", player1.get_vie(), "% de vie")

    elif choicearme == 3:
        armepistolet.utilise(1)
        player1.degats(armepistolet.get_degats())
        print(player1.get_nom(), "vous avez perdue", armepistolet.get_degats(), "% de vie")
        print("Il vous reste que", player1.get_vie(), "% de vie")

    print()
    print()

    if armegrenade.get_utilisation() == 0:
        print("vous ne pouvez plus utilisé de", armegrenade.get_nom())

    if armemitrail.get_utilisation() == 0:
        print("vous ne pouvez plus utilisé de", armemitrail.get_nom())

    if armepistolet.get_utilisation() == 0:
        print("vous ne pouvez plus utilisé de", armepistolet.get_nom())
