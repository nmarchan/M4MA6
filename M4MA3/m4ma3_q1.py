from random import randint #needed for random function

class Die():
    '''Creates a die with a certain number of sides'''
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        '''Prints a random number between 1 and the number of sides'''
        print(randint(1, self.sides))

thisdice = Die() #creates a six sided die

for i in range(0, 10): #rolls the die 10 times
    thisdice.roll_die()

    
