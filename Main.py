from Card import Card
from Minion import Minion

def main():
    #create the Town Crier Card
    #cost =1 and name = Town Crier
    #instantiate an object called Town_Crier
    #creating and instance of the class
    townCrier = Minion(1, 'Town Crier', 1, 2)
        
    #create and instance of the class Card called RedBand Wasp
    #attributes cost =2, Name = RedBandWasp
    redbandWasp = Minion(2, "Redband Wasp", 1, 3)

    #create an instacne of the Card class caleld Warpath
    #cost = 2, Name = Warpath
    warPath = Card(2, 'Warpath')


    townCrier.printCardInfo()
    townCrier.printMinionInfo()

    redbandWasp.printCardInfo()
    warPath.printCardInfo()

if __name__== "__main__":
    main()