from re import X
from brain import Brain

class Bot:
    def __init__(self) -> None:
        self.brain = Brain(size=100)
        self.x, self.y, self.val = 0, 0, 0
        self.cellFilled, self.cellLeft = 0, 0
        self.dead, self.finished, self.isBest = False, False, False
        self.fitness = 0.0


    def move(self):
        b = self.brain
        if len(b.dirs) > b.step:
            self.x, self.y, self.val = b.dirs[b.step]
            b.step += 1
        else:
            self.dead = True
        return (self.x, self.y, self.val)

    
    def calculate_fitness(self):
        if self.finished:
            fitness = 0
        else:
            fitness = 0
        return fitness


    def make_baby(self):
        baby = Bot()
        baby.brain = self.brain.clone()
        return baby
