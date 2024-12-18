# fonction génératrice de grille à partir d'une taille de côté M - ou 2 tailles (M,N)
#  cases K  : cases pleines, ou noires, ou True, ou X ; répartie aléatoirement
#  cases vides, ou blanches, ou False,
#  Générer cette grille en ligne de commande en python.
import random

def main():
        revealGrid(3, 5, "#", "⬜️", "💣")
        print()
    

def createEmptyGrid(widthSide, lengthSide, hiddenSquare):
    gridList = []
    newList = []
    for length in range(lengthSide):
        for width in range(widthSide):
            newList.append(hiddenSquare)
        print(newList, end="")
        gridList.append(newList)
        newList = []
        print()  
    
    return gridList


def countBombs(grid, square):
    counterOfBombs = 0

    for sublist in grid:
        for item in sublist:
            if item == square:
                counterOfBombs += 1
            else:
                counterOfBombs = counterOfBombs  
        print("nombre de bombes: ", counterOfBombs)  


def revealGrid(widthSide, lengthSide, hiddenSquare, emptySquare, fullSquare):
    gridList = createEmptyGrid(widthSide, lengthSide, hiddenSquare)
    randomList = [emptySquare, fullSquare, emptySquare]
    repetition = int(widthSide) * int(lengthSide)
    newList = []
    # print("grid list de départ: ", gridList)

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
                    gridList[ord - 1].insert(abs - 1, newList[abs - 1])
                    gridList[ord - 1].pop(width + 1)

            print(newList, end="")

            newList = []
            print()
        print("gridList: ", gridList)
    
        countBombs(gridList, fullSquare) 

main()