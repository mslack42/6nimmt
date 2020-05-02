# 6Nimmt test harness

from Objects import *
from Utilities import *
from Simulation import *
from NaiveStrategies import *   

player1 = Player("HornsThenExtremes50", HornsThenExtremesStrategy(50))
player2 = Player("Boggle2", BoggleStrategy())
player3 = Player("ExtremesFirst50", ExtremesFirstStrategy(50))
player4 = Player("Boggle4", BoggleStrategy())
player5 = Player("Boggle5", BoggleStrategy())
player6 = Player("Boggle6", BoggleStrategy())
players=[player1, player2, player3, player4, player5, player6]

playManyGames(players, 1000)
