import random
from collections import deque


class Board:
    def __init__(self, size):
        self.grid = size
        self.size = size * size
        
    def next_valid_position(self, cur, increment):
        next_pos = cur + increment
        if next_pos > self.size:
            return cur
        return next_pos
    
    def find_row(self, next_pos):
        row = next_pos // self.grid
        if next_pos % self.grid == 0 :
            row -= 1
        return row
    
    def find_col(self, row, next_pos):
        offset = next_pos - (self.grid * row)
        if row % 2 == 0:
            col = 0
            for i in range(offset - 1):
                col += 1
            return col
        else:
            col = self.grid
            for i in range(offset):
                col -= 1
            return col
            
    def find_coordinates(self, next_pos):
        row = self.find_row(next_pos)
        return (self.find_col(row, next_pos), row)
    

class Dice:
    
    @staticmethod
    def roll():
        return random.randint(1, 6)
    

class Player:
    def __init__(self, name):
        self.name = name
        self.dice = [0]
        self.pos = [0]
        self.coor = [(0, 0)]


board = Board(3)


players = deque()
players.append(Player("1"))
players.append(Player("2"))
players.append(Player("3"))


while True:
    cur_player = players.popleft()
    increment = Dice.roll()
    cur_player.dice.append(increment)
    next_pos = board.next_valid_position(cur_player.pos[-1], increment)
    coor = board.find_coordinates(next_pos)
    cur_player.coor.append(coor)
    cur_player.pos.append(next_pos)
    for player in players:
        if next_pos == player.pos[-1]:
            print(f"{cur_player.name} is cutting {player.name}")
            player.pos.append(0)
    
    if next_pos == board.size:
        print(f"{cur_player.name} is winner")
        print(f"winer positions", cur_player.pos)
        print(f"winer dice history", cur_player.dice)
        print(f"winer coor history", cur_player.coor)
        
        print("other guys position")
        for player in players:
            print(f"{player.name} pos: {player.pos}")
            print(f"{player.name} dice: {player.dice}")
            print(f"{player.name} coor: {player.coor}")
            
        break
        
    players.append(cur_player)