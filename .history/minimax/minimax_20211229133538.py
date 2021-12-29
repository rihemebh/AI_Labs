
def minimax( state, turn : int):  
        
        if(isFinal(state)): 
            return utility(turn)
        
        if(turn == 1):
            score = -99999
            for s in getChildren(state): 
                score = max(score, minimax(s , 0))
            return score
        else: 
            score = 99999
            for s in getChildren(state):
                score = min(score, self.minimax(s , 1))
            
            return score


           
              
 
      

            





