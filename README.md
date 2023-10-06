# 397-assignment2

## Defining the MDP

1. States

   - Locations 0-9
   - 0 is the initial state, 9 is the terminal
   - 3,6,8 have treasure

2. State information at each state
   - Name
   - Whether it has treasure
   - Whether it has been dug
  
4. Set of Agent actions
   - Move (90% probability), dig (10% probability)
  
5. Apply gamma of 0.9 at every time step
  
6. State Transition Matrix

![State Transition Matrix drawio-5](https://github.com/wxue24/397-assignment2/assets/64175276/0178e631-929a-4ea4-b1bd-d094ba20e325)

![State Transition Matrix drawio-4](https://github.com/wxue24/397-assignment2/assets/64175276/4ba97d8e-0f78-4bcb-8882-bed7bcf39d6f)


6. Reward function
   - If agent digs at a treasure location he gets +2 
   - If agent moves from location to location he gets -1
   - If agent lands on terminal state he gets +5
   - If agent lands on terminal state and finds all three buried treasures he gets +15

## Value Function

The value function's purpose within the context of my MRP is to help the agent discover the optimal policy, or in this case to get to the terminal island with the highest reward. In order to simplify the process, we define the rewards for each location as -1 for 6/10 islands, +3 for 3/10 islands, and +15 for the terminal island. In the `simulate` method we calculate the values for each state using the closed form of the bellman equation, and print those values out. These values allow us to determine the optimal policy (the agent should choose the transition leading to the highest value). The value of each island is printed out. The optimal policy as discovered by the value calculations is 0 -> 2 -> 6 -> 9, which solves the MDP. The maximum reward is thus -1 + 0.9(-1) + 0.9^2(2) + 0.9^3(15) = 10.65.

## Packages

Install `numpy` in your env.
## Running episodes

Navigate to the directory and run `python3 simulation.py`. If you need to change simulation parameters (number of episodes, max number of steps agent can take), modify `simulate(10,25)`

