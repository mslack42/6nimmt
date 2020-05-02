# Utility functions for simulating 6Nimmt

from Objects import *

def getHorns(number):
    if (number == 55):
        return 7
    elif (number % 11 == 0):
        return 5
    elif (number % 10 == 0):
        return 3
    elif (number % 5 == 0):
        return 2
    else:
        return 1

def calculateRowScore(row):
    score = 0
    for card in row:
        score += card.horns
    return score

def calculateRow(board, card):
    selectedIndex = None
    selectedIndexCurrentEndNumber = None
    for i in range(4):
        row = board.rows[i]
        rowEndNumber = row[len(row) - 1].number
        if (rowEndNumber < card.number):
            if (selectedIndexCurrentEndNumber is None or selectedIndexCurrentEndNumber > rowEndNumber):
                selectedIndex = i
                selectedIndexCurrentEndNumber = rowEndNumber
    return selectedIndex

def printHand(player):
    print([ card.number for card in player.hand])

def printScores(players):
    rankedPlayers = sorted(players, key=lambda player: player.score, reverse=True)
    print([ player.name + ": " + str(player.score) for player in rankedPlayers])
