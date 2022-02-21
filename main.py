from playerClass import Player


# Function to print grill
def printGrille(grilleDict : dict):
    print(f"{grilleDict[1]} | {grilleDict[2]} | {grilleDict[3]}")
    print(f"{grilleDict[4]} | {grilleDict[5]} | {grilleDict[6]}")
    print(f"{grilleDict[7]} | {grilleDict[8]} | {grilleDict[9]}")


# Function to know if grill is full
def isGrilleFull(grilleDict : dict):
    for key in grilleDict.keys():
        if grilleDict[key] == str(key):
            return False
    
    return True


# Function to know if a box is occupied or no
def isOccupied(grilleDict : dict, case):
    return grilleDict[int(case)] != str(case)



# Creating grill
grille = {
    1 : "1",
    2 : "2",
    3 : "3",
    4 : "4",
    5 : "5",
    6 : "6",
    7 : "7",
    8 : "8",
    9 : "9"
}


# Defining two players
player1 = Player("X")
player2 = Player("O")




# While none of players has winning combination we continue the game
while not player1.isWinner() or player2.isWinner():
    # Printing grill and players signs
    print("\n" * 30)
    print(f"Player 1 : {player1.getSign()}")
    print(f"Player 2 : {player2.getSign()}\n\n")
    printGrille(grille)
    
    
    
    
    # Player 1 turn

    # Asking him to enter the box number in which box he wants to put his sign
    player1play = input("\nPlayer 1 enter a number : ")
    
    # Verification if what he entered is valid
    while player1play not in [str(i) for i in range(1, 10)] or isOccupied(grille, player1play):
        print("\n# Entrez un nombre valide #\n")
        player1play = input("\nPlayer 1 enter a number : ")


    # Adding what he choose to his plays list
    player1.plays.append(player1play)
    
    # Putting his sign into the box
    grille[int(player1play)] = player1.getSign()
    
    # If he has a winning combination, we stop the game
    if player1.isWinner():
        print("\n/// PLAYER 1 WINS ! ///\n")
        printGrille(grille)
        break
    
    
    # If grill is full we stop the game
    if isGrilleFull(grille):
        print("\n/// TIE ! ///\n")
        break



    # Player 2 turn
    
    # On affiche la grille et les infos des joueurs
    print("\n" * 30)
    print(f"Player 1 : {player1.getSign()}")
    print(f"Player 2 : {player2.getSign()}\n\n")
    printGrille(grille)
    
    
    
    
    # Asking him to enter the box number in which box he wants to put his sign
    player2play = input("\nPlayer 2 enter a number : ")
    
    # Verification if what he entered is valid
    while player2play not in [str(i) for i in range(1, 10)] or isOccupied(grille, player2play):
        print("\n# Entrez un nombre valide #\n")
        player2play = input("\nPlayer 2 enter a number : ")
        
    
    # Adding what he choose to his plays list
    player2.plays.append(player2play)
    
    # Putting his sign into the box
    grille[int(player2play)] = player2.getSign()
    
    # If he has a winning combination, we stop the game
    if player2.isWinner():
        print("\n/// PLAYER 2 WINS ! ///\n")
        printGrille(grille)
        break


    # If grill is full we stop the game
    if isGrilleFull(grille):
        print("\n/// TIE ! ///\n")
        break


print("\n\n/// END OF THE GAME ///\n")
