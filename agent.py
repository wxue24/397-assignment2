from location import Location
from STM import STM
import random

DIG_PROB = 0.1
MOVE_PROB = 0.9
INITIAL_LOC = 0
TERMINAL_LOC = 9
GAMMA = 0.9

class Agent(object):

    def __init__(self, treasure_locations: list[int], locations: list[Location]):
        self.treasure_locations = treasure_locations
        self.location = INITIAL_LOC
        self.locations = locations
        self.rewards = 0
        self.treasures_found = 0
        self.steps = 0

    def getSteps(self):
        return self.steps

    def getLocation(self):
        return self.location

    def getRewards(self):
        return round(self.rewards, 2)

    def atTerminal(self):
        return self.location == TERMINAL_LOC

    def randomAction(self) -> tuple[str, int]:
        self.steps += 1

        if random.random() <= DIG_PROB and not self.locations[self.location].hasBeenDug():
            # Dig
            if self.locations[self.location].dig():
                self.rewards += 2 * GAMMA ** self.steps
                self.treasures_found += 1
                return ("dig", 2)
            return ("dig", 0)

        else:
            self.rewards -= 1
            # Randomly choose where to go next based on STM
            locations: list[int] = []
            probabilities: list[int] = []
            for end_loc, prob in STM[self.location]:
                locations.append(end_loc - 1)
                probabilities.append(prob)
            choice = random.choices(
                population=locations, weights=probabilities, k=1)[0]
            self.location = choice

            if self.location == TERMINAL_LOC:
                if self.treasures_found == 3:
                    self.rewards += 15 * GAMMA ** self.steps
                    return ("move", 15)
                else:
                    self.rewards += 5 * GAMMA ** self.steps
                    return ("move", 5)
            return ("move", -1)
