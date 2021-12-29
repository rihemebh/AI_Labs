
from minimax.utils import isFinal,utility


def alphabeta(state, turn : int, alpha , beta ):  
        
        if(isFinal(state)): 
            return utility(turn)
        
        if(turn == 1):
            score = -99999
            for s in getChildren(state): 
                score = max(score, alphabeta(s , 0, alpha , beta))
                if (score >= beta): return score
                alpha = min(alpha,score)
            return score
        else: 
            score = 99999
            for s in getChildren(state):
                score = min(score, alphabeta(s , 1, alpha , beta))
                if (score <= alpha):  return score
                beta = min(beta,score)
            return score