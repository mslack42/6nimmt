# Objects in a game of 6Nimmt

import random
from Utilities import *

class Card:
    number = 0
    horns = 0
   
    def __init__(self, num):
        self.number = num
        self.horns = getHorns(num)

class Deck:
    cards = []

    def __init__(self):
        for i in range(1, 105):
            self.cards.append(Card(i))
        random.shuffle(self.cards)

    def dealCard(self):
        return self.cards.pop()

    def dealCards(self, players, board):
        for player in players:
            while len(player.hand) < 10:
                player.hand.append(self.dealCard())
        for i in range(4):
            board.rows.append([self.dealCard()])
       
class Player:
    hand = []
    name = ""
    score = 0
    strategy = None
    selectedCard = None

    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
        self.hand = []
        self.score = 0
        self.selectedCard = None

    def pickCard(self, board, players):
        #print("Picking card - " + self.name)
        self.strategy.selectCard(board, players, self)

    def pickRow(self, board, players):
        return self.strategy.selectRow(board, players, self)

    def playCard(self, board, rowNum):
        #print("Playing card - " + self.name + " - " + str(self.selectedCard.number))
        selectedRow = board.rows[rowNum]
        if (self.selectedCard.number < selectedRow[len(selectedRow)-1].number):
            # Taking a row
            self.score = self.score + calculateRowScore(selectedRow)
            board.rows[rowNum] = [self.selectedCard]
        else:
            # Placing on the end of a row
            if (len(board.rows[rowNum]) == 5):
                # 6 Nimmt!!!
                self.score = self.score + calculateRowScore(selectedRow)
                board.rows[rowNum] = [self.selectedCard]
            else:
                board.rows[rowNum].append(self.selectedCard)
        self.selectedCard = None

class Board:
    rows = []
