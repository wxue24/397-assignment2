from location import Location
from agent import Agent
import numpy
from STM import IDENTITY, PROBABILITIES, REWARDS

NUM_TREASURE = 3
NUM_LOCATIONS = 10
GAMMA = 0.9


def simulate(episodes: int, agent_steps_limit=25):
    treasure_locations = [3, 6, 8]

    # create locations
    locations: list[Location] = []
    for i in range(NUM_LOCATIONS):
        if i in treasure_locations:
            locations.append(Location(i, True))
        else:
            locations.append(Location(i, False))

    for e in range(1, episodes + 1):
        agent = Agent(locations)
        while agent.getSteps() <= agent_steps_limit and not agent.atTerminal():
            print(
                "Steps: {} | location: {} | current reward: {}".format(
                    agent.getSteps(), agent.getLocation(), agent.getRewards()
                )
            )

            action, reward = agent.randomAction()
            print("Agent", action, "and got", reward, "rewards")

        print("History of episode", e)
        if agent.atTerminal():
            print("Terminal state reached")
        print("Total reward:", agent.getRewards())
        print("")

    # Use closed form of bellman equation
    values: numpy.ndarray = numpy.dot(
        numpy.linalg.inv(IDENTITY - GAMMA * PROBABILITIES), REWARDS
    )
    print("Values of each state (location)")
    for i in range(10):
        print("Location: {} | Reward: {} | Value: {}".format(i, REWARDS[i], round(values[0, i], 2)))
    print("Optimal policy: 0 -> 2 -> 6 -> 9")
    print("The MDP is solved given my optimal policy")
    print("Max reward possible: -1 + 0.9(-1) + 0.9^2(2) + 0.9^3(15) = 10.65")


simulate(10, 25)
