import minimax


g = minimax.Game([7])
print()
if(g.minimax([4],1) == 1): 
    print("Max is the winner")
else: print('Min in the winner')