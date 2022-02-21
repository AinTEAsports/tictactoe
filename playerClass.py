class Player:

    def __init__(self, sign : str):
        """Init for the 'Player' class

        Args:
            sign (str): the symbol that will be used to replace boxes in the grill
        """
        self.sign = sign
        self.plays = []
    
    
    def isWinner(self):
        """Method that returns if the player has a winning combination

        Returns:
            bool: returns if the player has a winning combination
        """
        if '1' in self.plays and '2' in self.plays and '3' in self.plays:
            return True
        elif '4' in self.plays and '5' in self.plays and '6' in self.plays:
            return True
        elif '7' in self.plays and '8' in self.plays and '9' in self.plays:
            return True
        elif '1' in self.plays and '4' in self.plays and '7' in self.plays:
            return True
        elif '2' in self.plays and '5' in self.plays and '8' in self.plays:
            return True
        elif '3' in self.plays and '6' in self.plays and '9' in self.plays:
            return True
        elif '1' in self.plays and '5' in self.plays and '9' in self.plays:
            return True
        elif '3' in self.plays and '5' in self.plays and '7' in self.plays:
            return True
        else:
            return False


    def getSign(self):
        """Method to get the player sign

        Returns:
            str (in facts it's char but ther's no char 'type' in python): returns the player's sign
                (the sign that will replace the grill's boxes)
        """
        return self.sign


# Didn't know what to put in here so I just put a joke, hope you laugh
if __name__ == '__main__':
    print("First person  : Knock knock...")
    print("Second person : Who's there ?")
    print("First person  : Atch...")
    print("Second person : Atch who ?")
    print("First person  : Bless you")
    print("Both person   : *laughing*")
