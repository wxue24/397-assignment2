from location import Location
from agent import Agent
import random

NUM_TREASURE = 3
NUM_LOCATIONS = 10


def simulate(episodes: int, agent_steps_limit=25):
    treasure_locations = random.sample(range(NUM_LOCATIONS), NUM_TREASURE)

    # create locations
    locations: list[Location] = []
    for i in range(NUM_LOCATIONS):
        if i in treasure_locations:
            locations.append(Location(i, True))
        else:
            locations.append(Location(i, False))

    for e in range(1, episodes + 1):
        agent = Agent(treasure_locations, locations)
        while agent.getSteps() <= agent_steps_limit and not agent.atTerminal():


            print("Steps: {} | location: {} | current reward: {}".format(agent.getSteps(), agent.getLocation(), agent.getRewards()))

            
            action, reward = agent.randomAction()
            print("Agent", action, "and got", reward, "rewards")

        print("History of episode", e)
        if agent.atTerminal():
            print("Terminal state reached")
        print("Total reward:", agent.getRewards())
        print("")
        


simulate(10, 25)
