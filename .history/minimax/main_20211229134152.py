from minimax import minimax
from alphabeta import alphabeta



initial = input("Initial state ")

if(minimax([int(initial)],1) == 1): 
    print("Max is the winner")
else: print('Min in the winner')
"""

### Alpha - beta

print(alphabeta([int(initial)],1, -99999, 99999))
"""