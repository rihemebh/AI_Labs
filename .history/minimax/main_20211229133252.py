import minimax
import


g = minimax.Game()
initial = input("Initial state ")
if(g.minimax([int(initial)],1) == 1): 
    print("Max is the winner")
else: print('Min in the winner')

