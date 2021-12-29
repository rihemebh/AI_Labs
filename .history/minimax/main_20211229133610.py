import minimax
import



initial = input("Initial state ")
if(minimax([int(initial)],1) == 1): 
    print("Max is the winner")
else: print('Min in the winner')

