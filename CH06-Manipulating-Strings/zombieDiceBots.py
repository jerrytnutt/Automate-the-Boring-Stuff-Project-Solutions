import zombiedice,random

# A bot that, after the first roll, randomly decides if it will continue or stop
class randomChoice:
    def __init__(self, name):
        
        self.name = name

    def turn(self, gameState):
        
        diceRollResults = zombiedice.roll()  

        while diceRollResults is not None:
          
          num = random.randint(0, 1)
          
          if num == 0:
            diceRollResults = zombiedice.roll() 
          else:
            break

# A bot that stops rolling after it has rolled two shotguns      
class twoShotguns:
    def __init__(self, name):
        
        self.name = name

    def turn(self, gameState):
        
        diceRollResults = zombiedice.roll()  
        shotgun = 0
        while diceRollResults is not None:
          shotgun += diceRollResults['shotgun']
          if shotgun < 2:
            diceRollResults = zombiedice.roll() 
          else:
            break


# A bot that initially decides it’ll roll the dice one to four times, but will stop early if it rolls two shotguns
class randomRolls:
    def __init__(self, name):
        
        self.name = name

    def turn(self, gameState):
        rolls = random.randint(1, 4)
        shotgun = 0
        for i in range(rolls):

          diceRollResults = zombiedice.roll()
          shotgun += diceRollResults['shotgun']
          if shotgun >= 2:
            break
       


# A bot that stops rolling after it has rolled more shotguns than brains
class comparisonZombie:
    def __init__(self, name):
        
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()            

        brains = 0
        shotgun = 0
        
       
        while diceRollResults is not None:
            
            
            brains += diceRollResults['brains']
            shotgun += diceRollResults['shotgun']
            if shotgun > brains:
              break
            else:
              diceRollResults = zombiedice.roll() 
            