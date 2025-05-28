import random
from collections import deque


class Board:
    def __init__(self, size):
        self.size = size * size
        
    def next_valid_position(self, cur, increment):
        next_pos = cur + increment
        if next_pos > self.size:
            return cur
        return next_pos
    

class Dice:
    
    @staticmethod
    def roll():
        return random.randint(1, 6)
    

class Player:
    def __init__(self, name):
        self.name = name
        self.dice = [0]
        self.pos = [0]


board = Board(4)


players = deque()
players.append(Player("1"))
players.append(Player("2"))
players.append(Player("3"))


while True:
    cur_player = players.popleft()
    increment = Dice.roll()
    cur_player.dice.append(increment)
    next_pos = board.next_valid_position(cur_player.pos[-1], increment)
    cur_player.pos.append(next_pos)
    for player in players:
        if next_pos == player.pos[-1]:
            print(f"{cur_player.name} is cutting {player.name}")
            player.pos.append(0)
    
    if next_pos == board.size:
        print(f"{cur_player.name} is winner")
        print(f"winer positions", cur_player.pos)
        print(f"winer dice history", cur_player.dice)
        
        print("other guys position")
        for player in players:
            print(f"{player.name} pos: {player.pos}")
            print(f"{player.name} dice: {player.dice}")
            
        break
        
    players.append(cur_player)