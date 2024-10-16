# fonction génératrice de grille à partir d'une taille de côté M - ou 2 tailles (M,N)
#  cases K  : cases pleines, ou noires, ou True, ou X ; répartie aléatoirement
#  cases vides, ou blanches, ou False,
#  Générer cette grille en ligne de commande en python.
import random

def main():
    repetition = createEmptyGrid(4, 6, "#")
    print()
    for i in range(repetition): 
        SquareClicked = input("Enter the location of a square: ")
        revealGrid(4, 6, "#", "0", "K", 6, SquareClicked)
    

def createEmptyGrid(widthSide, lengthSide, hiddenSquare):
    for length in range(lengthSide):
        for width in range(widthSide):
            newList = []
            newList.append(hiddenSquare)
            print(newList, end="")
        print()    
    repetition = int(widthSide) * int(lengthSide)
    return repetition

def revealGrid(widthSide, lengthSide, hiddenSquare, emptySquare, fullSquare, numberOfBombs, squareClicked):
    randomList = [emptySquare, fullSquare, emptySquare]
    squareLocationOrd, squareLocationAbs = squareClicked.split(':')
    ord = int(squareLocationOrd)
    abs = int(squareLocationAbs)

    for length in range(1, lengthSide):
        for width in range(1, widthSide):
            newList = []
            newList.append(hiddenSquare)
            if width == abs and length == ord:
                newList.insert(ord, random.choice(randomList))
            print(newList, end="")
        print()

main()
