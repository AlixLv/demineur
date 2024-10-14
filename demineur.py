# fonction génératrice de grille à partir d'une taille de côté M - ou 2 tailles (M,N)
#  cases K  : cases pleines, ou noires, ou True, ou X ; cases réparties aléatoirement
#  cases vides, ou blanches, ou False 
#  Générer cette grille en ligne de commande en python.

def main():
    createGrid(10, 5, "#", "K")


def createGrid(lengthSide, widthSide, emptySquare, fullSquare):
    emptySquare = "#"
    fullSquare = "K"
    for width in range(widthSide):
        print(emptySquare * (lengthSide - 1))
        

main()