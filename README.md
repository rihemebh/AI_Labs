# Minimax & alpha -beta algorithms 

## Game
At the beginning, we have a stack of n tokens. The players take turns dividing one of the piles in front of them into two non-empty piles of different sizes. On each turn of the game, a new stack is therefore created. From the game configuration with three stacks of 2, 3 and 2 tokens respectively, the only playable move is to divide the stack containing 3 tokens into two stacks: one with 2 tokens and the other a single token. The player who can no longer play (i.e. there are only stacks of 1 or 2 chips left) has lost.

