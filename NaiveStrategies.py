# Naive 6Nimmt strategies (that any decent strategy should be able to beat)

import random
from Objects import *
from Utilities import *

class DefaultStrategy:
    def selectCard(self, board, players, currentPlayer):
        random.shuffle(currentPlayer.hand)
        currentPlayer.selectedCard = currentPlayer.hand.pop()

    def selectRow(self, board, players, currentPlayer):
        lowestScore = calculateRowScore(board.rows[0])
        selectedIndex = 0
        for i in range(1,4):
            row = board.rows[i]
            if (calculateRowScore(row) < lowestScore):
                lowestScore = calculateRowScore(row)
                selectedIndex = i
        return selectedIndex

class BoggleStrategy(DefaultStrategy):
    # This is the default strategy to compare against

    #def selectCard(self, board, players, currentPlayer):
    #def selectRow(self, board, players, currentPlayer):

    pass

class InOrderStrategy(DefaultStrategy):
    def selectCard(self, board, players, currentPlayer):
        currentPlayer.hand = sorted(currentPlayer.hand, key=lambda card: card.number)
        currentPlayer.selectedCard = currentPlayer.hand.pop()

class ExtremesFirstStrategy(DefaultStrategy):
    pivotPoint = 50

    def __init__(self, pivotPoint = 50):
        self.pivotPoint = pivotPoint
   
    def selectCard(self, board, players, currentPlayer):
        currentPlayer.hand = sorted(currentPlayer.hand, key=lambda card: abs(self.pivotPoint - card.number))
        currentPlayer.selectedCard = currentPlayer.hand.pop()

class NaiveHornsFirstStrategy(DefaultStrategy):
    def selectCard(self, board, players, currentPlayer):
        currentPlayer.hand = sorted(currentPlayer.hand, key=lambda card: card.horns)
        currentPlayer.selectedCard = currentPlayer.hand.pop()

class HornsThenExtremesStrategy(DefaultStrategy):
    pivotPoint = 50

    def __init__(self, pivotPoint = 50):
        self.pivotPoint = pivotPoint
       
    def selectCard(self, board, players, currentPlayer):
        currentPlayer.hand = sorted(currentPlayer.hand, key=lambda card: card.horns)
        if (currentPlayer.hand[-1].horns > 2):
            currentPlayer.selectedCard = currentPlayer.hand.pop()
        else:
            currentPlayer.hand = sorted(currentPlayer.hand, key=lambda card: abs(self.pivotPoint - card.number))
            currentPlayer.selectedCard = currentPlayer.hand.pop()
