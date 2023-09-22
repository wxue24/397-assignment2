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

   ![State Transition Matrix drawio-2](https://github.com/wxue24/397-assignment2/assets/64175276/5ea72347-70d0-4785-9cd4-392a5a36c36b)

6. Reward function
   - If agent digs at a treasure location he gets +10
   - If agent digs at wrong location he gets -1
   - If agent moves to location he hasn't been to he gets +1
   - If agent moves to location he has been to he gets -1

