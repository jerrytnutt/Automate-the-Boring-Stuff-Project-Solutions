import zombiedice,random
import zombieDiceBots

# Create four zombie bots and run them against the example bots to see how they compare
# All created zombie bots are imported from the zombieDiceBots.py file

# Prototype class for all zombie bot classes
class MyZombie:
    def __init__(self, name):
        
        self.name = name

    def turn(self, gameState):
        

        diceRollResults = zombiedice.roll() 
        # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}
        brains = 0
       
        while diceRollResults is not None:
            
            brains += diceRollResults['brains']
            

            if brains < 2:
                
                diceRollResults = zombiedice.roll() 
            else:
                break

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    MyZombie(name='My Zombie Bot'),  
    # Three premade example bots and four created bots will be used
    zombieDiceBots.randomChoice(name='Random Choice'), zombieDiceBots.twoShotguns(name='Two Shot'),
    zombieDiceBots.randomRolls(name='Number Rolls'), zombieDiceBots.comparisonZombie(name='Comparison Zombie')
)

if __name__ == "__main__":
  zombiedice.runTournament(zombies=zombies, numGames=1000)
