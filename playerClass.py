# Creating Player class
class Player:

    # We need the player sign
    def __init__(self, sign : str):
        self.sign = sign
        self.plays = []
    
    
    # Method to know if the player has a winning combination
    def isWinner(self):
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


    # Method to get the player's sign
    def getSign(self):
        return self.sign


# Didn't know what to put in here so I just put a joke, hope you laugh
if __name__ == '__name__':
    print("First person : Knock knock...")
    print("Second person : Who's there ?")
    print("First person : Atch...")
    print("Second person : Atch who ?")
    print("First person : Bless you")
    print("Both person : *laughing*")
