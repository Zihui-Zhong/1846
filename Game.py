import numpy as np

class Game:
    def __init__(self, players, possibleCorps):
        self.players = players
        self.corps = possibleCorps
        self.shares = np.zeros([len(self.players)+1,len(self.corps)])
        self.shareValue = np.zeros((len(self.corps)))
        for a in range(0,len(self.corps)):
            self.shares[0][a] = 10

a = Game(['titan','martin','zihui','alex'],['Best','worst','dump'])

print(a)