# 397-assignment2

## Defining the MDP

1. States

   - Locations 1-10
   - 1 is the initial state, 10 is the terminal

2. State information at each state
   - Agent current reward, location, time steps
   - Locations' name, treasure, inital/terminal
  
3. Set of Agent actions
   - Move, dig
  
4. Gamma (0.9)
  
5. State Transition Matrix

![State Transition Matrix drawio-5](https://github.com/wxue24/397-assignment2/assets/64175276/0178e631-929a-4ea4-b1bd-d094ba20e325)

![State Transition Matrix drawio-4](https://github.com/wxue24/397-assignment2/assets/64175276/4ba97d8e-0f78-4bcb-8882-bed7bcf39d6f)


7. Reward function
   - If agent digs at a treasure location he gets +2 
   - If agent moves from location to location he gets -1
   - If agent lands on terminal state he gets +5
   - If agent lands on terminal state and finds all three buried treasures he gets +15

## Running episodes

Navigate to the directory and run `python3 simulation.py`. If you need to change simulation parameters (number of episodes, max number of steps agent can take), modify `simulate(10,25)`

