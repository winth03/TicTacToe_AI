from bot import Bot

class Population:
    def __init__(self, size) -> None:
        bots = []
        for i in range(size):
            bots.append(Bot())
        self.bots = bots

        self.gen = 1
        self.bestBot = 0
        self.minStep = 100
