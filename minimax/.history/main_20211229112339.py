import minimax


g = minimax.Game([7])
initial = input("Initial state ")
if(g.minimax([initi],1) == 1): 
    print("Max is the winner")
else: print('Min in the winner')