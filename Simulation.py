# Functions for simulating rounds of 6Nimmt

from Objects import *
from Utilities import *

def playRound(players, board):
    for player in players:
        player.pickCard(board, players)
       
    players = sorted(players, key = lambda p: p.selectedCard.number)

    for player in players:
        selectedRowNum = calculateRow(board, player.selectedCard)
        if (selectedRowNum is None):
            selectedRowNum = player.pickRow(board, players)
        player.playCard(board, selectedRowNum)

def playGame(players):
    board = Board()
    deck = Deck()
    deck.dealCards(players, board)

    #for player in players:
    #    printHand(player)
   
    for i in range(10):
        playRound(players, board)

def playManyGames(players, gameCount):
    for i in range(gameCount):
        #print("Playing game " + str(i))
        playGame(players)

    printScores(players)
