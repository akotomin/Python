import sys


class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return self.score > 0


lst_in = list(map(str.strip, sys.stdin.readlines()))
players = []

for i in lst_in:
    parts = i.split('; ')
    obj = Player(parts[0], int(parts[1]), int(parts[2]))
    players.append(obj)

players_filtered = list(filter(bool, players))
print(players_filtered)
