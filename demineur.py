# fonction génératrice de grille à partir d'une taille de côté M - ou 2 tailles (M,N)
#  cases K  : cases pleines, ou noires, ou True, ou X ; répartie aléatoirement
#  cases vides, ou blanches, ou False,
#  Générer cette grille en ligne de commande en python.
import random

def main():
        revealGrid(3, 5, "#", "0", "K")
        print()
    

def createEmptyGrid(widthSide, lengthSide, hiddenSquare):
    newList = []
    for length in range(lengthSide):
        for width in range(widthSide):
            newList.append(hiddenSquare)
        print(newList, end="")
        newList = []
        print()    
    repetition = int(widthSide) * int(lengthSide)
    return repetition


def revealGrid(widthSide, lengthSide, hiddenSquare, emptySquare, fullSquare):
    repetition = createEmptyGrid(widthSide, lengthSide, hiddenSquare)
    randomList = [emptySquare, fullSquare, emptySquare]
    gridList = []
    newList = []


    for i in range(repetition): 
        squareClicked = input("Enter the location of a square: ")
        squareLocationOrd, squareLocationAbs = squareClicked.split(':')
        ord = int(squareLocationOrd)
        abs = int(squareLocationAbs)

        for length in range(0, lengthSide):
            for width in range(0, widthSide):
                newList.append(hiddenSquare)
                if width + 1 == abs and length + 1 == ord:
                    newList.insert(abs, random.choice(randomList))
                    newList.pop(width)
            print(newList, end="")
            gridList.append(newList)
            # insérer dans gridList le nouvel élément de la list en cours
            newList = []
            print()
        print("gridList: ", gridList) 

main()
