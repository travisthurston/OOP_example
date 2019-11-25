#this class needs to inherit the attributes and behaviors of the Card class\
# a minion object is a card
#Child or derived class
from Card import Card
class Minion(Card):
    #Inherits cost and name from Parent class card
    def __init__(self, cost, name, damage, life):
        Card.__init__(self,cost, name)
        #assign parameters to the object
        self.damage = damage
        self.life = life

    def printMinionInfo(self):
        print("Name:" + self.name)
        print("Cost:" + str(self.cost))
        print("Damage:" + str(self.damage))
        print("Life:" + str(self.life))
