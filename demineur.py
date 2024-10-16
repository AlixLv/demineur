# fonction génératrice de grille à partir d'une taille de côté M - ou 2 tailles (M,N)
#  cases K  : cases pleines, ou noires, ou True, ou X ; répartie aléatoirement
#  cases vides, ou blanches, ou False,
#  Générer cette grille en ligne de commande en python.
import random

def main():
    createEmptyGrid(4, 6, "#")
    print()
    # createFulledGrid(4, 6, "0", "K", 4)
    SquareClicked = input("Enter the location of a square: ")
    revealGrid(6, 6, "#", "0", "K", 6, SquareClicked)
    

def createEmptyGrid(lengthSide, widthSide, hiddenSquare):
    for width in range(widthSide):
        for length in range(lengthSide):
            newList = []
            newList.append(hiddenSquare)
            print(newList, end="")
        print()    


def createFulledGrid(lengthSide, widthSide, emptySquare, fullSquare, numberOfBombs):
    randomList = [emptySquare, fullSquare, emptySquare]

    for width in range(widthSide):
        for length in range(lengthSide):
            newList = []
            if numberOfBombs == 0:
                newList.append(emptySquare)   
            else:    
                newList.append(random.choice(randomList))
            for value in newList:
                if value == randomList[1]:
                    numberOfBombs -= 1
 
            print(newList, end="")
            
        print()


def revealGrid(lengthSide, widthSide, hiddenSquare, emptySquare, fullSquare, numberOfBombs, squareClicked):
    randomList = [emptySquare, fullSquare, emptySquare]
    for width in range(widthSide):
        for length in range(lengthSide):
            newList = []
            newList.append(hiddenSquare)
            print(newList, end="")
        newIndex = int(squareClicked)
        newList.insert(newIndex, random.choice(randomList))
        print(newList, end="")
        print() 


main()
