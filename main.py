import salabim as sim
import random
import numpy as np


class Machine(sim.Component):
    def __init__(self, distribution, delay=0):
        super().__init__()
        self.distribution = distribution
        self.delay = delay
        self.count = 0

    def process(self):
        self.hold(self.delay)
        while True:
            amount = int(self.distribution.sample())
            for _ in range(amount):
                WindScreenWiper()
                self.count += 1
            self.hold(1)

class WindScreenWiper(sim.Component):
    count = 0
    def process(self):
        WindScreenWiper.count += 1
        pass


# TODO: statistics
dist_extrudor3 =
dist_extrudor4 =
dist_extrudor5 = # dgamma a = 0.9074  loc 16147   scale 2431,4683

env = sim.Environment()

Extrudor3 = Machine(dist_extrudor3)
Extrudor4 = Machine(dist_extrudor4)
Extrudor5 = Machine(dist_extrudor5)

numDays = 10
numShifts = numDays * 3

env.run(till=numShifts)

print(WindScreenWiper.count)
