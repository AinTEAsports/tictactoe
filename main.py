from playerClass import Player


# ASCII art because we're h@ck€rZ
print("""
  _______         ______              ______         
 /_  __(_)____   /_  __/___ ______   /_  __/___  ___ 
  / / / / ___/    / / / __ `/ ___/    / / / __ \/ _ \\
 / / / / /__     / / / /_/ / /__     / / / /_/ /  __/
/_/ /_/\___/    /_/  \__,_/\___/    /_/  \____/\___/
""")


def displayGrill(grillDict : dict):
    """Function to print grill

    Args:
        grillDict (dict): The dictionnary we'll use for displaying grill
    """
    print(f"{grillDict[1]} | {grillDict[2]} | {grillDict[3]}")
    print(f"{grillDict[4]} | {grillDict[5]} | {grillDict[6]}")
    print(f"{grillDict[7]} | {grillDict[8]} | {grillDict[9]}")


def isGrillFull(grillDict : dict):
    """Function to know if grill is full

    Args:
        grillDict (dict): grill we'll return if it's full

    Returns:
        bool: returns if grill is full or no
    """
    for key in grillDict.keys():
        if grillDict[key] == str(key):
            return False
    
    return True


def isOccupied(grillDict : dict, case : int):
    """Function to know if a box is occupied or no

    Args:
        grillDict (dict): the grill in which there are the box that we'll verify it's ocuppied
        case (int): the index case we'll verify it's occupied or no

    Returns:
        bool: returns if a box is occupied or no
    """
    return grillDict[int(case)] != str(case)



# Creating grill
grill = {
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
    # Displaying grill and players signs
    print("\n" * 30)
    print(f"Player 1 : {player1.getSign()}")
    print(f"Player 2 : {player2.getSign()}\n\n")
    displayGrill(grill)
    
    
    
    
    # -----------------
    # | Player 1 turn |
    # -----------------

    # Asking him to enter the box number in which box he wants to put his sign
    player1play = input("\nPlayer 1 enter a number : ")
    
    # Verification if what he entered is valid
    while player1play not in [str(i) for i in range(1, 10)] or isOccupied(grill, player1play):
        print("\n# Enter a valid number ! #\n")
        player1play = input("\nPlayer 1 enter a number : ")


    # Adding what he choose to his plays list
    player1.plays.append(player1play)
    
    # Putting his sign into the box
    grill[int(player1play)] = player1.getSign()
    
    # If he has a winning combination, we stop the game
    if player1.isWinner():
        print("\n/// PLAYER 1 WINS ! ///\n")
        displayGrill(grill)
        break
    
    
    # If grill is full we stop the game
    if isGrillFull(grill):
        print("\n/// TIE ! ///\n")
        break



    # -----------------
    # | Player 2 turn |
    # -----------------
    
    # Displaying grill and players signs
    print("\n" * 30)
    print(f"Player 1 : {player1.getSign()}")
    print(f"Player 2 : {player2.getSign()}\n\n")
    displayGrill(grill)
    
    
    
    
    # Asking him to enter the box number in which box he wants to put his sign
    player2play = input("\nPlayer 2 enter a number : ")
    
    # Verification if what he entered is valid
    while player2play not in [str(i) for i in range(1, 10)] or isOccupied(grill, player2play):
        print("\n# Enter a valid number #\n")
        player2play = input("\nPlayer 2 enter a number : ")
        
    
    # Adding what he choose to his plays list
    player2.plays.append(player2play)
    
    # Putting his sign into the box
    grill[int(player2play)] = player2.getSign()
    
    # If he has a winning combination, we stop the game
    if player2.isWinner():
        print("\n/// PLAYER 2 WINS ! ///\n")
        displayGrill(grill)
        break


    # If grill is full we stop the game
    if isGrillFull(grill):
        print("\n/// TIE ! ///\n")
        break


print("\n/// END OF THE GAME ///\n")
