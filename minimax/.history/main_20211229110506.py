import minimax


g = minimax.Game([7])
# turn 1 : max and min is 0


#print(g.max([minimax.State([7],0), minimax.State([7],1)]))

if(g.minimax([18],1) == 1): 
    print("Max is the winner")
else: print('Min in the winner')