import minimax


g = minimax.Game([7])

if(g.minimax([18],1) == 1): 
    print("Max is the winner")
else: print('Min in the winner')