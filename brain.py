import random

class Brain:
    def __init__(self, dirs=[], size=0) -> None:
        def_dirs = []
        for i in range(size):
            dir = (random.randint(-1, 1), random.randint(-1, 1), random.randint(1, 9))
            def_dirs.append(dir)
            
        self.dirs = def_dirs if dirs==[] else dirs
        self.step = 0


    def randomize(self, size):
        self.dirs = []
        for i in range(size):
            dir = (random.randint(-1, 1), random.randint(-1, 1), random.randint(1, 9))
            self.dirs.append(dir)

    
    def clone(self):
        return Brain(self.dirs.copy())


    def mutate(self):
        mutation_rate = 0.01
        for i in range(len(self.dirs)):
            rand = random.random()
            if rand < mutation_rate:
                dir = (random.randint(-1, 1), random.randint(-1, 1), random.randint(1, 9))
                self.dirs[i] = dir
