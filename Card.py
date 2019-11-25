#Card class is a blueprint of the card object
#This is the parent or base class for Minion
class Card:

    #initializer to create the attributes of every class object
    def __init__(self, cost, name):
        self.cost = cost
        self.name = name
        #attributes - argument - parameter - describes the object
        #give the card a cost attribute
        #give the card a name attribute


#behaviors - methods - functions
    def printCardInfo(self):
        print("Name:" + self.name)
        print("Cost:" + str(self.cost))
        

